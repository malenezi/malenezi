# SDAIA Academy — National Data & AI Competency Framework

A fully static, production-ready website presenting the National Data & AI
Competency Framework as an executive-grade interactive experience.

## Running the site

No build step, server, or dependencies are required. Open `index.html` in any
modern browser, or serve the folder with any static host:

    # any one of these
    python3 -m http.server 8000
    npx serve .

Then visit the site root.

## Folder structure

    site/
    ├── index.html            Home
    ├── about.html            About the Framework
    ├── framework.html        Framework Structure
    ├── competencies.html     Competency Model
    ├── roles.html            Job Families & Roles
    ├── pathways.html         Learning Pathways
    ├── catalog.html          Course Catalog (searchable / filterable)
    ├── certifications.html   Certifications
    ├── governance.html       Governance & Standards
    ├── contact.html          Contact
    ├── robots.txt            SEO
    ├── sitemap.xml           SEO
    ├── css/
    │   └── style.css         Single shared stylesheet (design system)
    ├── js/
    │   ├── script.js         Shared interactions
    │   └── data.js           Course catalog data (window.SDAIA_PROGRAMS)
    └── assets/
        └── academy-icon.svg  Brand mark

## Design system

Visual identity, palette, typography, spacing, and UI components are derived
from the reference catalog. Key tokens (see `css/style.css` `:root`):

- Brand indigo `#414486`, sky `#70C8F2`, teal `#469A8A`, warm paper `#f7f5f0`
- Display serif **Fraunces**, sans **Geist**, mono **Geist Mono**
- Motion easing `cubic-bezier(0.2,0.7,0.2,1)`; 1280px content width

## Interactive features

- Sticky navigation with scroll shadow + mobile drawer
- Animated statistics counters (`data-count`)
- Scroll-reveal entrance animations (IntersectionObserver, with failsafe)
- Catalog: live search + persona / level / portfolio filters + URL deep-links
  (e.g. `catalog.html#portfolio=engineering`)
- Tabs (competency register, QA metrics) and accordions (job families, FAQs)
- Client-side contact form validation (demo — no transmission)

## Accessibility & performance

- Semantic HTML5, skip links, ARIA states on interactive widgets
- `prefers-reduced-motion` respected; keyboard-navigable
- No external JS frameworks — only Google Fonts is loaded remotely
- SEO: per-page titles, meta descriptions, Open Graph tags, sitemap, robots

## Notes

The catalog presents a representative 45-program sample extracted from the
reference catalog. The full framework comprises 178 programs across 39
pathways. The contact form is a front-end demonstration only.
