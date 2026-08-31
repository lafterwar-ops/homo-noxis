# Homo Noxius

## Current editable book

The full 24-chapter manuscript is assembled by:

- Master: `manuscript/00 Intro/chapter001-latexIntro.tex`
- Chapters: `manuscript/chapters/chapter1-Ascension.tex` through `chapter24-Whole.tex`, in the master's explicit input order.
- Compiled book: `output/chapter001-latexIntro.pdf`

Root `main.tex` is an earlier stub, not the current book master. PDFs, extracted text, submission excerpts and abandoned pass duplicates are not editable source authorities.

## Working references

Read [AGENTS.md](AGENTS.md), then the [current canon map](<manuscript/Supporting document/00 — Canon Map & Index.md>). Current author decisions and actual chapter sources outrank historical canons, conversation exports, review recommendations and agent traces. Old material is retained and explicitly reclassified; do not use it to reinstate superseded story decisions.

## Build

From the repository root in PowerShell:

```powershell
Push-Location output
xelatex -interaction=nonstopmode -halt-on-error "../manuscript/00 Intro/chapter001-latexIntro.tex"
xelatex -interaction=nonstopmode -halt-on-error "../manuscript/00 Intro/chapter001-latexIntro.tex"
Pop-Location
```

Inspect the PDF, not only the log. Keep Chapter 23 byte-identical unless the author explicitly requests a change to Ravar. Do not stage, commit or push; those actions belong to the author.
