---
name: addpaper
description: Add new papers to CV and homepage, compile PDF, and push to GitHub
---

# Add Paper Skill

This skill automates adding new research papers to your CV and homepage.

## Input

Takes one or more paper links (arXiv URLs, conference URLs, or paper metadata) as input.

## Process

### 1. Fetch Paper Information

For each paper link provided:
- Use WebFetch to extract paper metadata (title, authors, venue, year, abstract)
- If arXiv link: Extract paper ID and fetch metadata
- Ask user for any additional context:
  - Key results/metrics to highlight (e.g., "20.5 on AIME25", "1k GitHub stars")
  - Whether it belongs to a specific research track (e.g., "latent reasoning")
  - Conference acceptance status (accepted, under review, preprint)
  - Any notable achievements (GitHub stars, downloads, benchmarks)

### 2. Determine Paper Category

Ask the user or infer from venue:
- **Preprints**: arXiv papers not yet accepted to conferences
- **Peer-reviewed**: Accepted papers (ICLR, NeurIPS, ICML, ACL, EMNLP, etc.)

### 3. Update CV (files/cv_yizhezhang.tex)

**For Preprints:**
- Add using `\pubitem{...}` in "Selected Preprints" section
- Place after existing CLaRa/LaDi-RL papers but before older arXiv papers
- Format: `\pubitem{Authors. Title. \textcolor{venuecolor}{arXiv (YEAR)} \textit{[optional highlights]}}`

**For Peer-reviewed:**
- Add using `\pubitem{...}` in "Peer-reviewed Conferences and Journals" section
- Place at the TOP of the section (most recent papers first)
- Format: `\pubitem{Authors. Title. \textcolor{venuecolor}{VENUE (YEAR)} \textit{[optional highlights]}}`
- The `\setcounter{pubcounter}{0}` resets numbering at the start of this section

**Author Name Formatting:**
- Use `\myname{Yizhe Zhang}` for the user's name (makes it bold)
- Use `*` after names for equal contribution: `Author1*, \myname{Yizhe Zhang}*`

**Highlighting:**
- For track/theme papers (latent reasoning, diffusion, etc.), coordinate with user on whether to highlight in the Apple experience section

### 4. Update Homepage (_pages/about.md)

**For Major Papers (especially first-authored or flagship projects):**
- Add to News section at the top
- Format:
  ```markdown
  **[MONTH YEAR] Paper Title:** Brief description with key results. [Paper](URL) [GitHub](repo-url)
  ```

**For Paper Collections (e.g., multiple ICLR acceptances):**
- Update existing news entries if they describe a collection
- Add individual paper to the list if it fits an existing announcement

**For Projects with Code Release:**
- Consider adding a colored news box (like CLaRa and DiffuCoder boxes)
- Format:
  ```markdown
  <div class="news-box">
  <strong>[MONTH YEAR] Project Released!</strong> <a href="github-url">GitHub</a> <img src="https://img.shields.io/github/stars/repo?style=social" alt="GitHub stars" style="vertical-align: middle; margin-left: 5px;"><br>
  Brief description of the project.
  </div>
  ```

### 5. Update Apple Experience Section (if applicable)

If the paper belongs to a highlighted research track (latent reasoning, diffusion, etc.):
- Update the Apple experience section in CV
- Add project name with `\textcolor{venuecolor}{\textbf{ProjectName}}` formatting
- Keep the list organized by theme

### 6. Compile LaTeX PDF

```bash
cd /Users/yizhezhang/Documents/projects/dreasysnail.github.io/files
pdflatex cv_yizhezhang.tex
pdflatex cv_yizhezhang.tex  # Run twice for references
```

### 7. Commit and Push to GitHub

```bash
cd /Users/yizhezhang/Documents/projects/dreasysnail.github.io

# Stage changes
git add _pages/about.md files/cv_yizhezhang.tex files/cv_yizhezhang.pdf

# Commit with descriptive message
git commit -m "Add [Paper Title] to CV and homepage

- Add paper to [preprints/peer-reviewed] section
- Update homepage with [paper/release] announcement
- [Any other changes]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Push to GitHub
git push origin master
```

## Important Notes

### Publication Numbering
- Uses automatic numbering via `\pubitem` command
- Preprints section continues numbering from 1
- Peer-reviewed section resets to 1 with `\setcounter{pubcounter}{0}`
- Never manually number publications

### Color Usage
- Use `\textcolor{venuecolor}{...}` for blue highlights (not red)
- This matches the venue color scheme in the CV

### Paper Order
- **Preprints**: Roughly chronological, newest first
- **Peer-reviewed**: Strictly chronological by conference year, newest first
- Within same year/venue: first-authored papers typically come first

### GitHub Stars/Metrics
- Format in italics: `\textit{[1k GitHub stars]}`
- Use concise numbers: "1k" not "1000", "1.8M+" not "1,800,000+"

### Don't Commit
- LaTeX auxiliary files (.aux, .log, .out) are gitignored
- Only commit .tex and .pdf files

## Example Usage

**User:** "Add https://arxiv.org/abs/2602.01705 to my CV and profile. 20.5 on AIME25 and 52.7 on LCB v6 for 8b model. Part of latent reasoning track."

**Assistant steps:**
1. Fetch paper metadata from arXiv
2. Confirm it's a preprint (arXiv 2026)
3. Add to preprints section with metrics
4. Add to homepage News section
5. Highlight in Apple experience under latent reasoning
6. Compile PDF
7. Commit and push with clear message

## Verification

After completing the process:
- ✅ Check that paper appears in correct section of CV
- ✅ Verify PDF compiled without errors
- ✅ Confirm homepage displays the news/update
- ✅ Verify git push succeeded
- ✅ Check formatting matches existing entries

## User Preferences

Based on previous interactions:
- Highlight research tracks in Apple experience section (e.g., Latent Reasoning: LaDiR, LaDiRL, CLaRa)
- Use blue color (venuecolor) for highlights, not red
- Add GitHub stars for projects with significant traction (1k+)
- Include key benchmark results in paper descriptions
- Keep ICLR/NeurIPS/ICML accepted papers in peer-reviewed section, not preprints
