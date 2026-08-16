# KingJack Production - Chapter 19 - Round 01

## Preconditions

- Arbitration SHA-256 required and observed: `1D686C6B48BDC0E96C6AB0FECFE5FD9F0CE02C27FB10501CFE3906C24D4C2627`.
- Target baseline SHA-256 required and observed: `F40D8E4FAD57C5DFA534233F90D215AC200BFAB8C437B61ABE8BAFB8E7BEFA4D`.
- Baseline canonical count required and observed: `7424`; fixed band: `6682..8166`.
- Baseline physical form required and observed: `40351` bytes, UTF-8 without BOM, `354` LF, `0` CRLF, `0` lone CR, terminal LF present.
- Four arbitration operations parsed. Immediately before production began, every exact old block occurred once and every exact replacement block occurred zero times.

## Ordered operations

1. Restored the omitted nearest-truth term: pre-gate `old 1 / new 0`; post-gate `old 0 / new 1`.
2. Established provisional recorder custody and placed Jean-Charles: pre-gate `old 1 / new 0`; post-gate `old 0 / new 1`.
3. Made Shield's second intervention continuous: pre-gate `old 1 / new 0`; post-gate `old 0 / new 1`.
4. Sourced the visible connective tissue of the depositions: pre-gate `old 1 / new 0`; post-gate `old 0 / new 1`.

Operations 1-4 were applied exactly, in order, with no discretionary wording, joins, cleanup, reformatting, or normalization.

## Changed files

- `manuscript/chapters/chapter19-Seal.tex`
- `notes/omega/chapter-19/round-01/production.md`

No other file was edited.

## Exact validation

- Final target SHA-256: `2CF7C1430F5ECD7ADB0767C38E2C10103C856B383843460838F7C889E89378DA`.
- Canonical count: `7495`, inside `6682..8166`.
- Physical form: `40786` bytes, UTF-8 without BOM, `354` LF, `0` CRLF, `0` lone CR, terminal LF present.
- LaTeX/form counts: `\typesetchapter` `1`; total `\begin`/`\end` `3/3`; `center` `2/2`; `room` `1/1`; `\ornament` `10`; `\par` `137`; `\textit` `3`; `\emph` `9`.
- Final exact-block gates: Operations 1-4 each `old 0 / new 1`.
- Target `git diff --check`: passed with exit code `0`.
- Git index: empty.

## Diff mapping

The target diff contains exactly four replacement hunks, each confined to its authorized operation: line 40 maps to Operation 1, line 61 to Operation 2, line 75 to Operation 3, and line 140 to Operation 4. No target line outside those operations changed.

## Build and Git actions

No full build was run because the sealed inputs expose no root or build command. No file was staged, committed, or pushed, and no other Git action was taken.

## Independent KingJack closure

- Recomputed target SHA-256 `2CF7C1430F5ECD7ADB0767C38E2C10103C856B383843460838F7C889E89378DA`, canonical count `7495`, bytes `40786`, LF `354`, CRLF/lone CR `0`, no BOM, and terminal LF: PASS.
- Recomputed form: room `1/1`; center `2/2`; ornaments `10`; prose paragraphs `137`; braces `20/20`: PASS.
- Exact-operation audit: Operations 1–4 each have old block `0` and replacement block `1`; exactly four diff hunks map one-to-one to the sealed authority: PASS.
- Justice-math audit: every displayed Pell pair has the stated alternating sign and `239/169` now follows `99/70`; the false-witness posterior equals `10/343`; `4969` gives remainders `6,8,3,5`; the least-squares seventh-year forecast is `12.6`: PASS.
- Source/custody audit: provisional hearing custody controls the already-turning recorder without granting the later Threshold Exception; the sealed reel remains source of deposition words and Paul's explicitly supplied observations remain source of visible detail: PASS.
- Architecture audit: all five Justice rooms, five distinct office roads/arches, hearing, Threshold Exception, isolated depositions, refusal audit, denial road, Roger call, ruling, Ka-Elun's death, Faith damage, Greater Seal, Jean-Charles ambiguity, Sarah's silence, and final Pendulum remain fixed: PASS.
- Boundary audit: Chapter 18's final blast passes into Chapter 19's fresh-reel handoff; Chapter 19's still-turning reel passes into Chapter 20's nine-day-later Hall account: PASS.
- Scope/Git audit: Chapter 18 retains SHA `01506221871D731FF6E66C85E89D6F862E0E8772C7083DC74834EED789C031D2`; Chapter 20 remains untouched; HEAD remains `da3c50c4ea2f0f166be9675cb63dc5040cbb032a`; index empty; nothing staged, committed, or pushed: PASS.
- Full-book build: independently attempted with `latexmk` against `manuscript/00 Intro/chapter001-latexIntro.tex`, with output directed to the system temporary directory. MiKTeX stopped before manuscript processing because its fresh-install setup is unfinished; this is an environmental limitation, not a detected manuscript failure.
- Word movement: `7424 -> 7495` (`+71`, approximately `+0.96%`), inside the fixed `6682..8166` band.

State: COMPLETE
