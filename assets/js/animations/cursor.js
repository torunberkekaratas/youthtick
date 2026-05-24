export function initCursor() {
  if (window.matchMedia('(pointer: coarse)').matches) return;

  if (!document.getElementById('cursor-dot')) {
    const dot = document.createElement('div');
    dot.id = 'cursor-dot';
    dot.setAttribute('aria-hidden', 'true');
    document.body.appendChild(dot);
  }
  if (!document.getElementById('cursor-ring')) {
    const ring = document.createElement('div');
    ring.id = 'cursor-ring';
    ring.setAttribute('aria-hidden', 'true');
    document.body.appendChild(ring);
  }

  const dot  = document.getElementById('cursor-dot');
  const ring = document.getElementById('cursor-ring');

  document.body.classList.add('cursor-ready');
  let mx = -120, my = -120, rx = -120, ry = -120;
  let rafId = null;
  const lerp = (a, b, t) => a + (b - a) * t;

  const tick = () => {
    const dx = mx - rx, dy = my - ry;
    if (Math.abs(dx) < 0.5 && Math.abs(dy) < 0.5) {
      rx = mx; ry = my;
      ring.style.transform = 'translate(' + (rx - 20) + 'px,' + (ry - 20) + 'px)';
      rafId = null;
      return;
    }
    rx = lerp(rx, mx, 0.115);
    ry = lerp(ry, my, 0.115);
    dot.style.transform  = 'translate(' + (mx - 4) + 'px,' + (my - 4) + 'px)';
    ring.style.transform = 'translate(' + (rx - 20) + 'px,' + (ry - 20) + 'px)';
    rafId = requestAnimationFrame(tick);
  };

  window.addEventListener('mousemove', function (e) {
    mx = e.clientX; my = e.clientY;
    dot.style.transform = 'translate(' + (mx - 4) + 'px,' + (my - 4) + 'px)';
    if (!rafId) rafId = requestAnimationFrame(tick);
  }, { passive: true });

  const HOVER = 'a,button,' +
    '.focus-card,.blog-card,.blog-card-home,.project-card-home,' +
    '.project-card,.partner-card,.vol-opp-card,.sdg-card,' +
    '.report-card,.mvv-card,.team-card,.contact-form-card,' +
    '.network-country,[data-cursor]';
  
  document.addEventListener('mouseover', function (e) {
    if (e.target.closest(HOVER)) { dot.classList.add('hovering'); ring.classList.add('hovering'); }
  });
  document.addEventListener('mouseout', function (e) {
    if (e.target.closest(HOVER)) { dot.classList.remove('hovering'); ring.classList.remove('hovering'); }
  });
  document.addEventListener('mouseleave', function () {
    dot.style.opacity = '0'; ring.style.opacity = '0';
  });
  document.addEventListener('mouseenter', function () {
    dot.style.opacity = '1'; ring.style.opacity = '1';
  });
}
