# KingJack Production — Chapter 18 — Round 01

## Preconditions

- Arbitration SHA-256 verified: `0C6C5E8442781ACE9CCF6981ED3F5FCF95E85498F9E061547ECE5845B62DA7D4`.
- Target baseline SHA-256 verified: `02ECE03C7B961226959572B040129C206B75B468EA6627691B3136440D02611E`.
- Target baseline verified at `44049` bytes and canonical count `7913`, within the fixed band `7122..8704`.
- Baseline encoding/newlines verified: UTF-8 without BOM; `511` LF; `0` CRLF; `0` lone CR; terminal LF present.
- All five exact old blocks occurred once and all five exact replacements occurred zero times before production. Before each individual operation, its old block was reverified at `1` and its replacement at `0`.

## Applied operations

1. Identified Paul's strategic inference with the exact authorized replacement.
2. Identified the strip-timing inference with the exact authorized replacement.
3. Moved only the observed camp-separation paragraph ahead of Kailan's recognition.
4. Attributed documentary genuineness to Sarah with the exact authorized replacement.
5. Replaced the mind-reading verb with Paul-visible action using the exact authorized replacement.

No discretionary edits, joins, cleanup, rewording, or normalization were made.

## Changed files

- `manuscript/chapters/chapter18-Return.tex`
- `notes/omega/chapter-18/round-01/production.md`

## Final validation

- Target SHA-256: `01506221871D731FF6E66C85E89D6F862E0E8772C7083DC74834EED789C031D2`.
- Canonical count: `7941` (`+28`), within `7122..8704`.
- Size: `44180` bytes (`+131`).
- Encoding/newlines: valid UTF-8 without BOM; `511` LF; `0` CRLF; `0` lone CR; terminal LF present; `512` lines.
- Exact operation blocks after production: Operations 1–5 each old `0`, replacement `1`.
- LaTeX/form counts: `\typesetchapter{` `1`; `\begin{room}` `1`; `\end{room}` `1`; `\ornament` `7`; `\par` `233`; `\emph{` `3`; `\textit{` `1`; `\centerline{` `1`; opening braces `12`; closing braces `12`.
- Target diff has exactly five normal-context hunks. Hunk at line 32 maps only to Operation 1; line 68 only to Operation 2; line 236 only to Operation 3; line 272 only to Operation 4; line 446 only to Operation 5. Every changed manuscript line is accounted for by those operations.
- `git diff --check -- manuscript/chapters/chapter18-Return.tex` passed.
- Git index verified empty.
- Full build not attempted: the sealed-input firewall exposes no configured root or build command.
- No Git staging, commit, push, or other Git mutation was performed.

## Independent KingJack closure

- Recomputed target SHA-256 `01506221871D731FF6E66C85E89D6F862E0E8772C7083DC74834EED789C031D2`, canonical count `7941`, byte count `44180`, LF `511`, CRLF/lone CR `0`, no BOM, and terminal LF: PASS.
- Recomputed form: chapter `1`; room `1/1`; ornaments `7`; prose paragraphs `233`; braces `12/12`: PASS.
- Exact-operation audit: Operations 1–5 each have old block `0` and replacement block `1`; the five diff hunks contain no change outside their authority: PASS.
- Source audit: the strategic and airstrip conclusions are explicitly Paul's inferences; Sarah carries the institutional authenticity judgment; Va-Sheva is described only through visible action: PASS.
- Architecture audit: the frame, Paul handoff, full return route, custody chain, Jean-Charles ambiguity, Mountain entry, Va-Sheva reception, common wards, and final blast remain fixed: PASS.
- Boundary audit: Chapter 17's lawn tape ends into Chapter 18's Greater Seal frame and Paul account; Chapter 18's final blast passes into Chapter 19's fresh reel and Kailan's Justice-road takeover: PASS.
- Scope/Git audit: no earlier or later manuscript edit was authorized; Chapter 19 remains untouched; HEAD remains `da3c50c4ea2f0f166be9675cb63dc5040cbb032a`; index empty; nothing staged, committed, or pushed: PASS.
- Full-book build: independently attempted with `latexmk` against `manuscript/00 Intro/chapter001-latexIntro.tex`, with output directed to the system temporary directory. MiKTeX stopped before manuscript processing because its fresh-install setup is unfinished; this is an environmental limitation, not a detected manuscript failure.
- Word movement: `7913 -> 7941` (`+28`, approximately `+0.35%`), inside the fixed `7122..8704` band.

State: COMPLETE
