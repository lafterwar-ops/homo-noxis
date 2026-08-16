# Chapter 3 — KingJack Round 01 — Production Record

- State: `COMPLETE`
- Authoritative input: completed `arbitration.md`
- Writable by: fresh producer only
- Target: `manuscript/chapters/chapter3-Oasis.tex`

The producer may not read John, Patrick, Theo, or Chris's reports. It may apply
only accepted brief items, using the smallest sufficient movement, and may write
only this record plus files explicitly authorized by arbitration. Rejected,
deferred, ambiguous, or independently invented changes are forbidden.

## Baseline

- Pre-edit SHA-256: `D6A177F183009667264D5588D2E2A07487AA12C76E0215A7D454E9D57A84333C` — `PASS`, exact match before manuscript editing.
- Authoritative baseline count: `5,713 words`, using Unicode regex `\b[\p{L}\p{N}’'-]+\b`.
- Permitted final band: `5,142..6,284 words`.
- Local .NET/PCRE2 absolute baseline proxy: `5,711`; retained only as diagnostic metadata. The authoritative `5,713` baseline was not replaced. Signed movement was measured by applying the same local regex engine before and after the five bounded interventions.
- Baseline structure: `5/5` `room` opens/closes; `10/10` `scripture` opens/closes; `15/15` total environment opens/closes; `4` ornaments.
- Pre-edit Git index SHA-256: `9F3BDA7DE1753EDBD9702A5FC82D8A21ACA15A8125DD09EB50F86D7D9F084A39`.

## Applied interventions

Applied in the arbitration brief's exact order; after each intervention, its full containing scene was reread before proceeding.

1. **Opening oral unit — applied.** Inserted one paragraph/action-unit break between Kailan's sleepless discovery that questions are permitted and his interrogation of the moving image and watcher. No word, action, beat, speaker, or `room` boundary was added, deleted, or reordered.
2. **Beam/Oasis hinge — applied.** Kailan now states that Light gave him a beam, that the outside permission arrived before he could trace it that morning, and that the beam remained to be walked. No point, source, fall, route, location, Oasis identity, or Chapter 4 event was supplied.
3. **Access-party arithmetic — applied.** The list now parses as Kailan `(1)` + three older women `(3)`, including the woman in the grey shawl + one cloudy-eyed boy led by one of those women `(1)` + two mourning-cord workers `(2)` = `7`. No person, role, outcome, or later count changed.
4. **Balance source anchor — applied.** The clean-work finding is attributed to the Balance tally as Kailan heard it. Every tool/beast/worker category and the clean result remain unchanged; nothing new was counted or inferred institutionally.
5. **Redundant breach gloss — applied.** Deleted exactly `When Va-Sheva came back to me, nothing in her face had softened.` The preceding procedure and the following `You saw the flash first` exchange remain in their original order and wording.

## Departures

- None. All five interventions were executable without material interpretation, omission, or scope expansion.
- No deferred, rejected, forbidden, or independently invented change was made.

## Validation

- **Continuous read:** `PASS`. Revised Chapter 3 was read from first line to last after all five interventions.
- **Final governing word count:** `5,715`; signed movement `+2` from the authoritative `5,713` baseline; within `5,142..6,284`.
- **Count diagnostic:** local regex proxy moved from `5,711` to `5,713`, also `+2`; the stable engine offset was not used to replace the authoritative baseline.
- **Post-edit Chapter 3 SHA-256:** `A83F79CF92878C2EF6D09C658A56FE54E4B2E2F266F99A06469F87F9D7388086`.
- **LaTeX/environment audit:** `PASS` — `5/5` `room`, `10/10` `scripture`, `15/15` total environments, and `4` ornaments. Environment nesting/order stack completed empty with no mismatch; unescaped brace depth ended at zero and never went negative.
- **Access-party and later-count audit:** `PASS` — `1 + 3 + 1 + 2 = 7`; `Six` and `Seven bodies held` remain unchanged.
- **Beam continuity audit:** `PASS` — Chapter 3 only assigns and postpones the beam. It adds no point, source, fall, route, location, or relation to the Oasis and therefore preserves the fixed Chapter 4 handoff encoded in arbitration.
- **Payment/custody/label continuity audit:** `PASS` — microscope/swimming/pond bargain remains; the covered dish and folded grey shawl remain separately carried under Shield custody; Shield's `mirage` label remains available for Kailan's later use.
- **Source audit:** `PASS` — the oral break adds no assertion; the beam chronology is Kailan's room testimony; the party list is Kailan's first-person account; the tally anchor explicitly says `I heard`; the deletion adds no assertion. No omniscient narration was introduced.
- **Uncertainty audit:** `PASS` — flash, turned marker, pale strand, Mara, and herb remain neither objectively joined nor objectively separated. `Probably not` and `join them first and separate them later` remain unchanged.
- **Protected-content audit:** `PASS` — all `room`, `scripture`, and ornament boundaries; the Book of Blood and Genesis exchange; geography; flirtation gloss; goat beat; unidentified first `Good`; object/work/evidence custody; seven/six/seven outcome; return under shadow; bodily relief; private belief; and closing tenderness remain untouched except at the five authorized loci.
- **Exact diff audit:** `PASS` — each of the five final intervention strings matched exactly once. Reversing only those five changes in memory reproduced baseline SHA-256 `D6A177F183009667264D5588D2E2A07487AA12C76E0215A7D454E9D57A84333C`, proving manuscript movement is confined to the five authorized loci.
- **External checker note:** MiKTeX `chktex` could not run without first creating configuration outside the two-file writable scope. No setup write was permitted; the non-mutating environment-stack and brace checks above passed.
- **Full-build attempt:** `UNAVAILABLE IN CURRENT ENVIRONMENT`. `latexmk -xelatex -interaction=nonstopmode -halt-on-error` was invoked against `manuscript/00 Intro/chapter001-latexIntro.tex` with output directed to a temporary directory. MiKTeX exited before reading the manuscript (`-1073740791`) and reported that this is a fresh TeX installation whose setup must be completed. This is an environment limitation, not a manuscript diagnostic.
- **Independent continuity check:** `PASS` — Chapters 1 and 2 retain their exact post-KingJack hashes (`8925F44F...` and `318D68C1...`); Chapter 4 is clean, and its opening still asks Kailan for the assigned beam before beginning the source-to-fall tracing.
- **Independent source-legality check:** `PASS` — every revised assertion has a recoverable teller: Kailan speaks the opening and beam chronology in the room, recounts the access party in first person, and expressly grounds the clean-work conclusion in the tally he heard. No omniscient assertion was introduced.
- **`git diff --check`:** `PASS` (exit `0`) on the two authorized paths.
- **Changed-file boundary:** production wrote only `notes/omega/chapter-3/round-01/production.md` and `manuscript/chapters/chapter3-Oasis.tex`, both via `apply_patch`. No other file or manuscript chapter was written.
- **Git/index integrity:** `PASS` — no stage, commit, push, branch switch, or history rewrite was performed. Post-production index SHA-256 `9F3BDA7DE1753EDBD9702A5FC82D8A21ACA15A8125DD09EB50F86D7D9F084A39` exactly matches the pre-edit hash.

## Completion

- Package: `5/5` ordered interventions applied.
- Omissions: `0`.
- Departures: `0`.
- Final count/hash: `5,715` / `A83F79CF92878C2EF6D09C658A56FE54E4B2E2F266F99A06469F87F9D7388086`.
- State: `COMPLETE`.
