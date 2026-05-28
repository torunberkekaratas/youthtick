/* ────────────────────────────────────────────────────────
   FALLBACK SHIM FOR CACHED CLIENTS
   This file ensures that returning visitors who have the 
   old HTML cached do not see a broken website. It intercepts
   the old calls and loads the new ES Module architecture.
   ──────────────────────────────────────────────────────── */

(async function() {
    console.warn("Legacy components.js loaded from cache. Bootstrapping new architecture...");
    
    // Expose required functions dynamically to prevent "renderNav is not defined" errors
    try {
        const navMod = await import('./assets/js/components/navigation.js');
        window.renderNav = navMod.renderNav;
        window.closeMobileMenu = navMod.closeMobileMenu;
        
        const footMod = await import('./assets/js/components/footer.js');
        window.renderFooter = footMod.renderFooter;
    } catch (e) {
        console.error("Failed to load modular components from shim", e);
    }

    // Inject the new master app.js if it's not already on the page
    if (!document.querySelector('script[src*="app.js"]')) {
        const script = document.createElement('script');
        script.type = 'module';
        script.src = 'assets/js/core/app.js';
        document.body.appendChild(script);
    }
})();
