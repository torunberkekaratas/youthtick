/* ────────────────────────────────────────────────────────
   FALLBACK SHIM FOR CACHED CLIENTS
   Prevents 404 errors for users with cached HTML files.
   The actual i18n logic is now handled by assets/js/core/app.js
   ──────────────────────────────────────────────────────── */
console.warn("Legacy i18n.js loaded from cache. System will use modular architecture instead.");
