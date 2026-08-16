# Chapter 21 — Production Record

- State: `COMPLETE`
- Authoritative brief: `arbitration.md` → **Production brief**
- Writable by: producer only

## Production contract

The producer may read the current Chapter 21 and the completed arbitration file.
It must not read the Patrick, Theo, or Chris reports: their competing proposals
have already been adjudicated. The producer applies only accepted interventions,
using the smallest sufficient textual movement, and does not reopen arbitration.

The producer must preserve every invariant in the arbitration file, keep Chapter
21 within ten percent of its pre-production word count, validate mechanical
integrity, and leave the Git index untouched. It must never commit or push.

## Baseline

- Target: `manuscript/chapters/chapter21-Vigil.tex`
- Pre-production SHA-256: `BD6E16BB78AA04683F375BF0A5B9C3038A61B3F19AA85F35495F441F59F34E3D` (confirmed before editing).
- Local regex word count: `5133`, using `[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*` (confirmed before editing).
- Manuscript target was clean before production. The production record was already untracked.
- Git index before production: clean (`git diff --cached --quiet` exit `0`), SHA-256 `9F3BDA7DE1753EDBD9702A5FC82D8A21ACA15A8125DD09EB50F86D7D9F084A39`.

## Applied interventions

Applied in the arbitration brief's order, with no other manuscript sentence changed:

1. Retained `No charge came after that.` and deleted only the following burial restatement.
2. Revised the next paragraph's opening to `Already dead, Jean-Charles did not enter the living count for those first four days.` This makes death and the count/record sense explicit without changing cause, time, place, later disclosure, or final action.
3. Deleted only the final anticipatory-ration sentence from the water-listener/Ka-Cheryn paragraph; added no replacement.
4. Deleted the standalone `That frightened me.` and the clause `and showed her where my fear had gone to live`; retained the names, the single explicit comparison, Sela's listening, avowal, first kiss, and day-ninety destination.
5. Inserted `The six stones remained on the table.` between `Ka-Leth entered it.` and `The audit continued for four days.` The beat is physical, uninterpretive, and introduces no evidence.

## Departures from brief

None. All five interventions follow the ordered brief exactly; no rejected or deferred intervention was performed.

## Validation

- Read every changed paragraph with its preceding and following paragraph. Kailan remains the recoverable narrator; source custody, addressees, object custody, subjects, and transitions remain clear.
- Re-read the complete name-strip unit. Exactly one explicit diagnosis of the seventeen/millions disparity remains. Kailan still reads the seventeen names; Sela still listens without mending, makes her avowal, kisses first, and reaches the mutual day-ninety destination.
- Re-read the audit from the nine stones through the operational finding. Nine are placed; camera, copied-reel, and car-transfer stones are removed; six remain. The recurrence leaves those six on the table after the admission and does not attach the three exclusions to it. Camera ownership, ordering hand, recipient, purpose, orders, time of understanding, motive, and Va-Sheva's other question remain outside proof or unanswered.
- Checked the first Jean-Charles transition against the later audit ending. He is already dead in the living count and still dies holding the inner leaf; no cause, time, place, intermediate status, or delayed disclosure was altered.
- Path-limited manuscript diff contains exactly the five ordered changes and no rejected or deferred change.
- `git diff --check -- manuscript/chapters/chapter21-Vigil.tex`: clean (exit `0`).
- TeX braces: balanced (final depth `0`, minimum depth `0`). Dialogue quotes: `53` opening and `53` closing pairs, in sequence with `0` pairing errors. Ornament markers: `5`.
- Post-production local regex word count: `5106`, a net contraction of `27` words (`-0.526%`), within the ten-percent limit. Post-production manuscript SHA-256: `CA690DCA0F36271F6B4A305390ED4A79C7D3C57533010C003804D6E79FFAB676`.
- Git index after manuscript production remained clean (`git diff --cached --quiet` exit `0`) and its SHA-256 remained `9F3BDA7DE1753EDBD9702A5FC82D8A21ACA15A8125DD09EB50F86D7D9F084A39`. Nothing was staged, committed, or pushed. No file outside the two authorized production targets was changed by the producer.

## Completion

Production is complete. The manuscript contains exactly the five accepted interventions, every stated invariant is preserved, and the Git index is untouched.
