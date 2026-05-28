/* ─────────────────────────────────────────────────────────────────
   YouthTICK · home.js — Studio Edition v5
   Scroll Progress · Custom Cursor · 3D Tilt · Parallax · Particles
   ───────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  /* ── 1. SCROLL PROGRESS BAR ─────────────────────────────────── */
  function initScrollProgress() {
    const bar = document.getElementById('scroll-progress');
    if (!bar) return;
    const update = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? window.scrollY / max : 0) + ')';
    };
    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ── 2. CUSTOM CURSOR ───────────────────────────────────────── */
  function initCursor() {
    /* Skip on touch devices */
    if (window.matchMedia('(pointer: coarse)').matches) return;
    const dot  = document.getElementById('cursor-dot');
    const ring = document.getElementById('cursor-ring');
    if (!dot || !ring) return;

    document.body.classList.add('cursor-ready');
    let mx = -120, my = -120, rx = -120, ry = -120;
    const lerp = (a, b, t) => a + (b - a) * t;

    const tick = () => {
      rx = lerp(rx, mx, 0.115);
      ry = lerp(ry, my, 0.115);
      dot.style.transform  = 'translate(' + (mx - 4) + 'px,' + (my - 4) + 'px)';
      ring.style.transform = 'translate(' + (rx - 20) + 'px,' + (ry - 20) + 'px)';
      requestAnimationFrame(tick);
    };
    tick();

    window.addEventListener('mousemove', function (e) {
      mx = e.clientX; my = e.clientY;
    }, { passive: true });

    const HOVER = 'a,button,.focus-card,.blog-card-home,.project-card-home,.network-country,[data-cursor]';
    document.addEventListener('mouseover', function (e) {
      if (e.target.closest(HOVER)) { dot.classList.add('hovering'); ring.classList.add('hovering'); }
    });
    document.addEventListener('mouseout', function (e) {
      if (e.target.closest(HOVER)) { dot.classList.remove('hovering'); ring.classList.remove('hovering'); }
    });

    /* Hide on leave / show on enter window */
    document.addEventListener('mouseleave', function () {
      dot.style.opacity = '0'; ring.style.opacity = '0';
    });
    document.addEventListener('mouseenter', function () {
      dot.style.opacity = '1'; ring.style.opacity = '1';
    });
  }

  /* ── 3. PARALLAX (hero image + bg gradient) ─────────────────── */
  /* Note: initCardTilt / initStatCells / initHeroScrollFade / initHeroBadges
     are now handled globally by components.js for all pages. */
  function initParallax() {
    var img = document.querySelector('.hero-img-wrap');
    var bg  = document.querySelector('.hero-bg');
    if (!img) return;
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      img.style.transform = 'translateY(' + (y * 0.055) + 'px)';
      if (bg) bg.style.transform = 'translateY(' + (y * 0.022) + 'px)';
    }, { passive: true });
  }

  /* ── 5. ANIMATED STAT COUNTERS ──────────────────────────────── */
  function initCounters() {
    var stats = document.getElementById('manifesto-stats');
    if (!stats) return;
    var counters = stats.querySelectorAll('[data-count]');
    if (!counters.length) return;
    var done = false;
    var obs = new IntersectionObserver(function (entries) {
      if (done || !entries[0].isIntersecting) return;
      done = true;
      obs.disconnect();
      counters.forEach(function (el) {
        var target   = parseInt(el.dataset.count, 10);
        var suffix   = el.dataset.suffix || '';
        var duration = 1400;
        var start    = null;
        function step(ts) {
          if (!start) start = ts;
          var progress = Math.min((ts - start) / duration, 1);
          var eased    = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.round(eased * target) + suffix;
          if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.6 });
    obs.observe(stats);
  }

  /* ── 6. MANIFESTO CANVAS PARTICLES ──────────────────────────── */
  function initManifestoParticles() {
    var canvas = document.getElementById('manifesto-canvas');
    if (!canvas) return;
    var ctx     = canvas.getContext('2d');
    var section = canvas.closest('.manifesto-section');
    if (!section) return;

    function resize() {
      canvas.width  = section.offsetWidth;
      canvas.height = section.offsetHeight;
    }
    // Defer initial layout read to rAF — prevents forced reflow on DOMContentLoaded
    requestAnimationFrame(resize);
    window.addEventListener('resize', resize, { passive: true });

    /* Gentle floating specks */
    var N = 36;
    var pts = [];
    for (var i = 0; i < N; i++) {
      pts.push({
        x:  Math.random() * canvas.width,
        y:  Math.random() * canvas.height,
        r:  Math.random() * 1.8 + 0.4,
        vx: (Math.random() - 0.5) * 0.18,
        vy: (Math.random() - 0.5) * 0.12,
        a:  Math.random() * 0.5 + 0.12,
        g:  Math.random() < 0.4 ? 1 : 0 /* gold vs blue */
      });
    }

    var active = false;
    var obsP = new IntersectionObserver(function (entries) {
      active = entries[0].isIntersecting;
    }, { threshold: 0.05 });
    obsP.observe(section);

    function draw() {
      requestAnimationFrame(draw);
      if (!active) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (var j = 0; j < pts.length; j++) {
        var p = pts[j];
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0)            p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0)            p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = p.g
          ? 'rgba(184,138,40,' + (p.a * 0.40) + ')'
          : 'rgba(37,99,235,' + (p.a * 0.22) + ')';
        ctx.fill();
      }
    }
    draw();
  }

  /* ── INIT ────────────────────────────────────────────────────── */
  /* cardTilt / statCells / heroScrollFade / heroBadges / cursor /
     scrollProgress / pageFade are all handled by components.js globally. */
  document.addEventListener('DOMContentLoaded', function () {
    /* Home-only shared components */
    if (typeof renderFooter  === 'function') renderFooter();
    if (typeof renderMarquee === 'function') renderMarquee('marquee-target');

    /* Home-specific interactions only */
    initParallax();
    initManifestoParticles();
    initCounters();

    /* Lucide (second pass — components.js fires first) */
    setTimeout(function () { if (window.lucide) lucide.createIcons(); }, 250);
  });

})();
