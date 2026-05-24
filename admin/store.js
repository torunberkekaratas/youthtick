/* ─────────────────────────────────────────────────────────────
   YouthTICK Super Admin — Data Store
   Central data layer for all admin content, media, blog, settings.
   ───────────────────────────────────────────────────────────── */

const STORE = {
  KEYS: {
    CONTENT:   'yt-admin-content',
    DESIGN:    'yt-admin-design',
    BLOG:      'yt-admin-blog',
    MEDIA:     'yt-admin-media',
    SETTINGS:  'yt-admin-settings',
    ACTIVITY:  'yt-admin-activity',
    USERS:     'yt-admin-users'
  },

  /* ── Generic get/set ────────────────────────────────────── */
  get(key)         { try { return JSON.parse(localStorage.getItem(key) || 'null'); } catch { return null; } },
  set(key, value)  { localStorage.setItem(key, JSON.stringify(value)); },

  /* ══════════════════════════════════════════════════════════
     CONTENT STORE — i18n overrides per language
     ══════════════════════════════════════════════════════════ */
  getContent()     { return this.get(this.KEYS.CONTENT) || { en: {}, tr: {}, de: {} }; },
  setContent(data) { this.set(this.KEYS.CONTENT, data); },

  getContentKey(lang, key) {
    const content = this.getContent();
    return content[lang]?.[key] ?? null;
  },
  setContentKey(lang, key, value) {
    const content = this.getContent();
    if (!content[lang]) content[lang] = {};
    content[lang][key] = value;
    this.setContent(content);
  },
  setContentBatch(lang, updates) {
    const content = this.getContent();
    if (!content[lang]) content[lang] = {};
    Object.assign(content[lang], updates);
    this.setContent(content);
  },

  /* ══════════════════════════════════════════════════════════
     DESIGN STORE — CSS custom property overrides
     ══════════════════════════════════════════════════════════ */
  getDesign()     { return this.get(this.KEYS.DESIGN) || {}; },
  setDesign(data) { this.set(this.KEYS.DESIGN, data); },
  setDesignVar(varName, value) {
    const design = this.getDesign();
    design[varName] = value;
    this.setDesign(design);
  },

  /* ══════════════════════════════════════════════════════════
     BLOG STORE
     ══════════════════════════════════════════════════════════ */
  getBlog() {
    return this.get(this.KEYS.BLOG) || { posts: [] };
  },
  saveBlog(data)  { this.set(this.KEYS.BLOG, data); },
  getAllPosts()    { return this.getBlog().posts; },
  getPost(id)     { return this.getAllPosts().find(p => p.id === id) || null; },
  savePost(post) {
    const blog = this.getBlog();
    const idx = blog.posts.findIndex(p => p.id === post.id);
    if (idx >= 0) blog.posts[idx] = post;
    else blog.posts.unshift(post);
    this.saveBlog(blog);
  },
  deletePost(id) {
    const blog = this.getBlog();
    blog.posts = blog.posts.filter(p => p.id !== id);
    this.saveBlog(blog);
  },
  generatePostId() { return 'post-' + Date.now() + '-' + Math.random().toString(36).slice(2,7); },
  generateId()     { return Date.now().toString(36) + Math.random().toString(36).slice(2,7); },

  /* ══════════════════════════════════════════════════════════
     MEDIA STORE
     ══════════════════════════════════════════════════════════ */
  getMedia()     { return this.get(this.KEYS.MEDIA) || { items: [] }; },
  saveMedia(data){ this.set(this.KEYS.MEDIA, data); },
  getAllMedia()   { return this.getMedia().items; },
  addMedia(item) {
    const media = this.getMedia();
    media.items.unshift({ ...item, id: 'media-' + Date.now(), uploadedAt: new Date().toISOString() });
    this.saveMedia(media);
    return media.items[0];
  },
  deleteMedia(id) {
    const media = this.getMedia();
    media.items = media.items.filter(m => m.id !== id);
    this.saveMedia(media);
  },
  updateMediaAlt(id, alt) {
    const media = this.getMedia();
    const item = media.items.find(m => m.id === id);
    if (item) { item.alt = alt; this.saveMedia(media); }
  },

  /* ══════════════════════════════════════════════════════════
     SETTINGS STORE
     ══════════════════════════════════════════════════════════ */
  getSettings() {
    return this.get(this.KEYS.SETTINGS) || {
      siteName: 'YouthTICK',
      siteTagline: 'European Youth Network',
      email: 'info@youthtick.org',
      phone: '',
      addressBerlin: 'Berlin, Germany',
      addressIstanbul: 'Istanbul, Turkey',
      instagram: 'https://instagram.com',
      linkedin: 'https://linkedin.com',
      twitter: '',
      youtube: '',
      maintenanceMode: false,
      googleAnalyticsId: '',
      established: '2026'
    };
  },
  saveSettings(data) { this.set(this.KEYS.SETTINGS, data); },

  /* ══════════════════════════════════════════════════════════
     ACTIVITY LOG
     ══════════════════════════════════════════════════════════ */
  logActivity(type, message, user = 'System') {
    const all = this.get(this.KEYS.ACTIVITY) || [];
    all.unshift({
      id:        Date.now(),
      type,
      message,
      user,
      timestamp: new Date().toISOString()
    });
    // Keep last 200 entries
    this.set(this.KEYS.ACTIVITY, all.slice(0, 200));
  },
  getActivity(limit = 50) {
    return (this.get(this.KEYS.ACTIVITY) || []).slice(0, limit);
  },

  /* ══════════════════════════════════════════════════════════
     USERS STORE
     ══════════════════════════════════════════════════════════ */
  getUsers()      { return this.get(this.KEYS.USERS) || []; },
  saveUsers(data) { this.set(this.KEYS.USERS, data); },
  getUser(id)     { return this.getUsers().find(u => u.id === id) || null; },
  saveUser(user) {
    const users = this.getUsers();
    const idx = users.findIndex(u => u.id === user.id);
    if (idx >= 0) users[idx] = user;
    else users.push(user);
    this.saveUsers(users);
  },
  deleteUser(id) {
    const users = this.getUsers().filter(u => u.id !== id);
    this.saveUsers(users);
  },

  /* ══════════════════════════════════════════════════════════
     HELPERS
     ══════════════════════════════════════════════════════════ */
  formatDate(iso) {
    if (!iso) return '—';
    return new Date(iso).toLocaleDateString('en-GB', {
      day: '2-digit', month: 'short', year: 'numeric',
      hour: '2-digit', minute: '2-digit'
    });
  },
  formatDateShort(iso) {
    if (!iso) return '—';
    return new Date(iso).toLocaleDateString('en-GB', {
      day: '2-digit', month: 'short', year: 'numeric'
    });
  },
  escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  },
  truncate(str, n = 80) {
    if (!str) return '';
    return str.length > n ? str.slice(0, n) + '…' : str;
  }
};
