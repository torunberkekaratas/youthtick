import { t, setLanguage } from './i18n.js';
// We need to mutate TRANSLATIONS or pass a callback.
// Since i18n.js encapsulated TRANSLATIONS, let's expose an `applyOverrides` function from i18n.js instead.
// For now, I will modify i18n.js slightly to accept overrides.

const KEYS = {
  content: 'yt-admin-content',
  design:  'yt-admin-design',
  blog:    'yt-admin-blog',
  integrations: 'yt-admin-integrations',
};

// ─────────────────────────────────────────
// 2. DESIGN TOKEN OVERRIDES
// ─────────────────────────────────────────
function applyDesignOverrides() {
  try {
    const raw = localStorage.getItem(KEYS.design);
    if (!raw) return;
    const design = JSON.parse(raw);
    if (!design || typeof design !== 'object') return;

    const vars = [];
    const COLOR_MAP = {
      'c-blue-vivid':  '--blue-vivid',
      'c-blue-dark':   '--blue-dark',
      'c-blue-mid':    '--blue-mid',
      'c-navy':        '--navy',
      'c-navy-deep':   '--navy-deep',
      'c-cream':       '--cream',
      'c-ink':         '--ink',
      'c-accent-gold': '--gold',
      'c-surface':     '--bg-card',
    };

    if (design.colors && typeof design.colors === 'object') {
      Object.entries(design.colors).forEach(([id, val]) => {
        const prop = COLOR_MAP[id];
        if (prop && val) vars.push(`${prop}: ${val};`);
      });
    }

    if (design.fontPrimary) vars.push(`--font-primary: ${design.fontPrimary};`);
    if (design.fontSize)    vars.push(`--font-size-base: ${design.fontSize}px;`);
    if (design.lineHeight)  vars.push(`--line-height: ${design.lineHeight};`);
    if (design.radiusCard)  vars.push(`--radius-card: ${design.radiusCard}px;`);
    if (design.radiusBtn)   vars.push(`--radius-btn: ${design.radiusBtn}px;`);
    if (design.sectionPad)  vars.push(`--section-pad: ${design.sectionPad}px;`);
    if (design.maxWidth)    vars.push(`--max-w: ${design.maxWidth}px;`);

    if (vars.length) {
      const varBlock = document.createElement('style');
      varBlock.id = 'yt-design-tokens';
      varBlock.textContent = `:root { ${vars.join(' ')} }`;
      (document.head || document.documentElement).appendChild(varBlock);
    }

    if (design.fontPrimary) {
      document.documentElement.style.setProperty('--font-primary', design.fontPrimary);
      if (document.body) document.body.style.fontFamily = design.fontPrimary;
    }

    if (design['h-heading-size']) {
      const heroTitle = document.querySelector('.hero-title');
      if (heroTitle) heroTitle.style.fontSize = design['h-heading-size'] + 'px';
    }

    if (design['n-style']) {
      const nav = document.querySelector('.nav');
      if (nav) {
        nav.dataset.style = design['n-style'];
        if (design['n-style'] === 'solid') {
          nav.style.setProperty('--nav-initial-bg', 'rgba(255,255,255,1)');
        } else if (design['n-style'] === 'dark') {
          nav.style.setProperty('--nav-initial-bg', 'rgba(10,24,40,0.98)');
          nav.style.color = 'white';
        } else if (design['n-style'] === 'glass') {
          nav.style.setProperty('--nav-initial-bg', 'rgba(255,255,255,0.08)');
          nav.style.backdropFilter = 'blur(20px)';
        }
      }
    }

    if (design['m-scroll-anim'] === false) {
      const noAnimStyle = document.createElement('style');
      noAnimStyle.textContent = `
        [data-anim] { opacity: 1 !important; transform: none !important; transition: none !important; }
      `;
      document.head.appendChild(noAnimStyle);
    }

    if (design.customCss && design.customCss.trim()) {
      const customStyle = document.createElement('style');
      customStyle.id = 'yt-custom-css';
      customStyle.textContent = design.customCss;
      (document.head || document.documentElement).appendChild(customStyle);
    }

  } catch (e) {
    console.warn('[ContentBridge] Design override error:', e);
  }
}

// ─────────────────────────────────────────
// GA4 Measurement ID — replace with your real ID from analytics.google.com
// Format: G-XXXXXXXXXX
// ─────────────────────────────────────────
const GA4_ID = window.YT_GA4_ID || 'G-JD1LX1KFJQ';

// ─────────────────────────────────────────
// 3. ANALYTICS INTEGRATIONS
// ─────────────────────────────────────────
// Only loads analytics scripts when the user has explicitly accepted all cookies
// (GDPR: no analytics without consent).
let _analyticsLoaded = false;

