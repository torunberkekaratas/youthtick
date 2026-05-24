/* ── Scroll Progress Bar ─────────────────────────────────────────── */
export function initScrollProgress() {
  if (document.getElementById('scroll-progress')) return;
  const bar = document.createElement('div');
  bar.id = 'scroll-progress';
  bar.setAttribute('aria-hidden', 'true');
  document.body.insertBefore(bar, document.body.firstChild);
}

export function tickScrollProgress() {
  initScrollProgress();
  const bar = document.getElementById('scroll-progress');
  if (!bar) return;

  let ticking = false;
  const upd = () => {
    const s = document.documentElement;
    const pct = s.scrollTop / (s.scrollHeight - s.clientHeight) || 0;
    bar.style.transform = 'scaleX(' + pct + ')';
    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(upd); ticking = true; }
  }, { passive: true });

  upd();
}

/* ── Scroll-Reveal: [data-anim] → adds .visible when in viewport ── */
export function initScrollReveal() {
  const els = document.querySelectorAll('[data-anim]');
  if (!els.length) return;

  // Respect prefers-reduced-motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach(el => el.classList.add('visible'));
    return;
  }

  const obs = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target); // fire once
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  els.forEach(el => obs.observe(el));
}

/* ── anim-fade-up: CSS animation triggered on .anim-fade-up class ─ */
export function initFadeUpObserver() {
  const els = document.querySelectorAll('.anim-fade-up, .anim-fade-in, .anim-scale');
  if (!els.length) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const obs = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Already animated via CSS animation-delay — just ensure visibility
          entry.target.style.opacity = '';
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.08 }
  );

  els.forEach(el => obs.observe(el));
}
