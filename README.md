# YouthTICK

**YouthTICK** is a youth initiative from Yalova, Türkiye — building real Erasmus+ connections, intercultural programs and civic engagement that prepare young people for meaningful roles in European society.

🌐 [youthtick.org](https://youthtick.org)

---

## Tech Stack

- Pure HTML / CSS / JavaScript (no framework)
- ES Modules for component architecture
- Multilingual (EN / TR / DE) via custom i18n system
- Intersection Observer-based scroll animations
- FormSubmit for contact forms

## Structure

```
/
├── index.html          # Homepage
├── about.html
├── blog.html
├── article.html
├── partnership.html
├── contact.html
├── ...
├── styles.css          # Global styles
├── assets/
│   └── js/
│       ├── core/       # app.js, i18n.js, content-bridge.js
│       ├── components/ # navigation.js, footer.js, cookie-banner.js
│       ├── animations/ # scroll.js, cursor.js, card-tilt.js
│       ├── data/       # articles.js
│       └── locales/    # en.js, tr.js, de.js
└── admin/              # Admin panel
```

## License

© 2026 YouthTICK. All rights reserved.
