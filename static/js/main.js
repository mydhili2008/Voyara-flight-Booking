(() => {
  const menuButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');
  if (menuButton && nav) {
    menuButton.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') === 'true';
      menuButton.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
      document.body.classList.toggle('menu-open', !open);
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      menuButton.setAttribute('aria-expanded', 'false');
      nav.classList.remove('is-open');
      document.body.classList.remove('menu-open');
    }));
  }

  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -35px 0px' });
    revealEls.forEach(el => revealObserver.observe(el));
  } else revealEls.forEach(el => el.classList.add('is-visible'));

  const hero = document.querySelector('.hero');
  const heroVideo = document.querySelector('.hero-video');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (hero && !reducedMotion) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const y = Math.min(window.scrollY, window.innerHeight);
          hero.style.setProperty('--scroll-shift', `${y * 0.22}px`);
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
    hero.addEventListener('pointermove', event => {
      const rect = hero.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      hero.style.setProperty('--pointer-x', `${x * 12}px`);
      hero.style.setProperty('--pointer-y', `${y * 10}px`);
    });
  }
  if (heroVideo) {
    const playPromise = heroVideo.play();
    if (playPromise && typeof playPromise.catch === 'function') {
      playPromise.catch(() => heroVideo.classList.add('video-unavailable'));
    }
  }

  const swapButton = document.querySelector('.swap-button');
  if (swapButton) {
    swapButton.addEventListener('click', () => {
      const origin = document.querySelector('#origin');
      const destination = document.querySelector('#destination');
      if (!origin || !destination) return;
      const from = origin.value;
      const to = destination.value;
      const originOptions = Array.from(origin.options).map(o => o.value);
      const destinationOptions = Array.from(destination.options).map(o => o.value);
      if (destinationOptions.includes(from)) destination.value = from;
      if (originOptions.includes(to) && to) origin.value = to;
      swapButton.classList.remove('swap-pulse');
      void swapButton.offsetWidth;
      swapButton.classList.add('swap-pulse');
    });
  }

  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', event => {
      const dateInput = form.querySelector('input[type="date"]');
      if (dateInput && dateInput.value && dateInput.min && dateInput.value < dateInput.min) {
        event.preventDefault();
        dateInput.setCustomValidity('Choose today or a future date.');
        dateInput.reportValidity();
      } else if (dateInput) dateInput.setCustomValidity('');
    });
  });
})();
