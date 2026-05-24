export function initCardTilt() {
  if (window.matchMedia('(pointer: coarse)').matches) return;

  const CARDS = [
    '.focus-card', '.blog-card-home', '.project-card-home',
    '.project-card', '.blog-card',
    '.partner-card', '.vol-opp-card',
    '.sdg-card', '.report-card',
    '.mvv-card', '.team-card'
  ].join(',');

  const SELECTOR = CARDS;
  let activeCard = null;
  let raf = null;

  document.addEventListener('mousemove', function (e) {
    const card = e.target.closest(SELECTOR);
    if (!card) return;
    if (raf) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(function () {
      const r  = card.getBoundingClientRect();
      const nx = ((e.clientX - r.left) / r.width  - 0.5) * 2;
      const ny = ((e.clientY - r.top)  / r.height - 0.5) * 2;
      card.style.transform =
        'perspective(900px) rotateX(' + (-ny * 5.5) + 'deg) rotateY(' + (nx * 5.5) + 'deg) translateY(-6px) scale(1.015)';
      activeCard = card;
    });
  });

  document.addEventListener('mouseover', function (e) {
    if (!activeCard) return;
    if (!activeCard.contains(e.target)) {
      if (raf) cancelAnimationFrame(raf);
      activeCard.style.transition = 'transform 0.60s cubic-bezier(0.16,1,0.3,1), box-shadow 0.42s ease';
      activeCard.style.transform = '';
      const card = activeCard;
      setTimeout(function () { card.style.transition = ''; }, 650);
      activeCard = null;
    }
  });
}
