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
