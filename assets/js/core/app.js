import { initI18n, setLanguage } from './i18n.js';
import { initContentBridge } from './content-bridge.js';
import { renderNav, closeMobileMenu } from '../components/navigation.js';
import { renderFooter } from '../components/footer.js';
import { initCookieBanner } from '../components/cookie-banner.js';
import { initCursor } from '../animations/cursor.js';
import { initCardTilt } from '../animations/card-tilt.js';
import { tickScrollProgress, initScrollReveal } from '../animations/scroll.js';

// Expose necessary functions to the global scope so inline onclick handlers continue working
window.ytSetLang  = setLanguage;
window.closeMobileMenu = closeMobileMenu;
// Legacy shim compatibility
window.setLanguage = setLanguage;
window.renderNav   = () => {};  // no-op (already rendered by module)
window.renderFooter = () => {}; // no-op (already rendered by module)

function initLucide() {
  if (window.lucide) {
    window.lucide.createIcons();
  } else {
    // Lucide loads with defer — wait for it
    window.addEventListener('load', () => {
      if (window.lucide) window.lucide.createIcons();
    });
  }
}

function initApp() {
    // 1. Render UI Components (nav + footer inject themselves into <body>)
    renderNav();
    renderFooter();
    initCookieBanner();

    // 2. Initialize Translations (translates all data-i18n elements)
    initI18n();
    initContentBridge();

    // 3. Animations & Utilities
    initCursor();
    initCardTilt();
    tickScrollProgress();
    initScrollReveal();

    // 4. Lucide icons
    initLucide();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}
