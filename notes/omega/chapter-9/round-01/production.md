# KingJack Production — Chapter 9 — Round 01

## Baseline and preconditions

- Target: `manuscript/chapters/chapter9-Heaven.tex`.
- Baseline SHA-256: `DA4118F4BEDE4B6217AA52B725BBDC1A414237CAC931CBBE3788CB9ACE7DD3F6`.
- Strict count: `4753`, using `.NET` regex `\b[\p{L}\p{N}]+(?:['’\-][\p{L}\p{N}]+)*\b` over the exact UTF-8 target text.
- Fixed permitted band: `4277..5229`.
- The target working-tree diff was empty before production.
- Operation 1 old anchor occurrences before production: exactly `1`.
- Operation 2 old anchor occurrences before production: exactly `1`.
- Git index before production: empty.
- Unrelated unstaged and untracked work existed outside the authorised write set. It was treated as external work and left untouched.
- Arbitration state: `COMPLETE` and mechanically executable; no interpretation was required.

## Operations applied in order

1. Replaced exactly `When the cold had dried our faces enough for speech, Ka-Raedin told me what the place was for.\par` with `When the cold had dried our faces enough for speech, Ka-Raedin spoke.\par`. The following `Every Light that ever rose...` quotation and paragraph boundary are byte-for-byte unchanged.
2. Replaced exactly `At the foot of the shaft he put his hand flat on the cold stone.` with `The next day, at the foot of the shaft he put his hand flat on the cold stone.`. The remainder of the paragraph and preceding `Come down tomorrow.` remain unchanged.

## Changed files

- `manuscript/chapters/chapter9-Heaven.tex`: the two authorised one-line substitutions only.
- `notes/omega/chapter-9/round-01/production.md`: this process record.
- No other file was written by this producer.

## Movement and hashes

- Final strict count: `4750` (`-3`), inside `4277..5229`.
- Final SHA-256: `5DA93308992FE9C5EE88A87B168B4C40D7A60C2BF3F3BCB22B88F6F10C8239BE`.
- Baseline bytes: `24722`; final bytes: `24711`; actual movement: `-11` bytes.
- Reverse-substituting only the two authorised final anchors reconstructs baseline SHA-256 `DA4118F4BEDE4B6217AA52B725BBDC1A414237CAC931CBBE3788CB9ACE7DD3F6` and baseline strict count `4753`.

## Departures

- Editorial or textual departures from the ordered brief: none.
- Mechanical forecast note: arbitration projected `-12` bytes, while the exact applied replacements produce `-11` bytes. The required final count, required final SHA-256, reconstructed baseline SHA-256, and exact two-hunk diff all match, so no compensating edit was made.

## Validation

- Re-read the complete final target.
- Exact scope: comparing the final target with its reverse-reconstructed baseline yields changed lines `94` and `162` only; `git diff --numstat` is `2` additions and `2` deletions, and the diff contains only the two authorised replacements.
- Teller and source remain legal: Va-Kailan remains the continuous first-person teller; Ka-Raedin remains the identified remembered speaker at Operation 1; Operation 2 remains Va-Kailan's witnessed chronology.
- Chronology remains intact: `Come down tomorrow.` is followed by `The next day`; no travel, meeting, action, or same-night implication was added.
- Cup custody remains intact across the cut: Ka-Raedin wraps both cups and returns them to his robe before the next-day sentence; no custody transfer was added.
- Frozen room, plot, scientific observations and uncertainty markers, institutional knowledge boundaries, productive ambiguity, and final Pendulum sentence are unchanged. The first and final lines are unchanged.
- Form checks: `room` begin/end `1/1`; dialogue opens/closes `56/56`; braces `5/5`; `\par` count `85`, unchanged; LaTeX environment names pair as `room`/`room`.
- Target-scoped `git diff --check` passes.
- All pre-existing unrelated paths remained untouched. Concurrent unrelated untracked Chapter 14 round files appeared during validation and were also left untouched.
- Git index after production: empty.
- Full manuscript build not run: its configured entry point lies outside this constrained producer's readable inputs. Independent KingJack retains that verification.
- No staging, commit, or push occurred.

State: COMPLETE

## Independent KingJack verification

- Final strict UTF-8 count: `4750`, against baseline `4753`; net movement `-3` words (`-0.063%`) and within the fixed band `4277..5229`: `PASS`.
- Final SHA-256: `5DA93308992FE9C5EE88A87B168B4C40D7A60C2BF3F3BCB22B88F6F10C8239BE`, exactly matching the independently simulated prediction: `PASS`.
- Exact manuscript scope: two authorized one-line substitutions (`2` insertions / `2` deletions); both old anchors are absent and both new anchors occur once: `PASS`.
- Arbitration scope: no deferred catalogue/voice compression, rejected wave-wall exit, new event, new reaction, scientific deletion, Pendulum answer, or other unauthorized operation entered production: `PASS`.
- Teller/source audit: Va-Kailan remains the continuous teller after the room; Ka-Raedin remains the named remembered speaker before his byte-identical quotation; `The next day` is Va-Kailan's witnessed chronology. No omniscient or unowned assertion entered: `PASS`.
- Chronology/custody audit: `Come down tomorrow` now cuts explicitly to the next day; Ka-Raedin wraps both cups and returns them to his robe before the cut, and no travel, meeting, action, or custody transfer is invented: `PASS`.
- Form audit: `room` `1/1`, total `\\begin` / `\\end` `1/1`, paragraph markers `85`, and all opening/final text outside the two loci unchanged: `PASS`.
- Backward-continuity audit: Chapters 1-8 retain their locked hashes. Chapter 8's martyrdom and succession flow coherently into Chapter 9: `PASS`.
- Forward-transition audit: Chapter 10 is clean at SHA-256 `E42DE9F7C67FE4AFB3A2F286E955ECC2536481D378728533E638150EDBE906B5`; its Pendulum problem follows Chapter 9's withheld question coherently: `PASS`.
- Full-build attempt: `ENVIRONMENT BLOCKED`, not a manuscript failure. `latexmk` exits `-1073740791` before manuscript processing because MiKTeX reports a fresh installation whose setup has not been completed.
- External work in `ADDITION`, Chapter 13, Chapter 14 Omega, Chapter 8 Omega/manuscript, and Zeus remained outside the authorized scope and untouched. The external disappearance of the temporary `ADDITION/Resources/~$DDITION_revised (1).docx` path was observed but not caused or acted upon by this round.
- `git diff --check`: `PASS`; Git index: empty; stage / commit / push: none / none / none.

Independent verification: COMPLETE
