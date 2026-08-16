# KingJack Production — Chapter 8 — Round 01

## Authority and scope

- Phase: constrained production under the completed `arbitration.md` brief.
- Read set used: `.codex/skills/kingjack/SKILL.md`, this production record, completed `arbitration.md`, and `manuscript/chapters/chapter8-Light.tex` only.
- Contributor reports, KingJack status, other rounds, agent/John statuses, other chapters, ledgers, and diagnoses were not read.
- Authorized write set: this record and `manuscript/chapters/chapter8-Light.tex` only.
- No staging, commit, push, adjacent-chapter edit, or other manuscript movement was authorized or performed.

## Baseline and preconditions

- Locked target SHA-256: `C6E9BE6CB82DCD77C01D537E86515F957FF41E4F35D55414F3413CB4716BC483`; verified before editing.
- Strict Unicode count and method: `3227`, counted with `\b[\w’'-]+\b` under Unicode matching.
- Fixed permitted band: `2904..3550`.
- Encoding and line endings: UTF-8 without BOM; 157 LF line endings, no CRLF or bare CR.
- Exact old anchor `Something moved within the dome.` occurred once; the replacement anchor did not yet occur.
- Target working-tree diff was empty before editing.
- All seven pre-existing working-tree entries were inside `notes/omega/chapter-8/round-01/`; no entry existed outside that exact round directory.
- Git index was empty.
- Arbitration state was `COMPLETE` and supplied one exact operation with no interpretive choice.

## Applied operation

At the unique line-117 locus, through `apply_patch`, replaced exactly:

`Something moved within the dome.`

with:

`I heard something move within the dome.`

No adjacent character, whitespace, punctuation, line ending, encoding, sentence, or second prose locus changed.

Departure from the executable brief: none.

## Exact changed files

- `manuscript/chapters/chapter8-Light.tex`: the single authorized sentence replacement.
- `notes/omega/chapter-8/round-01/production.md`: this administrative completion record.

No other file was changed by the producer.

## Counts and hashes

- Strict count: `3227 -> 3229` (`+2`), within fixed band `2904..3550`.
- SHA-256: `C6E9BE6CB82DCD77C01D537E86515F957FF41E4F35D55414F3413CB4716BC483 -> C9A88C9516A5CAE06437465FA23178CE6617924FB56A2DB5B29372BC284C2A29`.
- Byte movement: `+7`; final target is the exact baseline-byte transformation predicted by arbitration.

## Validation

- Complete target reread after the patch: passed.
- Scope: exactly one diff hunk at line 117; the tracked working-tree diff names only `manuscript/chapters/chapter8-Light.tex`; all other working-tree entries remain confined to the exact round directory.
- Anchor: old string occurs `0` times; new string occurs `1` time.
- Source: Kailan is now the explicit teller and hearing is the explicit sensory source in his continuing account to Paul.
- Hidden act: the mover, act, motive, consent, and private exchange remain unidentified; the sentence adds no witnessed action or external camera.
- Room continuity: both room environments, speaker order, exits into Kailan's testimony, and interview framing are unchanged.
- Frozen architecture: both Ascensions, Syphiron's death, Raedin's succession, titles, chronology, custody chains, Pendulum behavior and wording, light/dark sequence, scripture order, blaze, aftermath, five-door interval, transitions, and black-water ending are byte-identical to baseline outside the authorized replacement.
- Form counts: `room` 2 begin / 2 end; `scripture` 5 begin / 5 end; ornaments `8`; `\par` markers `40`; all unchanged.
- Encoding and line endings: UTF-8 without BOM; 157 LF line endings, no CRLF or bare CR; unchanged.
- `git diff --check`: passed.
- Git index: empty after production; untouched.
- Full LaTeX build: not run because locating its configured entry point would exceed the producer's authorized read scope; independent KingJack verification is responsible for that gate.
- Stage / commit / push: none.

State: COMPLETE

## Independent KingJack verification

- Final strict UTF-8 count: `3229`, against baseline `3227`; net movement `+2` words (`+0.062%`) and within the fixed band `2904..3550`: `PASS`.
- Final SHA-256: `C9A88C9516A5CAE06437465FA23178CE6617924FB56A2DB5B29372BC284C2A29`, exactly matching the independently simulated prediction: `PASS`.
- Exact manuscript scope: one authorized one-line substitution (`1` insertion / `1` deletion); the old anchor is absent and the new anchor occurs once: `PASS`.
- Arbitration scope: no deferred room-light operator, Pendulum clarification, rejected compression, new reaction, mechanism, explanation, or other unauthorized operation entered production: `PASS`.
- Teller/source audit: the opening room explicitly transfers the telling to Kailan; `I heard` makes both teller and sensory route recoverable inside total darkness while leaving mover, act, motive, consent, and private exchange unknown. No external camera or omniscient assertion entered: `PASS`.
- Room/form audit: both `room` exits still resume Kailan's established continuous testimony; `room` `2/2`, `scripture` `5/5`, total `\\begin` / `\\end` `7/7`, ornaments `8`, and paragraph markers `40`: `PASS`.
- Canon/custody audit: both Ascensions, Syphiron's death, Raedin's succession, cloths, flame, knife, blood, Pendulum, ceremonial sequence, five doors, washing, and black-water ending remain unchanged: `PASS`.
- Backward-continuity audit: Chapters 1-7 retain their locked hashes. Chapter 7's double-Ascension handoff remains coherent: `PASS`.
- Forward-transition audit: Chapter 9 is clean at SHA-256 `DA4118F4BEDE4B6217AA52B725BBDC1A414237CAC931CBBE3788CB9ACE7DD3F6`; its later `I heard the sound under the stone` now has an even clearer Chapter 8 perceptual basis: `PASS`.
- Full-build attempt: `ENVIRONMENT BLOCKED`, not a manuscript failure. `latexmk` exits `-1073740791` before manuscript processing because MiKTeX reports a fresh installation whose setup has not been completed.
- The working tree contains only the authorized Chapter 8 manuscript change and this round directory; no external or overlapping edit appeared.
- `git diff --check`: `PASS`; Git index: empty; stage / commit / push: none / none / none.

Independent verification: COMPLETE