export function applyAnalyticsIntegrations() {
  if (_analyticsLoaded) return;                        // run only once
  if (localStorage.getItem('ytck_consent') !== 'all') return; // consent required

  // Direct GA4 via hardcoded ID or window.YT_GA4_ID
  if (GA4_ID && /^G-[A-Z0-9]+$/.test(GA4_ID)) {
    const s1 = document.createElement('script');
    s1.async = true;
    s1.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_ID}`;
    document.head.appendChild(s1);
    const s2 = document.createElement('script');
    s2.textContent = `window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${GA4_ID}');`;
    document.head.appendChild(s2);
    _analyticsLoaded = true;
    return;
  }

  try {
    const raw = localStorage.getItem(KEYS.integrations);
    if (!raw) return;
    const integrations = JSON.parse(raw);

    if (integrations.ga?.enabled && integrations.ga?.id) {
      const gId = integrations.ga.id.trim();
      if (/^G-[A-Z0-9]+$/.test(gId)) {
        const s1 = document.createElement('script');
        s1.async = true;
        s1.src = `https://www.googletagmanager.com/gtag/js?id=${gId}`;
        document.head.appendChild(s1);
        const s2 = document.createElement('script');
        s2.textContent = `window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${gId}');`;
        document.head.appendChild(s2);
        _analyticsLoaded = true;
      }
    }

    if (integrations.plausible?.enabled && integrations.plausible?.domain) {
      const domain = integrations.plausible.domain.trim();
      const s = document.createElement('script');
      s.defer = true;
      s.dataset.domain = domain;
      s.src = 'https://plausible.io/js/plausible.js';
      document.head.appendChild(s);
      _analyticsLoaded = true;
    }

    if (integrations.fathom?.enabled && integrations.fathom?.id) {
      const fId = integrations.fathom.id.trim();
      if (/^[A-Z0-9]+$/.test(fId)) {
        const s = document.createElement('script');
        s.src = 'https://cdn.usefathom.com/script.js';
        s.dataset.site = fId;
        s.defer = true;
        document.head.appendChild(s);
        _analyticsLoaded = true;
      }
    }
  } catch (e) {}
}

// ─────────────────────────────────────────
// 4. BLOG DATA BRIDGE
// ─────────────────────────────────────────
function exposeBlogData() {
  try {
    const raw = localStorage.getItem(KEYS.blog);
    if (!raw) { window.YT_BLOG_POSTS = []; return; }
    const parsed = JSON.parse(raw);
    const posts = Array.isArray(parsed) ? parsed : (parsed && Array.isArray(parsed.posts) ? parsed.posts : []);
    window.YT_BLOG_POSTS = posts
      .filter(p => p.status === 'published')
      .sort((a, b) => new Date(b.publishedAt || b.createdAt) - new Date(a.publishedAt || a.createdAt));
  } catch (e) {
    window.YT_BLOG_POSTS = [];
  }
}

// ─────────────────────────────────────────
// 5. DYNAMIC BLOG PAGE RENDERER
// ─────────────────────────────────────────
function renderPublicBlogPosts() {
  const grid = document.querySelector('.blog-grid, #blog-posts-grid, [data-blog-posts]');
  if (!grid || !window.YT_BLOG_POSTS?.length) return;

  if (grid.children.length > 0 && !grid.dataset.adminPopulate) return;

  const posts = window.YT_BLOG_POSTS.slice(0, parseInt(grid.dataset.limit) || 99);
  const lang = document.documentElement.lang || 'en';

  grid.innerHTML = posts.map(post => {
    const thumb = post.featuredImage
      ? `<div class="blog-card-thumb"><img src="${escHtml(post.featuredImage)}" alt="${escHtml(post.title)}" loading="lazy"/></div>`
      : `<div class="blog-card-thumb blog-card-thumb-placeholder"></div>`;

    const date = post.publishedAt
      ? new Date(post.publishedAt).toLocaleDateString(lang === 'de' ? 'de-DE' : lang === 'tr' ? 'tr-TR' : 'en-GB', { day: 'numeric', month: 'long', year: 'numeric' })
      : '';

    return `
      <article class="blog-card" data-anim="fade-up">
        ${thumb}
        <div class="blog-card-body">
          ${post.category ? `<div class="blog-card-category">${escHtml(post.category)}</div>` : ''}
          <h3 class="blog-card-title">${escHtml(post.title)}</h3>
          ${post.excerpt ? `<p class="blog-card-excerpt">${escHtml(post.excerpt)}</p>` : ''}
          <div class="blog-card-meta">
            ${post.author ? `<span>${escHtml(post.author)}</span>` : ''}
            ${date ? `<span>${date}</span>` : ''}
          </div>
        </div>
      </article>
    `;
  }).join('');
}

function escHtml(str) {
  if (!str) return '';
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function exposeMediaData() {
  try {
    const raw = localStorage.getItem('yt-admin-media');
    if (!raw) { window.YT_MEDIA = []; return; }
    window.YT_MEDIA = JSON.parse(raw) || [];
    window.YT_resolveMedia = function(idOrName) {
      if (!idOrName) return null;
      return window.YT_MEDIA.find(m => m.id === idOrName || m.name === idOrName) || null;
    };
  } catch (e) {
    window.YT_MEDIA = [];
  }
}

export function initContentBridge() {
  applyDesignOverrides();
  applyAnalyticsIntegrations(); // runs only if ytck_consent === 'all'
  exposeBlogData();
  exposeMediaData();
  renderPublicBlogPosts();
}
