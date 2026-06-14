/* =========================================================
   Toulouse FC replica — interactions
   ========================================================= */

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- Carousels: arrows + autoplay + pause on hover ---------- */
document.querySelectorAll('[data-carousel]').forEach((carousel) => {
  const track = carousel.querySelector('.carousel-track');
  const prev = carousel.querySelector('[data-prev]');
  const next = carousel.querySelector('[data-next]');

  const step = () => {
    const card = track.querySelector('.card, .card-hospitality');
    const gap = parseFloat(getComputedStyle(track).gap) || 20;
    return (card ? card.getBoundingClientRect().width : 280) + gap;
  };

  const scrollByCards = (dir, count = 2) => {
    track.scrollBy({ left: dir * step() * count, behavior: 'smooth' });
  };

  prev && prev.addEventListener('click', () => scrollByCards(-1));
  next && next.addEventListener('click', () => scrollByCards(1));

  const progress = carousel.querySelector('.carousel-progress span');

  // arrows + progress bar at the edges
  const updateUI = () => {
    const max = track.scrollWidth - track.clientWidth;
    if (prev) prev.style.opacity = track.scrollLeft <= 2 ? '.35' : '1';
    if (next) next.style.opacity = track.scrollLeft >= max - 2 ? '.35' : '1';
    if (progress && max > 0) {
      const ratio = track.scrollLeft / max;          // 0..1
      const visible = track.clientWidth / track.scrollWidth; // fraction shown
      const w = Math.max(0.12, visible);
      progress.style.width = (w * 100) + '%';
      progress.style.marginLeft = (ratio * (1 - w) * 100) + '%';
    }
  };
  track.addEventListener('scroll', updateUI, { passive: true });
  window.addEventListener('resize', updateUI);
  updateUI();

  // autoplay
  if (!reduceMotion) {
    let timer;
    const start = () => {
      timer = setInterval(() => {
        const max = track.scrollWidth - track.clientWidth - 2;
        if (track.scrollLeft >= max) {
          track.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
          scrollByCards(1, 1);
        }
      }, 4500);
    };
    const stop = () => clearInterval(timer);
    start();
    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
    carousel.addEventListener('focusin', stop);
    carousel.addEventListener('touchstart', stop, { passive: true });
  }
});

/* ---------- Team tabs ---------- */
document.querySelectorAll('.team-tabs .tab').forEach((tab) => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.team-tabs .tab').forEach((t) => t.classList.remove('active'));
    tab.classList.add('active');
  });
});

/* ---------- Scroll-reveal ---------- */
const revealTargets = document.querySelectorAll(
  '.section-head, .section-title-big, .banner-wide, .rdv-block, .equipes-card, ' +
  '.standings-grid, .stats-block, .duo-grid > *, .trio-grid > *, ' +
  '.agissons-text, .center-cta, .occitanie-content, .coeur-banner, ' +
  '.news-banner, .partners-panel'
);
revealTargets.forEach((el) => el.setAttribute('data-reveal', ''));

if ('IntersectionObserver' in window && !reduceMotion) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  revealTargets.forEach((el) => io.observe(el));
} else {
  revealTargets.forEach((el) => el.classList.add('is-visible'));
}

/* ---------- Dock scrollspy ---------- */
const dockItems = [...document.querySelectorAll('.dock-item')];
const spyMap = dockItems
  .map((a) => {
    const href = a.getAttribute('href') || '';
    return href.startsWith('#') && href.length > 1
      ? { item: a, section: document.querySelector(href) }
      : null;
  })
  .filter((x) => x && x.section);

if (spyMap.length && 'IntersectionObserver' in window) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const match = spyMap.find((s) => s.section === entry.target);
        if (match) {
          dockItems.forEach((d) => d.classList.remove('active'));
          match.item.classList.add('active');
        }
      }
    });
  }, { rootMargin: '-45% 0px -45% 0px' });
  spyMap.forEach((s) => spy.observe(s.section));
}

/* set Home active when near the very top */
window.addEventListener('scroll', () => {
  if (window.scrollY < 120) {
    dockItems.forEach((d) => d.classList.remove('active'));
    dockItems[0] && dockItems[0].classList.add('active');
  }
}, { passive: true });

/* ---------- Daha Fazla overlay ---------- */
(function () {
  const overlay  = document.getElementById('moreOverlay');
  const closeBtn = document.getElementById('moreClose');
  const trigger  = document.getElementById('moreTrigger');
  if (!overlay || !trigger) return;

  const open = (e) => {
    overlay.classList.add('is-open');
    overlay.removeAttribute('aria-hidden');
    document.body.style.overflow = 'hidden';
    closeBtn && closeBtn.focus();
  };
  const close = () => {
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    trigger.focus();
  };

  trigger.addEventListener('click', open);
  closeBtn && closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', (e) => { if (e.target === overlay) close(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && overlay.classList.contains('is-open')) close(); });
})();

/* ---------- Pre-fill volunteer application form role from role cards ---------- */
document.querySelectorAll('a[data-role][href="#basvuru-formu"]').forEach((link) => {
  link.addEventListener('click', () => {
    const select = document.getElementById('vf-role');
    if (!select) return;
    const role = link.getAttribute('data-role');
    const match = [...select.options].find((opt) => opt.value === role);
    if (match) select.value = role;
  });
});

/* ---------- Smooth anchor scrolling that accounts for the dock ---------- */
document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener('click', (e) => {
    const id = link.getAttribute('href');
    if (id.length <= 1) return;
    const target = document.querySelector(id);
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
  });
});
