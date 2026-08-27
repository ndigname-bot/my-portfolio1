// script.js - Full updated version

// Initialize AOS animations
AOS.init({
    duration: 1200,
    once: true,
    easing: 'ease-in-out-back'
});

// Smooth scrolling for nav links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

// Hide loader reliably (no more waiting for 'load' forever)
function hideLoader() {
    const loader = document.getElementById('loader');
    if (loader) {
        loader.style.transition = 'opacity 1s ease-out';
        loader.style.opacity = '0';
        setTimeout(() => {
            loader.remove();
        }, 1000); // Remove from DOM after fade
    }
}


// Try to hide immediately if page is already loaded
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(hideLoader, 500); // Small delay to let AOS init
} else {
    window.addEventListener('load', hideLoader);
}

// Ultimate fallback: force hide after 3 seconds no matter what
setTimeout(hideLoader, 3000);

// Mobile menu toggle
const menuToggle = document.getElementById('menu-toggle');
const menuOpen = document.getElementById('menu-open');
const menuClose = document.getElementById('menu-close');
const mobileMenu = document.getElementById('mobile-menu');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('translate-x-full');
        mobileMenu.classList.toggle('translate-x-0');
        menuOpen.classList.toggle('hidden');
        menuClose.classList.toggle('hidden');
    });

    // Close menu when clicking a link (better UX)
    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('translate-x-full');
            mobileMenu.classList.remove('translate-x-0');
            menuOpen.classList.remove('hidden');
            menuClose.classList.add('hidden');
        });
    });
}

// Spotlight Cursor Logic
document.addEventListener('mousemove', (e) => {
    const spotlight = document.getElementById('spotlight');
    if (spotlight) {
        spotlight.style.setProperty('--x', `${e.clientX}px`);
        spotlight.style.setProperty('--y', `${e.clientY}px`);
    }
});

// Modal Logic
function openModal(title, description, imageSrc) {
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalDesc').innerText = description;
    document.getElementById('modalImage').src = imageSrc;
    
    const modal = document.getElementById('projectModal');
    const modalContent = document.getElementById('modalContentBlock');
    
    modal.classList.remove('hidden');
    // slight delay to allow display block to apply before opacity transition
    setTimeout(() => {
        modal.classList.remove('opacity-0');
        modalContent.classList.remove('scale-95');
        modalContent.classList.add('scale-100');
    }, 10);
}

function closeModal() {
    const modal = document.getElementById('projectModal');
    const modalContent = document.getElementById('modalContentBlock');
    
    modal.classList.add('opacity-0');
    modalContent.classList.remove('scale-100');
    modalContent.classList.add('scale-95');
    
    setTimeout(() => {
        modal.classList.add('hidden');
    }, 300); // match duration of transition
}

// Close modal if clicked outside
document.getElementById('projectModal')?.addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
});
