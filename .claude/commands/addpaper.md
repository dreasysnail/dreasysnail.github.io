---
name: addpaper
description: Add new papers to CV, homepage, and publications page, then compile and push
---

# Add Paper Skill

Automates adding research papers to your academic website.

## Input

Paper links (arXiv URLs, DOIs) or paper metadata with:
- Key results/metrics (e.g., "20.5 on AIME25")
- Research track (e.g., "latent reasoning")
- Status (accepted/preprint)
- GitHub stars/downloads if applicable

## Process

### 1. Extract Paper Metadata

From arXiv/paper link, get:
- Title, authors, venue, year, abstract
- Ask user for highlights and categorization

### 2. Update CV (files/cv_yizhezhang.tex)

**Preprints** (arXiv not yet accepted):
```latex
\subsection{Selected Preprints}
\pubitem{Authors. Title. \textcolor{venuecolor}{arXiv (YEAR)} \textit{[highlights]}}
```

**Peer-reviewed** (accepted papers - add at TOP):
```latex
\subsection{Peer-reviewed Conferences and Journals (* equally contributed)}
\setcounter{pubcounter}{0}
\pubitem{Authors. Title. \textcolor{venuecolor}{VENUE (YEAR)} \textit{[highlights]}}
```

**Misc** (workshops, side projects):
```latex
\subsection{Workshop, Demo, and Miscellaneous}
\pubitem{Authors. Title. \textcolor{venuecolor}{VENUE (YEAR)}}
```

**Author formatting:**
- User's name: `\myname{Yizhe Zhang}` (auto-bold)
- Equal contribution: `Author1*, \myname{Yizhe Zhang}*`

**Highlights:**
- Use `\textcolor{venuecolor}{...}` for blue (NOT red)
- Metrics in italics: `\textit{[1k GitHub stars]}`

### 3. Update Publications Page (_publications/)

Create file: `YYYY-MM-DD-Title.md`

**Date format:**
- Preprints: `2026-12-01` (month=12, day=01 shows in "Preprint" section)
- Peer-reviewed: `2026-10-01` (other dates show in year sections)

**Template:**
```yaml
---
title: "Paper Title"
collection: publications
permalink: /publication/YYYY-MM-DD-Title
date: YYYY-MM-DD
venue: 'Venue Name or arXiv'
paperurl: 'https://arxiv.org/abs/...'
citation: '<b>Yizhe Zhang</b>, Co-Author1, Co-Author2'
topics: ['rag-reasoning', 'text-diffusion', 'code-llm-agents']
description: "One-line summary with key results"
abstract: "Full abstract..."
---

[Download paper here](paperurl)

Recommended citation:
\```bibtex
@article{...}
\```
```

**Topic tags** (for research categories):
- `code-llm-agents`
- `long-horizon-planning`
- `rag-reasoning`
- `text-diffusion`
- `coding-ai-scientist`

### 4. Update Homepage (_pages/about.md)

**Major papers:** Add to News section
```markdown
**[MONTH YEAR] Paper Title:** Description with results. [Paper](URL)
```

**Project releases:** Add colored box
```markdown
<div class="news-box">
<strong>[MONTH YEAR] Project Released!</strong> <a href="url">GitHub</a><br>
Description.
</div>
```

### 5. Update Apple Experience (if research track paper)

```latex
\hspace{1.5em} $\circ$ \textbf{Track Name:} \textcolor{venuecolor}{\textbf{Paper1}}, \textcolor{venuecolor}{\textbf{Paper2}}
```

### 6. Compile and Push

```bash
cd /Users/yizhezhang/Documents/projects/dreasysnail.github.io/files
pdflatex cv_yizhezhang.tex && pdflatex cv_yizhezhang.tex

cd ..
git add _pages/about.md _publications/*.md files/cv_yizhezhang.tex files/cv_yizhezhang.pdf
git commit -m "Add [Paper] to CV and publications

- Add to [section] in CV
- Create publication page
- Update homepage with announcement

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
git push origin master
```

## Key Files

1. **CV**: `files/cv_yizhezhang.tex` (manual LaTeX)
2. **Publications**: `_publications/YYYY-MM-DD-Title.md` (Jekyll pages)
3. **Homepage**: `_pages/about.md` (News section)
4. **Publications index**: `_pages/publications.md` (auto-generates from _publications/)

## Notes

- Use `\pubitem` for automatic numbering (never manual `[1]`, `[2]`)
- Preprints use `month=12, day=01` to show in Preprint section
- Peer-reviewed use other dates to show in year sections
- Blue highlights only (`venuecolor`), never red
- Don't commit `.aux`, `.log`, `.out` files
