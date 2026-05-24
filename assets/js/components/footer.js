export function renderFooter() {
  const currentYear = new Date().getFullYear();
  const footerHTML = `
  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">

        <div class="footer-brand">
          <img src="logoalt.png" alt="YouthTICK Light Logo" style="height: 64px; width: auto; margin-bottom:1.5rem; opacity: 0.9;" />
          <p class="footer-desc" data-i18n="footer.desc" style="color:var(--text-light); opacity:0.8; font-size:1.05rem; line-height:1.6; max-width: 320px;">
            A youth initiative dedicated to building intercultural bridges and civic engagement across Europe.
          </p>
          <div class="footer-socials">
            <a href="https://facebook.com/youthtick" target="_blank" rel="noopener noreferrer" aria-label="Facebook" class="footer-social">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
            </a>
            <a href="https://instagram.com/youthtick" target="_blank" rel="noopener noreferrer" aria-label="Instagram" class="footer-social">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            </a>
            <a href="https://linkedin.com/company/youthtick" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" class="footer-social">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
            </a>
            <a href="mailto:info@youthtick.org" aria-label="Email Us" class="footer-social">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-links">
          <h4 data-i18n="footer.about">About Us</h4>
          <ul>
            <li><a href="about.html" data-i18n="nav.about">Our Story</a></li>
            <li><a href="team.html" data-i18n="nav.team">Team</a></li>
            <li><a href="focus.html" data-i18n="nav.focus">Focus Areas</a></li>
            <li><a href="impact.html" data-i18n="nav.impact">Impact</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h4 data-i18n="footer.action">Action</h4>
          <ul>
            <li><a href="programs.html" data-i18n="nav.programs">Programs</a></li>
            <li><a href="projects.html" data-i18n="nav.projects">Projects</a></li>
            <li><a href="opportunities.html" data-i18n="nav.opportunities">Opportunities</a></li>
            <li><a href="events.html" data-i18n="nav.events">Events</a></li>
            <li><a href="volunteer.html" data-i18n="nav.join">Join Us</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h4 data-i18n="footer.resources">Resources</h4>
          <ul>
            <li><a href="blog.html" data-i18n="nav.blog">Blog & News</a></li>
            <li><a href="partnership.html" data-i18n="nav.partnership">Partnerships</a></li>
            <li><a href="contact.html" data-i18n="nav.contact">Contact</a></li>
            <li><a href="privacy.html" data-i18n="footer.privacy">Privacy Policy</a></li>
            <li><a href="#" onclick="resetCookieConsent();return false;" data-i18n="footer.cookies">Cookie Preferences</a></li>
          </ul>
        </div>

      </div>

      <div class="footer-bottom">
        <p>&copy; ${currentYear} YouthTICK. <span data-i18n="footer.rights">All rights reserved.</span> <span style="opacity:0.5; margin-left: 8px;" data-i18n="footer.built">Built in Yalova.</span></p>
        <p style="opacity:0.4; font-size:0.8rem; margin-top:0.25rem;" data-i18n="footer.disclaimer">This project is independent and is not directly funded by the European Union.</p>
      </div>
    </div>
  </footer>
  `;
  document.body.insertAdjacentHTML('beforeend', footerHTML);
}
