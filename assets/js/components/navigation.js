export function renderNav() {
  // Inject GSC verification meta tag (HTML-file method already deployed;
  // meta tag is a belt-and-suspenders fallback)
  if (!document.querySelector('meta[name="google-site-verification"]')) {
    const gsv = document.createElement('meta');
    gsv.name    = 'google-site-verification';
    gsv.content = '4b845199cb82da28';
    document.head.appendChild(gsv);
  }

  // Strip /tr/ or /de/ prefix before taking the filename for active-state detection
  const strippedPath = window.location.pathname.replace(/^\/(tr|de)(\/|$)/, '/');
  const currentPath  = strippedPath.split('/').pop() || 'index.html';
  const activePage   = currentPath === '' ? 'index.html' : currentPath;

  const links = [
    { href: 'about.html', key: 'nav.about' },
    { href: 'focus.html', key: 'nav.programs' },
    { href: 'projects.html', key: 'nav.projects' },
    { href: 'opportunities.html', key: 'nav.opportunities' },
    { href: 'partnership.html', key: 'nav.partnership' },
    { href: 'team.html', key: 'nav.team' },
    { href: 'blog.html', key: 'nav.blog' },
    { href: 'contact.html', key: 'nav.contact' }
  ];

  const navHTML = `
  <nav class="nav" id="main-nav" role="navigation" aria-label="Main navigation">
    <div class="container">
      <div class="nav-inner">

        <a href="index.html" class="nav-logo" aria-label="YouthTICK Home">
          <img src="logo.svg" alt="YouthTICK Logo" style="height: 44px; width: auto; display: block;" />
        </a>

        <ul class="nav-links" role="list">
          ${links.map(l => `
            <li>
              <a href="${l.href}"
                 class="nav-link${activePage === l.href ? ' active' : ''}"
                 data-i18n="${l.key}"
                 id="nav-link-${l.href.replace('.html','')}">
                ${l.key}
              </a>
            </li>
          `).join('')}
        </ul>

        <div class="nav-right">
          <div class="lang-switcher" data-notranslate role="group" aria-label="Language selection">
            <button class="lang-btn" data-lang="en" onclick="ytSetLang('en')" id="lang-en">EN</button>
            <button class="lang-btn" data-lang="tr" onclick="ytSetLang('tr')" id="lang-tr">TR</button>
            <button class="lang-btn" data-lang="de" onclick="ytSetLang('de')" id="lang-de">DE</button>
          </div>
          <a href="volunteer.html" class="btn btn-primary btn-sm nav-join-btn" id="nav-cta-volunteer" data-i18n="nav.join">Join Us</a>
        </div>

        <button class="nav-hamburger" id="nav-hamburger" aria-label="Toggle mobile menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>

  <div class="mobile-menu" id="mobile-menu" role="dialog" aria-label="Mobile navigation">
    ${links.map(l => `<a href="${l.href}" class="mobile-nav-link" data-i18n="${l.key}">${l.key}</a>`).join('')}
    <div class="mobile-lang" data-notranslate>
      <button class="mobile-lang-btn" data-lang="en" onclick="ytSetLang('en');closeMobileMenu()">🇬🇧 EN</button>
      <button class="mobile-lang-btn" data-lang="tr" onclick="ytSetLang('tr');closeMobileMenu()">🇹🇷 TR</button>
      <button class="mobile-lang-btn" data-lang="de" onclick="ytSetLang('de');closeMobileMenu()">🇩🇪 DE</button>
    </div>
    <a href="volunteer.html" class="btn btn-primary" style="margin-top:10px;width:100%;justify-content:center;" data-i18n="nav.join">Join Us</a>
  </div>
  `;

  document.body.insertAdjacentHTML('afterbegin', navHTML);

  const nav = document.getElementById('main-nav');
  const onScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 24);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const hamburger = document.getElementById('nav-hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  hamburger.addEventListener('click', () => {
    const open = mobileMenu.classList.toggle('open');
    hamburger.classList.toggle('open', open);
    hamburger.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
}

export function closeMobileMenu() {
  const mobileMenu = document.getElementById('mobile-menu');
  const hamburger = document.getElementById('nav-hamburger');
  if (mobileMenu && mobileMenu.classList.contains('open')) {
    mobileMenu.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
}
