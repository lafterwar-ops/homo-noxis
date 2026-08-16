# KingJack Production — Chapter 15 — Round 01

## Baseline

- Authorized target: `manuscript/chapters/chapter15-Knocks.tex`.
- Starting SHA-256: `239FD4DC9C9809EAC99EB1D587CD8EC00B9B979A3A635B2969AC67DA44E34823` — exact match.
- Starting canonical count under `[A-Za-z0-9]+(?:[-'’][A-Za-z0-9]+)*`: `1818` — exact match.
- Starting byte length: `9458`.
- Both arbitration old-text anchors occurred exactly once before production.

## Arbitration seal

- Required arbitration SHA-256: `83B60B3310FA0CBAC2F4EC64E5DB8F3D94366027BD13A17C625938D67D689516`.
- Observed arbitration SHA-256: `83B60B3310FA0CBAC2F4EC64E5DB8F3D94366027BD13A17C625938D67D689516`.
- Result: exact match; arbitration was `COMPLETE` and executable.

## Operations applied

1. `KJ15-R01-01` was applied first as the complete exact substitution. Its checkpoint matched: SHA-256 `288E432D119D1D83395F0CD7FDD33D90455E8A12A74EBAC42144D098F9EDAABF`, canonical count `1815`, and `9443` bytes.
2. `KJ15-R01-02` was then applied as the complete exact substitution. No smoothing, improvisation, rejected/deferred proposal, or other manuscript change was introduced.

## Changed files

- `manuscript/chapters/chapter15-Knocks.tex` — exactly the two authorized substitutions.
- `notes/omega/chapter-15/round-01/production.md` — this completed production record.

No other file was written by this producer.

## Deterministic validation

| Check | Required | Observed | Result |
|---|---:|---:|---|
| Final SHA-256 | `C32F9AF128E8071D4CD8750D8B659BB727B4230F1A9DFBB062D603581D6A212B` | `C32F9AF128E8071D4CD8750D8B659BB727B4230F1A9DFBB062D603581D6A212B` | pass |
| Canonical count | `1826` | `1826` | pass |
| Byte length | `9505` | `9505` | pass |
| Operation 01 old/new anchor | `0 / 1` | `0 / 1` | pass |
| Operation 02 old/new anchor | `0 / 1` | `0 / 1` | pass |
| `\begin{room}` / `\end{room}` | `1 / 1` | `1 / 1` | pass |
| Opening / closing braces | `20 / 20` | `20 / 20` | pass |

- Strict UTF-8 decoding passed; the file has no BOM, no CRLF sequence, and no bare carriage return.
- The target diff has exactly two zero-context hunks, at the two authorized existing lines. Each hunk is a one-line replacement; no line was inserted or deleted and the physical line count is unchanged.
- `git diff --check -- manuscript/chapters/chapter15-Knocks.tex` passed with no whitespace error.
- `git diff --cached --quiet` returned success: the index is empty.

## Source and continuity validation

- Operation 01 removes only the backward recorder-position contradiction: the machine remains on the table under Paul's operational custody, Sarah's challenge remains intact, and no pickup, set-down, movement, or new gesture is asserted.
- Operation 02 is live speech addressed to `Mr Morgan`. It keeps the fresh paper under the lamp, identifies the folder evidence as two older traces, makes the technical speaker recoverable as Sarah, and creates no transfer or new custody chain.
- The existing speakers and sources remain recoverable through address, domain knowledge, named monitoring, witnessed memory, and the handled records.
- Because the target diff is exhausted by those two substitutions, plot, proof order, custody, causal sequence, bounded uncertainty, final outcome, and the road/well continuation are unchanged.

## Form validation

- The chapter remains one room and fully live: every nonblank content line is dialogue or an existing permitted structural/documentary cue.
- No omniscient narration, interior motive, speaker-label system, new sound, new documentary divider, new room, external-camera statement, or unsupported scientific/provenance detail was added.
- The canonical final count `1826` remains inside the fixed band `1637..1999`.

## Build validation

- Not run — environmental/firewall limitation, not a prose failure. `latexmk`, `pdflatex`, `xelatex`, and `lualatex` are installed, but the sealed three-file production brief contains no established full-book build root or command. Discovering one would widen the producer's prohibited read scope, while compiling the chapter fragment alone would not be a valid book build. No prose was changed in response. KingJack's independent closure must run the established full build.

## Compliance

- Read scope remained limited to this production record, the sealed arbitration, and the authorized Chapter 15 target.
- Write scope remained limited to the target and this production record, both through exact patches.
- Operations were applied in the sealed order and no rejected or deferred idea was reopened.
- Nothing was staged, committed, or pushed.

## Independent KingJack closure

- KingJack independently inspected the final diff and confirmed exactly two authorized one-line replacement hunks and no other manuscript movement.
- All four fenced arbitration blocks were checked against the produced manuscript: both old blocks occur zero times and both approved replacements occur exactly once.
- Chapter 15 remains a fully live recorded room. Every nonblank content line is dialogue or an existing structural/documentary cue; no omniscient statement, narrator gloss, speaker-label system, new sound, gesture, divider, or room entered production.
- The recorder remains on the Chapter 14 table under Paul's operational custody. Sarah's address to `Mr Morgan` makes her technical turn recoverable, the fresh drum paper remains under the lamp, and the folder evidence is explicitly the two older traces. No paper or machine changes hands.
- Final canonical count is `1826`, up `8` words (`+0.440%`) from `1818`, inside `1637..1999`. Final SHA-256 is `C32F9AF128E8071D4CD8750D8B659BB727B4230F1A9DFBB062D603581D6A212B`; final length is `9505` bytes.
- The proof order, two remembered rites, cautious archival match, Kailan's recognition, Sarah's calendar method, live double knock, emergency-readiness alternative, bounded `Who`, inside/outside uncertainty, and road/well outcome remain unchanged.
- Chapter 14 leaves the recorder on the table and fresh paper under the lamp; Chapter 15 opens around those objects and closes on Kailan's promise to tell the road from the well; Chapter 16 begins that first-person account. Chapters 1--14 retain their sealed hashes and no later chapter changed.
- Structural and repository checks pass: one balanced room, raw braces `20/20`, UTF-8 without BOM, LF-only line endings, clean `git diff --check`, and empty Git index.
- A full `latexmk` build was independently attempted. MiKTeX exited before processing the manuscript with code `-1073740791`, reporting that its fresh-install setup is unfinished. This is an environment limitation, not a Chapter 15 LaTeX failure.
- No staging, commit, or push was performed.

State: COMPLETE
