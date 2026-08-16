# KingJack Production — Chapter 16 — Round 01

## Authority and baseline

- Role: fresh constrained KingJack producer.
- Authorised source reads: `notes/omega/chapter-16/round-01/production.md`, `notes/omega/chapter-16/round-01/arbitration.md`, and `manuscript/chapters/chapter16-Horizon.tex` only.
- Target baseline SHA-256 verified: `967FCB10465C8094D7C2CF35E982EE6DC7EADDF1A35BE6855AB73995EDFAA0F9`.
- Baseline canonical count verified: `5078` under `[A-Za-z0-9]+(?:[-'’][A-Za-z0-9]+)*`.
- Baseline size verified: `28986` bytes.
- All five arbitration old blocks occurred exactly once before execution.

## Arbitration seal

- Arbitration SHA-256 verified: `EECAC286895E60FE2ED14A37272B59F308A6A25079BAF54FC60E79453870DF11`.
- Arbitration state verified: `COMPLETE`.
- Execution authority was limited to OP-01 through OP-05, exact and in order; rejected and deferred work remained closed.

## Ordered operations executed

| Operation | Executed replacement | Canonical delta |
|---|---|---:|
| OP-01 | Bound upper-hearing facts to the white-haired Justice witness. | `+7` |
| OP-02 | Kept the mirror claim visual by removing the wardens' hearing claim. | `-1` |
| OP-03 | Defined supervision as supervision of the lessons while permitting the manual's reading custody. | `-1` |
| OP-04 | Replaced the concealed-construction claim with the acoustic `no pipe murmur`. | `0` |
| OP-05 | Bounded the Keeper claim to the offices' last-known condition at exile. | `-1` |

Net canonical delta: `+4`.

## Changed files

- `manuscript/chapters/chapter16-Horizon.tex`: the five authorised literal replacements only, applied by `apply_patch`.
- `notes/omega/chapter-16/round-01/production.md`: this production record, written by `apply_patch` after manuscript validation.
- No other file was written during production. No file was staged, committed, or pushed.

## Deterministic validation

- Final target SHA-256: `4A9B9A01D39CBEFA21C3B5377991E85440A0C947E396DD95191BB9671815E3E2` — exact.
- Final canonical count: `5082` — exact and inside the fixed band `4571..5585`.
- Final target size: `28983` bytes — exact.
- OP-01 through OP-05 old/new anchor counts: `0/1`, `0/1`, `0/1`, `0/1`, `0/1`.
- Target diff: exactly five hunks, in OP-01 through OP-05 order; each hunk is one removed line and its exact replacement line. No adjacent prose was reflowed or normalised.
- `git diff --check` on the target returned clean.
- Git index remained empty.

## Source and form validation

- First-person source legality is preserved: OP-01 uses named-witness report, OP-02 uses Kailan's mirror sight, OP-04 uses Kailan's hearing, and OP-05 uses his last-known evidence; OP-03 remains attributed dialogue.
- Live-room architecture remains exactly `3` `\begin{room}` and `3` `\end{room}` markers.
- Literal brace balance remains `14/14`.
- UTF-8 has no BOM; line endings remain LF-only (`537` LF, `0` CRLF, `0` bare CR).
- The exact five-hunk diff preserves the formal first-person testimony architecture, the three live-room interruptions, and the testimony-to-live-emergency turn.
- Horizon custody remains custody rather than freedom. The manual's private reading remains legal while its lessons remain supervised.
- The signed outcome, recurring drum, unresolved rising, final demand, names, relationships, motives, destinations, physical carriers, and Chapter 17 handoff remain unchanged.

## Build validation

- Producer-side build: not run. No build command or build root appears in the three authorised files, and widening the read scope for build discovery was forbidden. KingJack must perform build validation independently.
- Source-level validation completed without a rewriting, formatting, or normalising tool.

## Compliance

- Read scope was not widened beyond the three authorised files.
- Only OP-01 through OP-05 were applied, exactly and in order. No smoothing, improvisation, cleanup, punctuation pass, voice polish, rejected work, or deferred work was introduced.
- Manuscript execution changed only the target; the production record was updated only after the target reached every deterministic postcondition.
- No Git staging, commit, push, branch, or remote mutation occurred.

## Independent KingJack closure

- KingJack independently inspected the final diff and confirmed exactly five authorized one-line replacement hunks and no other manuscript movement.
- All ten fenced arbitration blocks were checked against the produced manuscript: every old block occurs zero times and every approved replacement occurs exactly once.
- Kailan remains the recoverable first-person teller. The Justice witness now supplies the upper-hearing facts; the mirror passage claims only visible separation; the house passage claims only what Kailan can hear; and the Keeper sentence is bounded to the offices' last-known condition at exile. The optics offer now permits private reading while keeping the lessons supervised.
- Final canonical count is `5082`, up `4` words (`+0.079%`) from `5078`, inside `4571..5585`. Final SHA-256 is `4A9B9A01D39CBEFA21C3B5377991E85440A0C947E396DD95191BB9671815E3E2`; final size is `28983` bytes.
- Formal name-holding, Threshold-to-well transfer, Horizon intake and second renaming, eleven-day spoken silence, Ka-Sarah/Sarah recognition, Horizon custody, supervised outside optics, signed outcome, recurring drum, and productive ambiguity remain unchanged.
- Chapter 15 cases the Knocks reel and begins the road reel; Chapter 16 remains Kailan's final formal testimony and ends in live drum pressure; Chapter 17 continues as a fully live emergency transcript. Chapters 1--15 retain their sealed hashes and no later chapter changed.
- Structural and repository checks pass: three balanced rooms, raw braces `14/14`, ten ornaments, 241 `\par` markers, UTF-8 without BOM, LF-only line endings, clean `git diff --check`, and empty Git index.
- A full `latexmk` build was independently attempted. MiKTeX exited before manuscript processing with code `-1073740791`, reporting unfinished fresh-install setup. This is an environment limitation, not a Chapter 16 LaTeX failure.
- All pre-existing Chapter 14--15, John, Omega, and ledger work remains present and unstaged. No staging, commit, or push was performed.

State: COMPLETE
