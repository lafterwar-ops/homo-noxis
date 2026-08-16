# KingJack Production — Chapter 10 — Round 01

- Inputs read: this production record, completed `arbitration.md`, and `manuscript/chapters/chapter10-Threshold.tex`
- Contributor reports: not read
- Authorized write set: this production record and `manuscript/chapters/chapter10-Threshold.tex`
- Git actions: no stage, commit, or push

## Baseline and preconditions

- Target: `manuscript/chapters/chapter10-Threshold.tex`
- Baseline SHA-256: `E42DE9F7C67FE4AFB3A2F286E955ECC2536481D378728533E638150EDBE906B5`
- Baseline strict count: `6336`, using `[A-Za-z0-9]+(?:[-'’][A-Za-z0-9]+)*`
- Fixed permitted band: `5702..6970`
- Pre-edit target-scoped diff: empty
- Pre-edit Git index: empty
- Unique-anchor gate: each of the three exact old strings occurred once
- Arbitration state: `COMPLETE`; production authority was exact and unambiguous

All preconditions passed before manuscript movement.

## Applied operations

1. Deleted only `In those files, every outside question reached the Blackwood Foundation before it reached the people named beneath the tree.` The existing separator space and `\par` remained, and the next paragraph still begins `One thin file began...`.
2. Replaced only `Before I touched the door, the packet had been sealed, the exterior clothes laid ready and the lamp lit.` with `The sealed packet, the exterior clothes and the warm lamp made me believe he had been prepared for the desert before I touched the door.`
3. Replaced only `When I opened the outer stone` with `When I opened the stone behind the polished plate`.

The operations were applied in the ordered brief sequence. No smoothing, synonym pass, new gesture, new source, new geography, or adjacent grammatical change was made.

## Changed files

- `manuscript/chapters/chapter10-Threshold.tex`: three accepted manuscript operations
- `notes/omega/chapter-10/round-01/production.md`: this production audit record

No other file was written by the producer. Pre-existing external/user work was left untouched.

## Counts and hashes

- Strict count: `6336 -> 6326` (`-10`), within `5702..6970`
- Byte count: `35260 -> 35188` (`-72`)
- Final SHA-256: `AF207B08D340BF3CFD637D11A15F852849DB8C2E4598BDF382EF458E3A49E3BB`
- Target diff: exactly three hunks, three removed lines, and three added lines; the one exact sentence deletion and two exact replacements only

## Departures

None. Final wording, spacing, paragraph join, line endings, encoding, count, byte movement, and hash match the arbitration brief.

## Validation

- The final target was reread in full after production.
- Narrator/address remain legal: the two room environments remain direct dialogue, and the intervening account remains Kailan's testimony to Paul.
- Source law remains legal: `made me believe` marks the warden-preparation timing as Kailan's bounded inference from the sealed packet, exterior clothing, warm lamp, dust, warning tongue, reset, wall answer, and response interval. No omniscient certification or external camera was added.
- Route geography remains recoverable and unchanged except for the authorized recurrence anchor: the polished-plate relation is recalled on the archive-to-desert return, while the later `shaved edge` and `slab` closure remains intact.
- Frozen plot, two-room form, outcome, chronology, revelation order, productive ambiguities, and adjacent transitions remain unchanged. April 2 still hands off to tomorrow / Good Friday / Sarah.
- Custody remains unchanged: the altered lens is returned, the torn strip is taken, the ribbon remains in blood, the field packet remains with the warden, the camera card is collected, and the photograph is shown to Paul.
- LaTeX mechanics: `room` begins/ends `2/2`; ornaments `4`; paragraph markers `94`; dialogue quote pairs `12/12`; unescaped braces `22/22`.
- `git diff --check` passed for the target.
- Git index remained empty. Nothing was staged, committed, or pushed.
- Full manuscript compilation was not run: the configured entry point is outside this producer's authorized readable inputs and is left to the independent KingJack Phase 5 verifier.

State: COMPLETE

## Independent KingJack verification

- Final strict count independently reproduced: `6326`, from baseline `6336` (`-10`; `-0.158%`), inside the fixed `5702..6970` band.
- Final SHA-256 independently reproduced: `AF207B08D340BF3CFD637D11A15F852849DB8C2E4598BDF382EF458E3A49E3BB`, exactly matching the arbitration prediction.
- The manuscript diff contains exactly the three authorized hunks (`3` insertions, `3` deletions). No rejected or deferred proposal entered the text.
- Source law passes. Between the two room transcripts, Kailan remains the recoverable teller addressing Paul. The Blackwood deletion adds no assertion; `made me believe` explicitly bounds the warden-preparation claim as Kailan's inference from witnessed objects; and the polished-plate route anchor names geography Kailan traversed and observed.
- Custody passes unchanged: the altered lens is returned; Kailan retains the torn strip; the ribbon stays in blood; the sealed packet remains with the warden; Martinez removes the camera card; and Paul retains the photograph for Sarah's arrival.
- Form passes: `room` begins/ends `2/2`; all environments begin/end `2/2`; ornaments `4`; paragraph markers `94`; centreline `1`.
- Frozen incoming canon passes. Chapters 1--9 retain their recorded hashes: Chapter 1 `8925F44F291EC8F6F0C207808DCFA06843E46C947609A7D34D33F8C1AB614C61`; Chapter 2 `318D68C183889E5C61958BD55FBFCEE5A911592EB59E92C5A27FEDA5CE410011`; Chapter 3 `A83F79CF92878C2EF6D09C658A56FE54E4B2E2F266F99A06469F87F9D7388086`; Chapter 4 `4AFD2C89E87D3C831BDF8CD48051F9F113F47200591BD60EBE1B4730D21FB435`; Chapter 5 `65D05BD1A4D6B8654B2CB8DB77B9F073639C3B2874211545127E614C75C4FE92`; Chapter 6 `9EA2B58766913DD733D947802B90879647F17D9F5A924FF7D6BA43A21445944A`; Chapter 7 `585CF5365D93E3A8AFB9A1A85298AF9C32FC6064B1C06249A3AE8C310185DA53`; Chapter 8 `C9A88C9516A5CAE06437465FA23178CE6617924FB56A2DB5B29372BC284C2A29`; Chapter 9 `5DA93308992FE9C5EE88A87B168B4C40D7A60C2BF3F3BCB22B88F6F10C8239BE`.
- Boundary continuity passes. Chapter 9 hands Kailan the Pendulum problem; Chapter 10 opens by returning to that account. Chapter 10 promises Sarah's Good Friday arrival; clean Chapter 11 SHA-256 `A12B873CCA5AF35FCDD3CA1D6130D9EC323960AA2391AB2A79522F5E5CA6BFCC` opens on April 3 with Sarah joining the recorded interview.
- `git diff --check` passes; the Git index is empty. No stage, commit, or push was performed.
- During brainstorming, an external/user process normalized and committed previously dirty work outside this round. Chapter 10 remained at its baseline hash until authorized production, the reports remained firewalled, and this KingJack round performed no Git action.
- Full compilation was attempted from `manuscript/00 Intro/chapter001-latexIntro.tex`; `latexmk` exited before manuscript processing because MiKTeX reports a fresh installation whose setup must be finished.

Independent verification: COMPLETE
