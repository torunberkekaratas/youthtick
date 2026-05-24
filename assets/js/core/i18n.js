import en from '../locales/en.js';
import tr from '../locales/tr.js';
import de from '../locales/de.js';

const TRANSLATIONS = { en, tr, de };

function detectLanguage() {
  // 1. Check URL parameter
  const urlParams = new URLSearchParams(window.location.search);
  const langParam = urlParams.get('lang');
  if (langParam && ['en', 'tr', 'de'].includes(langParam)) return langParam;

  // 2. Check localStorage
  try {
    const saved = localStorage.getItem('yt_lang');
    if (saved && ['en', 'tr', 'de'].includes(saved)) return saved;
  } catch (e) {}

  // 3. Fallback to English
  return 'en';
}

let currentLang = detectLanguage();
window.currentLang = currentLang;

export function t(key) {
  return (TRANSLATIONS[currentLang] && TRANSLATIONS[currentLang][key])
      || (TRANSLATIONS.en && TRANSLATIONS.en[key])
      || key;
}

export function setLanguage(lang) {
  if (!TRANSLATIONS[lang]) return;
  currentLang = lang;
  window.currentLang = lang;

  try { localStorage.setItem('yt_lang', lang); } catch (e) {}

  try {
    const url = new URL(window.location.href);
    url.searchParams.set('lang', lang);
    history.replaceState(null, '', url.toString());
  } catch (e) {}

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    const val = TRANSLATIONS[lang][key] || TRANSLATIONS.en[key];
    if (val === undefined) return;
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      el.placeholder = val;
    } else {
      el.innerHTML = val;
    }
  });

  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.dataset.i18nPlaceholder;
    const val = TRANSLATIONS[lang][key] || TRANSLATIONS.en[key];
    if (val !== undefined) el.placeholder = val;
  });

  const titleEl = document.querySelector('title[data-titlekey]');
  if (titleEl) {
    const titleKey = titleEl.dataset.titlekey;
    const val = (TRANSLATIONS[lang][titleKey] || TRANSLATIONS.en[titleKey]);
    if (val) document.title = val + ' — YouthTICK';
  }

  document.documentElement.lang = lang;

  document.querySelectorAll('[data-lang]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });

  window.dispatchEvent(new Event('languageChanged'));
}

export function injectHreflang() {
  const base = window.location.href.split('?')[0];
  ['en', 'tr', 'de'].forEach(lang => {
    const link = document.createElement('link');
    link.rel = 'alternate';
    link.hreflang = lang;
    link.href = base + '?lang=' + lang;
    document.head.appendChild(link);
  });
  const def = document.createElement('link');
  def.rel = 'alternate';
  def.hreflang = 'x-default';
  def.href = base + '?lang=en';
  document.head.appendChild(def);
}

export function initI18n() {
  setLanguage(currentLang);
  injectHreflang();
}
