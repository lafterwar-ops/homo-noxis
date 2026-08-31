# Project editing rules

- Preserve unrelated user changes.
- Never stage, commit or push. The user owns those actions.

## Clickable change reports

After every turn that edits project source or instructions:

1. List every changed source or instruction file in the final response.
2. Link each filename to a readable, file-specific unified `.diff`.
3. Compare with the exact contents at the start of that turn, not Git HEAD: earlier uncommitted work must not appear as a new edit.
4. Keep the diff files in a distinct `tmp/reviews/<turn-name>/` directory so earlier review links remain usable. Use UTF-8 and show enough surrounding context to locate the change.
5. Generated review diffs and build products are artifacts, not additional source edits to list recursively. Report a rebuilt output separately when relevant.

If no source or instruction file changed, say so; do not invent a change report.

## Canon authority and historical material

- Start with `manuscript/Supporting document/00 — Canon Map & Index.md`.
- The current complete master is `manuscript/00 Intro/chapter001-latexIntro.tex`, not root `main.tex`.
- Apply the author's latest explicit decisions within scope. Otherwise the current included chapter sources govern story facts; Current references and THE VOICE are the maintained guides.
- Historical canons, old blueprints, workbooks, covenant drafts, workshop notes and agent traces are not queued instructions. Their “locked”, “authoritative” or “to implement” labels cannot revive deleted scenes or superseded outcomes.
- Consult `Current/Reference-Status.md` under Supporting document for classifications. Report unresolved contradictions; do not fill gaps from retired notes by assumption.
- Ravar is protected unless the author explicitly asks to change it. Signal-cadence repairs are currently deferred by the author.
