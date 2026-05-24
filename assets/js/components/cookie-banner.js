import { applyAnalyticsIntegrations } from '../core/content-bridge.js';

export function initCookieBanner() {
  const KEY = 'ytck_consent';
  if (localStorage.getItem(KEY)) return;

  const banner = document.createElement('div');
  banner.id = 'cookie-banner';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', 'Cookie consent');
  banner.innerHTML = `
    <div class="cookie-inner">
      <div class="cookie-text">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true" style="flex-shrink:0;margin-top:2px;color:var(--gold)"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8zm-1-5h2v2h-2zm0-8h2v6h-2z"/></svg>
        <p data-i18n="cookie.text">We use essential cookies to keep the site running, and optional analytics to understand how visitors find us. No personal data is sold or shared.</p>
      </div>
      <div class="cookie-actions">
        <a href="privacy.html" class="cookie-policy-link" data-i18n="cookie.link">Cookie Policy</a>
        <button class="cookie-btn cookie-btn-secondary" id="cookie-essential" data-i18n="cookie.essential">Essential Only</button>
        <button class="cookie-btn cookie-btn-primary" id="cookie-accept" data-i18n="cookie.accept">Accept All</button>
      </div>
    </div>
  `;
  document.body.appendChild(banner);

  setTimeout(function () { banner.classList.add('visible'); }, 1200);

  function dismiss(value) {
    localStorage.setItem(KEY, value);
    banner.classList.remove('visible');
    // If user just accepted all, activate analytics immediately (no page reload needed)
    if (value === 'all') applyAnalyticsIntegrations();
    setTimeout(function () { banner.remove(); }, 400);
  }

  document.getElementById('cookie-essential').addEventListener('click', () => dismiss('essential'));
  document.getElementById('cookie-accept').addEventListener('click', () => dismiss('all'));
}
