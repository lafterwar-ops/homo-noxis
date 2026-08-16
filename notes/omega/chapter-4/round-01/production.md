# Chapter 4 — KingJack Round 01 — Production Record

## Scope

- Producer: fresh constrained KingJack producer
- Arbitration: complete before production began
- Content target: `manuscript/chapters/chapter4-Mountain.tex`
- Record target: `notes/omega/chapter-4/round-01/production.md`
- Files read: the completed arbitration, this production record, and the Chapter 4 target only
- Files written: `manuscript/chapters/chapter4-Mountain.tex` and this production record only
- Staging, commit, and push: not performed

## Baseline and preconditions

- Target SHA-256: `77F2B71AF7AA8597FEC361959B8802C56B577A9F4D363672655E5BC34633EE02` — exact match
- Authoritative Unicode lexical count by `\b[\p{L}\p{N}’'-]+\b`: `5304` — exact match
- Git index: empty
- Encoding and line endings: UTF-8 without BOM; `365` LF line endings and `0` CRLF line endings
- Authorized anchors: each occurred exactly once

All preconditions passed before the first successful manuscript edit.

## Ordered operations

1. Opening chronology: replaced only `And yesterday, the heavens:` with `And the heavens:`. The first context-rich patch attempt matched no line and made no change; the unique complete opening room was then read, the exact authorized substring was applied, and the complete containing room was reread. Removed occurrence: `0`; replacement occurrence: `1`.
2. Kailan's condition: replaced the unique full line beginning `--- That is the whole of it. And if I am proven right` with the arbitration's exact watcher/man/machine/evidence line. The complete containing room was reread. Removed full-line occurrence: `0`; replacement full-line occurrence: `1`.
3. Paul's promise: replaced the unique full line beginning `--- Very well. If there are men behind that glass` with the arbitration's exact `If I find the eye you have described` line. The complete containing room was reread. Removed full-line occurrence: `0`; replacement full-line occurrence: `1`.
4. Editing stopped after the third authorized substitution.

## Departures

- Manuscript departures from the arbitration brief: none.
- Unapproved interpretation or improvisation: none.
- The initial failed patch verification in operation 1 was a zero-change attempt; target hash and contents remained at baseline before the authorized substitution was applied.

## Final manuscript validation

- Exact diff: pass. It contains exactly three removed lines and three replacement lines implementing the three ordered substitutions, with no other manuscript change.
- Final authoritative Unicode lexical count: `5310` — exact expected count and inside fixed band `4774..5834`.
- Final SHA-256: `4AFD2C89E87D3C831BDF8CD48051F9F113F47200591BD60EBE1B4730D21FB435` — exact predicted hash.
- Encoding and line endings: UTF-8 without BOM; still `365` LF line endings and `0` CRLF line endings.
- Removed opening counts: `And yesterday, the heavens:` = `0`; `And if I am proven right, if anything at all stands behind that glass` = `0`; `If there are men behind that glass` = `0`.
- Replacement counts: the complete `And the heavens: \textit{Cosmos, a Personal Voyage}.` replacement = `1`; the complete Kailan replacement line = `1`; the complete Paul replacement line = `1`.
- TeX structure: `12` `\begin{...}` tokens and `12` `\end{...}` tokens; environment names and nesting are balanced.
- Source legality and omniscience: pass. All changes remain in identified dialogue; no neutral or omniscient narration was added.
- Preserved unknowns: pass. The prospective condition names possible evidence without confirming a watcher, mechanism, target, identity, form, or outcome.
- Chapters 1–3: untouched. No production command wrote them; every patch target was one of the two authorized files.
- `git diff --check`: pass.
- Git index after validation: empty.
- Stage, commit, push: none performed.

## Build availability

- `latexmk` and `pdflatex` are available from MiKTeX.
- Full build: not attempted. The constrained assignment permits reading only the arbitration, production record, and Chapter 4 target, so no repository build entry point or other manuscript input was opened. This is a scope limitation, not a manuscript failure.
- Available Chapter 4 LaTeX sanity gate: pass (`12` begins, `12` ends, balanced environment names and nesting); `git diff --check` also reports no error.

## Independent KingJack verification

- The final manuscript diff was independently inspected and contains exactly the three arbitration-authorized substitutions (`3` removed lines / `3` replacement lines), with no extra whitespace or manuscript movement.
- The final count and SHA-256 independently reproduce `5310` and `4AFD2C89E87D3C831BDF8CD48051F9F113F47200591BD60EBE1B4730D21FB435`.
- All removed and replacement strings independently reproduce the required `0` and `1` occurrence counts.
- Source legality passes: all revised assertions are spoken by Paul or Kailan inside the established lawn/interview room; no omniscient narration or unknown outcome was introduced.
- Chapters 1, 2, and 3 retain their exact post-KingJack hashes. Chapter 5 remains clean, and its opening still carries the Kepler, divided-light, and measurement consequences forward without contradiction.
- A full build was independently attempted with `latexmk -xelatex -interaction=nonstopmode -halt-on-error` against `manuscript/00 Intro/chapter001-latexIntro.tex`, directing output to a temporary directory. MiKTeX exited before reading the manuscript (`-1073740791`) and reported that its fresh-install setup must be completed. This is an environment limitation, not a manuscript diagnostic.
- The final Git index is empty; no stage, commit, push, branch switch, or history rewrite occurred.

## Exact changed files

1. `manuscript/chapters/chapter4-Mountain.tex` — exactly three authorized substitutions.
2. `notes/omega/chapter-4/round-01/production.md` — WAITING record replaced by this execution record.

State: COMPLETE
