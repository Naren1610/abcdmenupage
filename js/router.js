/**
 * Page Router & Transition Manager for ABCD Restaurant Menu
 * Handles smooth fade transitions between distinct HTML pages.
 */

document.addEventListener("DOMContentLoaded", () => {
    // 1. Initial Page Load Transition (Fade In)
    // We remove the 'page-transitioning' class on load so the page fades in from black
    setTimeout(() => {
        document.body.classList.add('page-loaded');
    }, 50);

    // 2. Handle ABCD Navigation Clicks
    const navLetters = document.querySelectorAll('.abcd-letter');
    navLetters.forEach(letter => {
        letter.addEventListener('click', (e) => {
            e.preventDefault();
            const targetUrl = e.currentTarget.getAttribute('data-url');
            if (targetUrl) {
                navigateToPage(targetUrl);
            }
        });
    });

    // 3. Handle Back Button Clicks (from menu pages)
    const btnBack = document.querySelector('.btn-icon[href="index.html"]');
    if (btnBack) {
        btnBack.addEventListener('click', (e) => {
            e.preventDefault();
            navigateToPage("index.html");
        });
    }

    // Shared Transition Function
    function navigateToPage(url) {
        // Trigger fade out via CSS class
        document.body.classList.remove('page-loaded');
        document.body.classList.add('page-exiting');

        // Wait for CSS transition (approx 400ms) before changing href
        setTimeout(() => {
            window.location.href = url;
        }, 400);
    }
});

// 4. Handle Bfcache (Back/Forward Cache) for browser back button
window.addEventListener('pageshow', (event) => {
    // If the page was loaded from cache (e.g. by hitting back), reset the transition state
    if (event.persisted || document.body.classList.contains('page-exiting')) {
        document.body.classList.remove('page-exiting');
        
        // Small delay to ensure the DOM is ready to paint the transition back in
        setTimeout(() => {
            document.body.classList.add('page-loaded');
        }, 10);
    }
});
