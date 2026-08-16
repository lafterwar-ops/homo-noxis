# KingJack Production — Chapter 12 — Round 02

## Inputs

- Waiting production record: `notes/omega/chapter-12/round-02/production.md`; pre-production SHA-256 `018CB82BA02C86F956626128854001BD4D2CB7ECE7F2009D28AEAE2A1202CB61`.
- Completed arbitration: `notes/omega/chapter-12/round-02/arbitration.md`; required and observed SHA-256 `1B53A0B2799158C0F59992ACABA7A1B070A274A119B07F2C13233CB05312CC57`.
- Target: `manuscript/chapters/chapter12-Confession.tex`; required and observed pre-edit SHA-256 `31E6D9C2577C599FE917A5754CBD1E0987193D9D2910E084F08B36FE92B6AFA1`.

No Round 02 trace, status file, Round 01 file, agent report, adjacent manuscript chapter, or ledger was read.

## Preconditions

- Arbitration was complete and producer-executable.
- Target strict count was exactly `3916`, using letter-or-digit tokens with internal apostrophes or hyphens retained as one word.
- Target diff was empty.
- Git index was empty.
- Target was valid UTF-8 without BOM.
- Target used LF-only line endings: `0` CR bytes.
- The old Operation 1 exchange occurred exactly once.
- The old Operation 2 passage paragraph occurred exactly once.

All preconditions passed before manuscript movement.

## Operations applied in order

1. Operation 1 replaced `Anything else in that chamber?` with `Did you remove anything else from that chamber?` and replaced `What did you remove?` with `What did you remove from beyond the first seal?`. The surrounding answers, scrap origin, custody questions, and gestures were unchanged. Strict-count delta: `+8`.
2. Operation 2 inserted exactly `A fourth warden waited on the first step and took my left side.` after `They took me through the wall niche.` No other choreography changed. Strict-count delta: `+13`.

No smoothing, gesture, adjacent grammar change, deletion, explanation, revived proposal, or later-file edit was made. Non-mechanical departures: none.

## Changed files

- `manuscript/chapters/chapter12-Confession.tex`
- `notes/omega/chapter-12/round-02/production.md`

No other file was written by this production. Nothing was staged, committed, or pushed.

## Validation

- The target diff contains only the two authorized custody-question substitutions and the one authorized fourth-warden sentence; its line-level summary is `3` additions and `3` deletions.
- The old Operation 1 block occurs `0` times and the new Operation 1 block occurs exactly once.
- The old Operation 2 block occurs `0` times and the new Operation 2 block occurs exactly once.
- Final strict count is `3937`: baseline `3916` plus `8` plus `13`; it is inside `3524..4308` with margins `413` above the floor and `371` below the ceiling.
- Final target SHA-256 is exactly `43C6819CB17C9599A72AF723F32573261A813EBB118DD0B469AEA046A051FC9B`.
- Final target remains valid UTF-8 without BOM and LF-only with `0` CR bytes.
- TeX structure passes: three `\ornament` commands; one `\begin{room}` and one `\end{room}`; `151` opening and `151` closing TeX quotation marks; `248` `\par` markers with all edited paragraphs retaining theirs; `8` opening and `8` closing braces; all named environments balanced.
- Custody scopes read as intended: the first `No` answers removal of the ribbon, the second `No` answers removal of anything else from the soundless chamber, and the scrap answers removal from beyond the first seal.
- Seizure choreography reads in order: two wardens enter through the door and a third drops from the ceiling seam; those wardens lift Kailan; a fourth visibly joins on the first step and takes his left side; the wardens later carry him over the lattice, where the existing text specifies four and retains the seat-placement actions.
- Source legality remains Kailan's first-person perception, recoverable inference, and attributed speech. The complete visible custody sequence remains ordered from robe seam and cloth through Kailan's hand, Va-Sheva's bare-edge lift, dark case, two clicks, and second belt strap to the later witnessed `Recovered before seal.` No proof handling was added.
- Reveal order is unchanged outside the scoped questions and joining sentence. The terminal room remains a single pair and its last lexical word remains `Amastan`.
- `git diff --check` passed.
- Git index remained empty after validation.

State: COMPLETE

## Independent KingJack verification

- Final strict count independently reproduced: `3937`, from baseline `3916` (`+21`; `+0.536%`), inside the fixed `3524..4308` band.
- Final SHA-256 independently reproduced: `43C6819CB17C9599A72AF723F32573261A813EBB118DD0B469AEA046A051FC9B`, exactly matching the corrected arbitration prediction.
- Both old operation blocks occur `0` times and both complete new blocks occur exactly once. The target diff contains only the three authorized substitutions (`3` added lines, `3` removed lines); no rejected, deferred or out-of-scope proposal entered production.
- Source law passes. All prose remains Kailan's sustained testimony begun in Chapter 11; the inserted fourth warden is visible to him on the first step, and the revised questions remain Va-Sheva's attributed speech. No external camera, hidden motive or inaccessible fact was added.
- Custody scope passes. The first `No` denies removing part of the ribbon; the second denies removing anything else from the soundless chamber; the scrap answer is explicitly scoped to what Kailan removed from beyond the first seal. The physical chain from robe seam and cloth through Kailan's hand, Va-Sheva's bare-edge lift, dark case, two clicks, second strap and later `Recovered before seal` remains unchanged.
- Choreography passes: two wardens enter through the door, a third drops from the ceiling seam, those wardens lift Kailan, a fourth visibly joins on the first step and takes his left side, and the existing four wardens later carry him across the lattice and place him at the seat.
- Form passes: `room` begins/ends `1/1`; all environments begin/end `1/1`; ornaments `3`; paragraph markers `248`; TeX quotation marks `151/151`; valid UTF-8 without BOM and LF-only line endings retained.
- Frozen incoming canon passes. Chapters 1–11 retain their recorded hashes, including Chapter 11 `A708FBD3F682A01978FE9E8D572A8BEC632A76FEC0B38F0E1A05FA678F1E9FEC`.
- Boundary continuity passes. Chapter 11 tells Kailan to begin at the door chosen while carrying Sarah's record; Chapter 12 opens with that record against his ribs. Chapter 12 ends on `Amastan`; clean Chapter 13 `chapter13-Infiltration.tex`, SHA-256 `9B5CEABE28E155797D4D3949A2C8ADC28B30D67A19D6C037C6AE41F8C53B18CA`, immediately resumes with Sarah giving Amastan whole.
- Completed Chapter 12 Round 01 remains immutable at its preflight hashes. No earlier round file was edited or used as arbitration evidence.
- No later manuscript file was authorized or changed. Trial, proof disposition, Sarah's offer, Va-Sheva's history and the compromised testimony room remain forward story pressures rather than Round 02 production obligations.
- `git diff --check` passes; the Git index is empty. Pre-existing Chapter 10–11 work was preserved. Nothing was staged, committed or pushed.
- Full compilation was attempted from `manuscript/00 Intro/chapter001-latexIntro.tex`; `latexmk` exited before manuscript processing because MiKTeX reports a fresh installation whose setup must be finished.

Independent verification: COMPLETE
