# Prof. Mamdouh Alenezi

Personal website — [malenezi.github.io/malenezi](https://malenezi.github.io/malenezi/)

**General Manager, SDAIA Academy** at the Saudi Data & Artificial Intelligence Authority, Riyadh.
Full Professor of Software Engineering. I lead national capability development for data and AI,
and publish on software security, AI for software engineering, and engineering education.

## Site structure

| Page | Purpose |
|---|---|
| `index.html` | Home — positioning, metrics, focus areas, selected impact, recent work |
| `about.html` | Extended biography, competencies, education, certifications |
| `leadership.html` | Executive and academic roles, consulting, teaching, supervision, committees |
| `publications.html` | Searchable list of all peer-reviewed publications |
| `projects.html` | Programmes, institutional systems, governance work, funded research |
| `speaking.html` | Conference chairing, committees, peer review, workshops, writing |
| `contact.html` | Contact details, profiles, CV downloads |
| `myblog/` | Insights — essays published on Medium and LinkedIn |

## How the site is built

Plain static HTML, no framework and no build dependencies at runtime. Shared styles live in
`assets/site.css` and behaviour in `assets/site.js`.

Page content is generated from one shared shell so every page stays consistent:

```bash
python3 _build/build.py
```

Content data lives in `data/`:

* `data/publications.json` — every journal article, conference paper and book chapter
* `data/insights.json` — published essays

Edit the data files (or the content constants in `_build/build.py`), re-run the build, and commit.

## Profiles

| | |
|---|---|
| Google Scholar | https://scholar.google.com/citations?user=zH5wDBIAAAAJ |
| ORCID | https://orcid.org/0000-0001-6852-1206 |
| Scopus | https://www.scopus.com/authid/detail.uri?authorId=55854089000 |
| DBLP | https://dblp.org/pers/hd/a/Alenezi:Mamdouh |
| LinkedIn | https://sa.linkedin.com/in/mamdouhalenezi |

<sub>Riyadh, Saudi Arabia</sub>
