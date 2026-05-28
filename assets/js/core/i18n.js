import en from '../locales/en.js';
import tr from '../locales/tr.js';
import de from '../locales/de.js';

const TRANSLATIONS = { en, tr, de };
const SUPPORTED = ['en', 'tr', 'de'];

// ─────────────────────────────────────────
// URL helpers
// ─────────────────────────────────────────

/** Return language prefix from pathname, e.g. '/tr/blog.html' → 'tr' */
function pathLang() {
  const p = window.location.pathname;
  if (p.startsWith('/tr/') || p === '/tr') return 'tr';
  if (p.startsWith('/de/') || p === '/de') return 'de';
  return null;
}

/** Strip any existing /tr/ or /de/ prefix from a pathname */
function stripLangPrefix(pathname) {
  return pathname.replace(/^\/(tr|de)(\/|$)/, '/') || '/';
}

/** Build the path for a given language */
function buildLangPath(lang, pathname) {
  const clean = stripLangPrefix(pathname);
  if (lang === 'en') return clean;                  // English → no prefix
  return '/' + lang + (clean.startsWith('/') ? clean : '/' + clean);
}

// ─────────────────────────────────────────
// Language detection
// ─────────────────────────────────────────

function detectLanguage() {
  // 1. URL path prefix — canonical form (/tr/page.html)
  const fromPath = pathLang();
  if (fromPath) return fromPath;

  // 2. Legacy query param (?lang=tr) — redirect to path-based URL, then return
  const params = new URLSearchParams(window.location.search);
  const qLang  = params.get('lang');
  if (qLang && SUPPORTED.includes(qLang)) {
    if (qLang !== 'en') {
      // Redirect: remove query param, add path prefix, preserve hash
      const newPath = buildLangPath(qLang, window.location.pathname);
      params.delete('lang');
      const qs   = params.toString() ? '?' + params.toString() : '';
      window.location.replace(newPath + qs + window.location.hash);
      return qLang; // won't be reached (redirect), but keeps TS happy
    }
    // ?lang=en — just clean up the param silently
    try {
      const u = new URL(window.location.href);
      u.searchParams.delete('lang');
      history.replaceState(null, '', u.toString());
    } catch (_) {}
  }

  // 3. localStorage (persists across sessions)
  try {
    const saved = localStorage.getItem('yt_lang');
    if (saved && SUPPORTED.includes(saved)) return saved;
  } catch (_) {}

  // 4. Fallback
  return 'en';
}

let currentLang = detectLanguage();
window.currentLang = currentLang;

// ─────────────────────────────────────────
// Translation helper
// ─────────────────────────────────────────

export function t(key) {
  return (TRANSLATIONS[currentLang]?.[key])
      || (TRANSLATIONS.en?.[key])
      || key;
}

// ─────────────────────────────────────────
// Apply translations to DOM
// ─────────────────────────────────────────

function applyTranslations(lang) {
  const dict = TRANSLATIONS[lang] || TRANSLATIONS.en;

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    const val = dict[key] ?? TRANSLATIONS.en[key];
    if (val === undefined) return;
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      if (el.placeholder !== val) el.placeholder = val;
    } else {
      // Skip innerHTML write if content is already correct.
      // This prevents spurious LCP re-measurement when English text
      // is already pre-rendered in the HTML (no DOM mutation needed).
      if (el.innerHTML.trim() !== val.trim()) {
        el.innerHTML = val;
      }
    }
  });

  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.dataset.i18nPlaceholder;
    const val = dict[key] ?? TRANSLATIONS.en[key];
    if (val !== undefined) el.placeholder = val;
  });

  const titleEl = document.querySelector('title[data-titlekey]');
  if (titleEl) {
    const key = titleEl.dataset.titlekey;
    const val = dict[key] ?? TRANSLATIONS.en[key];
    if (val) document.title = val + ' — YouthTICK';
  }
}

// ─────────────────────────────────────────
// setLanguage — public API
// ─────────────────────────────────────────

export function setLanguage(lang) {
  if (!TRANSLATIONS[lang]) return;
  currentLang = lang;
  window.currentLang = lang;

  // Persist to localStorage
  try { localStorage.setItem('yt_lang', lang); } catch (_) {}

  // Update URL path prefix (keeps page reload-free)
  try {
    const newPath = buildLangPath(lang, window.location.pathname);
    // Also strip legacy ?lang= param from query string
    const url = new URL(window.location.href);
    url.searchParams.delete('lang');
    history.replaceState(null, '', newPath + (url.search || '') + url.hash);
  } catch (_) {}

  // Apply translations
  applyTranslations(lang);

  // Update <html lang="..">
  document.documentElement.lang = lang;

  // Update lang-switcher active state
  document.querySelectorAll('[data-lang]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });

  // Refresh hreflang + canonical to match new language
  injectHreflang();

  window.dispatchEvent(new Event('languageChanged'));
}

// ─────────────────────────────────────────
// hreflang injection
// ─────────────────────────────────────────

export function injectHreflang() {
  const cleanPath = stripLangPrefix(window.location.pathname);
  const origin    = window.location.origin;

  // Remove any existing hreflang tags injected by previous calls
  document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(el => el.remove());

  SUPPORTED.forEach(lng => {
    const link = document.createElement('link');
    link.rel      = 'alternate';
    link.hreflang = lng;
    link.href     = origin + buildLangPath(lng, cleanPath);
    document.head.appendChild(link);
  });

  const def = document.createElement('link');
  def.rel      = 'alternate';
  def.hreflang = 'x-default';
  def.href     = origin + cleanPath; // English (no prefix) is default
  document.head.appendChild(def);

  // Update the page's <link rel="canonical"> to reflect the current language URL.
  // Non-English pages are self-canonical (/tr/blog.html); English is the root path.
  const existingCanonical = document.querySelector('link[rel="canonical"]');
  const canonicalHref = origin + buildLangPath(currentLang, cleanPath);
  if (existingCanonical) {
    existingCanonical.href = canonicalHref;
  } else {
    const c = document.createElement('link');
    c.rel  = 'canonical';
    c.href = canonicalHref;
    document.head.appendChild(c);
  }
}

// ─────────────────────────────────────────
// initI18n — called by app.js
// ─────────────────────────────────────────

export function initI18n() {
  setLanguage(currentLang);
  injectHreflang();
}
