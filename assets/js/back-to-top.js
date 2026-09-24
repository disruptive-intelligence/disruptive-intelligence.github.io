(() => {
  const button = document.querySelector('.back-to-top');
  if (!button) return;

  const updateVisibility = () => {
    button.hidden = window.scrollY < 400;
  };

  window.addEventListener('scroll', updateVisibility, { passive: true });
  updateVisibility();

  button.addEventListener('click', () => {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
  });
})();
