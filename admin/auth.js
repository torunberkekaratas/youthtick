/* ─────────────────────────────────────────────────────────────
   YouthTICK Super Admin — Authentication System
   Secure client-side auth with hashed passwords, brute-force
   protection, and session management.
   ───────────────────────────────────────────────────────────── */

const AUTH = {
  STORAGE_KEY_USERS:    'yt-admin-users',
  STORAGE_KEY_SESSION:  'yt-admin-session',
  STORAGE_KEY_ATTEMPTS: 'yt-admin-attempts',
  SESSION_DURATION_MS:  8 * 60 * 60 * 1000, // 8 hours
  MAX_ATTEMPTS:         5,
  LOCKOUT_MS:           10 * 60 * 1000,      // 10 minutes
  SALT:                 'yt-institutional-salt-2026',

  /* ── Password hashing (Web Crypto API SHA-256) ─────────── */
  async hashPassword(password) {
    const encoder = new TextEncoder();
    const data = encoder.encode(password + this.SALT);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    return Array.from(new Uint8Array(hashBuffer))
      .map(b => b.toString(16).padStart(2, '0'))
      .join('');
  },

  /* ── Initialize default users on first run ─────────────── */
  async initialize() {
    const VERSION = 'v2'; // bump when default credentials change
    const storedVersion = localStorage.getItem('yt-admin-init-version');
    const existing = localStorage.getItem(this.STORAGE_KEY_USERS);

    if (!existing || storedVersion !== VERSION) {
      const defaultHash = await this.hashPassword('Torunalimertenes775556');
      const defaultUsers = [
        {
          id:           'sa-001',
          email:        'admin@youthtick.org',
          name:         'Super Administrator',
          role:         'super-admin',
          passwordHash: defaultHash,
          avatar:       'SA',
          createdAt:    new Date().toISOString(),
          lastLogin:    null,
          active:       true
        }
      ];
      localStorage.setItem(this.STORAGE_KEY_USERS, JSON.stringify(defaultUsers));
      localStorage.setItem('yt-admin-init-version', VERSION);
      return defaultUsers;
    }
    return JSON.parse(existing);
  },

  /* ── Brute-force protection ─────────────────────────────── */
  getAttempts(email) {
    const all = JSON.parse(localStorage.getItem(this.STORAGE_KEY_ATTEMPTS) || '{}');
    return all[email] || { count: 0, lockoutUntil: 0 };
  },
  recordAttempt(email) {
    const all = JSON.parse(localStorage.getItem(this.STORAGE_KEY_ATTEMPTS) || '{}');
    const current = all[email] || { count: 0, lockoutUntil: 0 };
    current.count++;
    if (current.count >= this.MAX_ATTEMPTS) {
      current.lockoutUntil = Date.now() + this.LOCKOUT_MS;
      current.count = 0;
    }
    all[email] = current;
    localStorage.setItem(this.STORAGE_KEY_ATTEMPTS, JSON.stringify(all));
    return current;
  },
  clearAttempts(email) {
    const all = JSON.parse(localStorage.getItem(this.STORAGE_KEY_ATTEMPTS) || '{}');
    delete all[email];
    localStorage.setItem(this.STORAGE_KEY_ATTEMPTS, JSON.stringify(all));
  },
  isLockedOut(email) {
    const { lockoutUntil } = this.getAttempts(email);
    return Date.now() < lockoutUntil;
  },
  getLockoutRemaining(email) {
    const { lockoutUntil } = this.getAttempts(email);
    return Math.max(0, Math.ceil((lockoutUntil - Date.now()) / 1000));
  },

  /* ── Login ──────────────────────────────────────────────── */
  async login(email, password) {
    const users = JSON.parse(localStorage.getItem(this.STORAGE_KEY_USERS) || '[]');

    if (this.isLockedOut(email)) {
      const secs = this.getLockoutRemaining(email);
      return { success: false, error: `Too many attempts. Try again in ${secs}s.`, locked: true };
    }

    const user = users.find(u => u.email.toLowerCase() === email.toLowerCase() && u.active);
    if (!user) {
      this.recordAttempt(email);
      return { success: false, error: 'Invalid credentials.' };
    }

    const hash = await this.hashPassword(password);
    if (hash !== user.passwordHash) {
      const attempt = this.recordAttempt(email);
      const remaining = this.MAX_ATTEMPTS - attempt.count;
      return {
        success: false,
        error: remaining > 0
          ? `Invalid credentials. ${remaining} attempt${remaining > 1 ? 's' : ''} remaining.`
          : 'Account temporarily locked due to too many attempts.'
      };
    }

    // Success
    this.clearAttempts(email);
    const session = {
      userId:  user.id,
      email:   user.email,
      name:    user.name,
      role:    user.role,
      avatar:  user.avatar,
      expires: Date.now() + this.SESSION_DURATION_MS,
      loginAt: new Date().toISOString()
    };
    sessionStorage.setItem(this.STORAGE_KEY_SESSION, JSON.stringify(session));

    // Update last login
    user.lastLogin = new Date().toISOString();
    localStorage.setItem(this.STORAGE_KEY_USERS, JSON.stringify(users));

    // Log activity
    STORE.logActivity('auth', `${user.name} signed in`, user.email);

    return { success: true, user: session };
  },

  /* ── Get current session ────────────────────────────────── */
  getSession() {
    try {
      const raw = sessionStorage.getItem(this.STORAGE_KEY_SESSION);
      if (!raw) return null;
      const session = JSON.parse(raw);
      if (Date.now() > session.expires) {
        this.logout();
        return null;
      }
      return session;
    } catch { return null; }
  },

  /* ── Require auth — redirect if not authenticated ───────── */
  requireAuth() {
    const session = this.getSession();
    if (!session) {
      const expired = sessionStorage.getItem('yt-session-was-active');
      const url = expired
        ? 'index.html?expired=1'
        : 'index.html';
      window.location.href = url;
      return null;
    }
    return session;
  },

  /* ── Logout ─────────────────────────────────────────────── */
  logout() {
    const session = this.getSession();
    if (session) STORE.logActivity('auth', `${session.name} signed out`, session.email);
    sessionStorage.setItem('yt-session-was-active', '1');
    sessionStorage.removeItem(this.STORAGE_KEY_SESSION);
    window.location.href = 'index.html';
  },

  /* ── Permission check ───────────────────────────────────── */
  can(session, permission) {
    const PERMISSIONS = {
      'super-admin': ['*'],
      'admin':       ['content', 'blog', 'media', 'translations', 'design', 'analytics'],
      'editor':      ['content', 'blog', 'media'],
      'content-manager': ['content', 'blog'],
      'translator':  ['translations']
    };
    const perms = PERMISSIONS[session?.role] || [];
    return perms.includes('*') || perms.includes(permission);
  }
};
