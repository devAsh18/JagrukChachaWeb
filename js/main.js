// Jagruk Chacha — shared site behavior
// Handles: theme toggle, language toggle, mobile menu, scroll animations, smooth scroll, contact form, active nav highlighting

(function () {
    'use strict';

    const html = document.documentElement;
    const isHomePage = !!document.getElementById('home');

    // ---------- Active nav highlighting via IntersectionObserver ----------
    // Respect prefers-reduced-motion: when set, skip the observer entirely and mark
    // only the home link (already set in HTML) — no animations, no re-paints.
    if (isHomePage && 'IntersectionObserver' in window) {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');

        if (sections.length && navLinks.length) {
            const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

            if (prefersReducedMotion) {
                // First-section-in-viewport wins; observed once. No continuous updates.
                const setCurrent = (id) => {
                    navLinks.forEach(link => {
                        const linkId = link.getAttribute('href').slice(1);
                        if (linkId === id) {
                            link.setAttribute('aria-current', 'location');
                        } else {
                            link.removeAttribute('aria-current');
                        }
                    });
                };
                const reducedObserver = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            setCurrent(entry.target.getAttribute('id'));
                        }
                    });
                }, { threshold: 0.5 });
                sections.forEach(section => reducedObserver.observe(section));
            } else {
                const navObserver = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            const id = entry.target.getAttribute('id');
                            navLinks.forEach(link => {
                                const linkId = link.getAttribute('href').slice(1);
                                if (linkId === id) {
                                    link.setAttribute('aria-current', 'location');
                                } else {
                                    link.removeAttribute('aria-current');
                                }
                            });
                        }
                    });
                }, { threshold: 0.3, rootMargin: '-100px 0px -60% 0px' });

                sections.forEach(section => navObserver.observe(section));
            }
        }
    }

    // ---------- Theme ----------
    const themeToggleInput = document.getElementById('themeToggleInput') || document.getElementById('themeToggle');
    const themeToggleMobile = document.getElementById('themeToggleInputMobile');
    const savedTheme = localStorage.getItem('theme') || 'dark';
    html.setAttribute('data-theme', savedTheme);
    if (themeToggleInput) {
        // index.html uses checkbox.checked = (light) for the toggle;
        // legal pages use checked = (dark). Normalize both to match the saved theme.
        if (themeToggleInput.id === 'themeToggleInput') {
            themeToggleInput.checked = savedTheme === 'light';
        } else {
            themeToggleInput.checked = savedTheme === 'dark';
        }
    }
    // Sync mobile theme toggle
    if (themeToggleMobile) {
        themeToggleMobile.checked = savedTheme === 'light';
    }

    function setTheme(newTheme) {
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        // Sync all theme toggles
        const isLight = newTheme === 'light';
        if (themeToggleInput) themeToggleInput.checked = isLight;
        if (themeToggleMobile) themeToggleMobile.checked = isLight;
    }

    if (themeToggleInput) {
        themeToggleInput.addEventListener('change', (e) => {
            let newTheme;
            if (themeToggleInput.id === 'themeToggleInput') {
                newTheme = e.target.checked ? 'light' : 'dark';
            } else {
                newTheme = e.target.checked ? 'dark' : 'light';
            }
            setTheme(newTheme);
        });
    }
    if (themeToggleMobile) {
        themeToggleMobile.addEventListener('change', (e) => {
            const newTheme = e.target.checked ? 'light' : 'dark';
            setTheme(newTheme);
        });
    }

    // ---------- Language ----------
    function updateLangLabels(lang) {
        const enLabel = document.querySelectorAll('.en-label') || document.getElementById('langEn');
        const hiLabel = document.querySelectorAll('.hi-label') || document.getElementById('langHi');
        if (enLabel) {
            if (enLabel.length) {
                enLabel.forEach(el => el.classList.toggle('active', lang === 'en'));
            } else {
                enLabel.classList.toggle('active', lang === 'en');
            }
        }
        if (hiLabel) {
            if (hiLabel.length) {
                hiLabel.forEach(el => el.classList.toggle('active', lang === 'hi'));
            } else {
                hiLabel.classList.toggle('active', lang === 'hi');
            }
        }
    }

    const langToggle = document.getElementById('langToggle');
    const langToggleMobile = document.getElementById('langToggleMobile');
    const savedLang = localStorage.getItem('lang') || 'en';
    html.setAttribute('data-lang', savedLang);
    html.lang = savedLang;
    if (langToggle) langToggle.checked = savedLang === 'hi';
    if (langToggleMobile) langToggleMobile.checked = savedLang === 'hi';
    updateLangLabels(savedLang);

    function setLang(newLang) {
        html.setAttribute('data-lang', newLang);
        html.lang = newLang;
        localStorage.setItem('lang', newLang);
        updateLangLabels(newLang);
        // Sync all lang toggles
        const isHindi = newLang === 'hi';
        if (langToggle) langToggle.checked = isHindi;
        if (langToggleMobile) langToggleMobile.checked = isHindi;
    }

    if (langToggle) {
        langToggle.addEventListener('change', (e) => {
            const newLang = e.target.checked ? 'hi' : 'en';
            setLang(newLang);
        });
    }
    if (langToggleMobile) {
        langToggleMobile.addEventListener('change', (e) => {
            const newLang = e.target.checked ? 'hi' : 'en';
            setLang(newLang);
        });
    }

    // ---------- Mobile menu ----------
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navLinks = document.getElementById('navLinks');
    if (mobileMenuBtn && navLinks) {
        function closeMenu() {
            navLinks.classList.remove('active');
            mobileMenuBtn.setAttribute('aria-expanded', 'false');
            mobileMenuBtn.focus();
        }
        function openMenu() {
            navLinks.classList.add('active');
            mobileMenuBtn.setAttribute('aria-expanded', 'true');
        }
        mobileMenuBtn.addEventListener('click', () => {
            const isOpen = navLinks.classList.contains('active');
            if (isOpen) closeMenu(); else openMenu();
        });
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMenu);
        });
        // Close on ESC
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navLinks.classList.contains('active')) {
                closeMenu();
            }
        });
    }

    // ---------- Contact form (index.html #collabForm, contact.html #contactForm) ----------
    const collabForm = document.getElementById('collabForm') || document.getElementById('contactForm');
    if (collabForm) {
        const submitBtn = document.getElementById('submitBtn');
        const isHindi = () => html.getAttribute('data-lang') === 'hi';

        collabForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const type = document.getElementById('type').value;
            const message = document.getElementById('message').value.trim();
            const subject = `New Contact - Jagruk Chacha: ${type}`;

            const body = isHindi()
                ? `नमस्ते जागरूक चाचा टीम,\n\n${message}\n\n---\nसंपर्क विवरण:\n━━━━━━━━━━━━━━━━━━━━\n👤 नाम: ${name}\n📧 ईमेल: ${email}\n📂 संपर्क का प्रकार: ${type}\n━━━━━━━━━━━━━━━━━━━━\n\nयह संदेश जागरूक चाचा वेबसाइट के collaboration फॉर्म से भेजा गया है।\n\nजागरूक रहो बेटा! 🙏`
                : `Hello Jagruk Chacha Team,\n\n${message}\n\n---\nContact Details:\n━━━━━━━━━━━━━━━━━━━━\n👤 Name: ${name}\n📧 Email: ${email}\n📂 Type: ${type}\n━━━━━━━━━━━━━━━━━━━━\n\nThis message was sent from the Jagruk Chacha website contact form.\n\nJagruk Raho! 🙏`;

            const mailtoLink = `mailto:jagrukchacha@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            window.location.href = mailtoLink;

            if (submitBtn) {
                submitBtn.innerHTML = `
                    <svg viewBox="0 0 24 24" style="fill: currentColor;">
                        <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                    </svg>
                    <span>${isHindi() ? 'ईमेल ऐप खुल रहा है...' : 'Opening email app...'}</span>
                `;
                submitBtn.style.background = 'linear-gradient(135deg, #10b981, #059669)';
                setTimeout(() => {
                    submitBtn.innerHTML = `
                        <svg viewBox="0 0 24 24">
                            <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                        </svg>
                        <span>${isHindi() ? 'ईमेल भेजें' : 'Send Email'}</span>
                    `;
                    submitBtn.style.background = 'var(--gradient-primary)';
                }, 3000);
            }
        });
    }

    // ---------- Scroll animations ----------
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

        document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
    } else {
        document.querySelectorAll('.animate-on-scroll').forEach(el => el.classList.add('visible'));
    }

    // ---------- Smooth scroll for in-page anchors ----------
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#' || href.length < 2) return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ---------- Episode view counts from static JSON ----------
    // Fetches episode-stats.json with a 24h localStorage cache.
    // Update episode-stats.json manually or via a GitHub Actions cron job.
    const STATS_URL = 'assets/episode-stats.json';
    const CACHE_KEY  = 'jc_episode_stats';
    const CACHE_TTL  = 24 * 60 * 60 * 1000; // 24 hours in ms

    function formatViews(n) {
        return n >= 1000
            ? (n / 1000).toFixed(1).replace(/\.0$/, '') + 'K'
            : String(n);
    }

    function getLang() {
        return html.getAttribute('data-lang') || 'en';
    }

    async function loadEpisodeStats() {
        const badges = document.querySelectorAll('[data-episode][data-stat]');
        if (!badges.length) return;

        let stats = null;

        try {
            const cached = localStorage.getItem(CACHE_KEY);
            if (cached) {
                const { data, ts } = JSON.parse(cached);
                if (Date.now() - ts < CACHE_TTL) {
                    stats = data;
                }
            }

            if (!stats) {
                const res = await fetch(STATS_URL);
                if (!res.ok) throw new Error('Failed to fetch stats');
                stats = await res.json();
                localStorage.setItem(CACHE_KEY, JSON.stringify({ data: stats, ts: Date.now() }));
            }
        } catch (_) {
            // Network/server error — keep placeholder text already in HTML
            return;
        }

        const lang = getLang();

        badges.forEach(badge => {
            const epId  = badge.dataset.episode;
            const stat  = badge.dataset.stat;
            const count = badge.querySelector('.episode-views-count');
            if (!count) return;

            const ep = stats?.episodes?.[epId];
            const value = ep?.platforms?.youtube?.[stat] ?? ep?.[stat];
            if (value) {
                const suffix = lang === 'hi' ? ' व्यूज़' : ' views';
                count.textContent = formatViews(value) + suffix;
            }
        });
    }

    loadEpisodeStats();

    // ---------- Skeleton shimmer fallback for images that never load ----------
    // If the image hasn't fired onload within 8 s (e.g. very slow network),
    // remove the shimmer class so the brand-tinted pulse doesn't run forever.
    // CSS also handles this under prefers-reduced-motion.
    (function () {
        var shimmerEls = document.querySelectorAll('.skeleton-shimmer');
        if (!shimmerEls.length) return;
        setTimeout(function () {
            shimmerEls.forEach(function (el) {
                el.classList.remove('skeleton-shimmer');
            });
        }, 8000);
    })();

    // ---------- Video Preview Modal ----------
    const videoModal = document.getElementById('videoModal');
    const heroCardPlay = document.getElementById('heroCardPlay');
    const videoModalClose = document.getElementById('videoModalClose');
    const videoModalBackdrop = document.getElementById('videoModalBackdrop');
    const videoModalIframe = document.getElementById('videoModalIframe');
    const VIDEO_EMBED_BASE = 'https://www.youtube.com/embed/';
    const VIDEO_ID = 'peCfxJ1HdnI';
    let lastFocused = null;
    // Selectors for focusable elements inside the modal — used by the focus trap
    // so keyboard users (WCAG 2.1.2) can't Tab out into the page behind the modal.
    const FOCUSABLE_SELECTOR = [
        'a[href]',
        'button:not([disabled])',
        'iframe',
        'input:not([disabled])',
        'select:not([disabled])',
        'textarea:not([disabled])',
        '[tabindex]:not([tabindex="-1"])'
    ].join(',');

    function getModalFocusable() {
        return Array.from(videoModal.querySelectorAll(FOCUSABLE_SELECTOR))
            .filter(el => !el.hasAttribute('hidden') && el.offsetParent !== null);
    }

    function openVideoModal() {
        lastFocused = document.activeElement;
        videoModal.hidden = false;
        videoModalIframe.src = VIDEO_EMBED_BASE + VIDEO_ID + '?autoplay=1&rel=0';
        document.body.style.overflow = 'hidden';
        videoModalClose.focus();
    }

    function closeVideoModal() {
        videoModalIframe.src = '';
        videoModal.hidden = true;
        document.body.style.overflow = '';
        if (lastFocused && typeof lastFocused.focus === 'function') {
            lastFocused.focus();
        }
    }

    if (heroCardPlay) heroCardPlay.addEventListener('click', openVideoModal);
    if (videoModalClose) videoModalClose.addEventListener('click', closeVideoModal);
    if (videoModalBackdrop) videoModalBackdrop.addEventListener('click', closeVideoModal);
    if (videoModal) {
        videoModal.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeVideoModal();
                return;
            }
            // Focus trap: cycle Tab/Shift+Tab within the modal's focusable
            // descendants so keyboard users stay inside while the modal is open.
            if (e.key === 'Tab') {
                const focusable = getModalFocusable();
                if (focusable.length === 0) {
                    e.preventDefault();
                    videoModalClose.focus();
                    return;
                }
                const first = focusable[0];
                const last = focusable[focusable.length - 1];
                const active = document.activeElement;
                if (e.shiftKey) {
                    if (active === first || !videoModal.contains(active)) {
                        e.preventDefault();
                        last.focus();
                    }
                } else {
                    if (active === last) {
                        e.preventDefault();
                        first.focus();
                    }
                }
            }
        });
    }

    // ---------- Back to Top ----------
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
        const toggleBackToTop = () => {
            backToTop.classList.toggle('visible', window.scrollY > window.innerHeight * 0.5);
        };
        window.addEventListener('scroll', toggleBackToTop, { passive: true });
        toggleBackToTop();
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
})();
