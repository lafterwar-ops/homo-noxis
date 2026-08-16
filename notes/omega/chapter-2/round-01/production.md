# Chapter 2 — KingJack Round 01 — Production Record

- State: `COMPLETE`
- Authoritative input: completed `arbitration.md`
- Writable by: fresh producer only

The producer may not read John, Patrick, Theo, or Chris's reports. It may apply
only accepted brief items, using the smallest sufficient movement, and may write
only this record plus files explicitly authorized by arbitration. Rejected,
deferred, ambiguous, or independently invented changes are forbidden.

## Baseline

- Target: `manuscript/chapters/chapter2-Mirror.tex`
- Verified pre-edit SHA-256: `2C1101DA9C08E798E7E8D14CBCEAC9DB24CC411C1974405FEC34254C1026938D`
- Locked canonical count: `4185` words, using Unicode regex `\b[\p{L}\p{N}’'-]+\b`
- Permitted final band: `3767..4603` words inclusive
- Chapter 1 and Chapter 3 are encoded read-only continuity constraints; neither is authorised for editing.
- Teller/source rule: first-person retrospective testimony and identified room speech remain the only narrative modes; every assertion must be recoverable to Kailan's senses, memory, explicit inference, a named speaker, direct instruction, or a visible/identified record.
- Authorised ordered operations: (1) clarify the existing three-door left/middle/right stage picture; (2) remove only the water lesson's final generalisation; (3) remove only the black-panel lesson's abstract taxonomy; (4) reorder the existing Faith evidence so the question precedes the physical answer; (5) correct the hand-mirror eye-line and return the strip to its niche; (6) remove the single redundant Mirror abstraction.

## Applied interventions

1. **Three-door spatial repair:** At `Three doorways stood at the far end`, mapped the existing apparent facades explicitly as left open/dark with base light, middle metal-closed, and right half-open with reflected brightness. At Kailan's attempt, identified the pushed and pulled surface as the left-hand facade. The worn circle, unoffered rear panel, premature entry, outcomes, and lesson are unchanged.
2. **Water proof compression:** At `Better. He watched the point tremble on the wall.`, removed only the final `Young minds love to turn traces into stories` generalisation. The trembling point and the distinction among disturbance, surviving trace, and unknown causal identity remain.
3. **Black-panel proof compression:** At `That is what a Keeper of Light does. I am a Veil.`, removed only the abstract `Light is a condition` taxonomy. The rank hinge, Va-Raedin's bodily occlusion, wrong-lamp maxim, Kailan's challenge, and Va-Raedin's answer remain.
4. **Faith revelation-order repair:** At `A passage overlooked a lower work hall`, delayed identification of the holes and hidden lamp until after `What do you see?`, Kailan's unchanged first explicit inference, and `Ask where the air enters.` The rail pressure, mist/singer synchrony, fine holes, placed light, raised hands, thickening mist, delayed stone response, nod, and the complete knowledge/belief exchange remain in their authorised order.
5. **Hand-mirror eye-line and custody:** At `He turned the glass`, changed the reflection so Va-Raedin's face displaces Kailan's after Kailan first sees his own. Immediately before `Come`, returned the same plain strip to its source niche without explanation.
6. **Mirror abstraction cut:** At `The wall followed the Mountain. Now the Mountain follows the wall.`, deleted only `It is the map that precedes the territory.` `Watch` and every subsequent observation, limitation, consequence, count, judgment, and silence remain.

## Departures

- None. The six operations were executed in the authorised order with no materially interpreted, broadened, deferred, rejected, or independently invented intervention.

## Validation

- **Final target:** canonical Unicode-regex count `4174`; net movement `-11` words from the locked `4185`; within the inclusive `3767..4603` band. Final SHA-256: `318D68C183889E5C61958BD55FBFCEE5A911592EB59E92C5A27FEDA5CE410011`.
- **Full-read audit:** Read the complete resulting Chapter 2 after the interventions and checked spatial continuity, cadence, source legality, and all six changed loci against the authoritative brief.
- **Source audit:** All narration remains Kailan's first-person retrospective testimony and all framed speech remains identified room speech. The only added assertions are visible spatial relations/actions available to Kailan: facade positions, the left facade he handles, the delayed location of existing holes and placed lamp, the corrected reflected face, and Va-Raedin's return of the strip. No motive, belief, operator, technical identity, or omniscient fact was added.
- **Continuity audit:** Chapter 1 and Chapter 3 were not opened; their constraints were audited from the authoritative arbitration encoding. Sa-Kailan's name, cut and bandage, Second Silence, hunger, pride, rank formulae, Pendulum, knowledge division, recorder frame, and concealed Paul/Sarah inference remain unchanged. The token remains in Kailan's custody, the thumb remains bandaged, and placed-light suspicion, sea desire, swimming/diving request, microscope/direct-proof demand, and the second outside passage retain their Chapter 3 handoff. Plot, room order, exercise outcomes, token morphology, Paul's print and silence, Faith ambiguity, Mirror limits, compartmentalisation, boat/strait/Isfahan facts, and the book/sea ending remain unchanged.
- **Form and LaTeX audit:** `room` environments begin/end `7/7`; `center` begins/ends `1/1`; all detected environments balance (`room=7/7`, `center=1/1`); raw LaTeX braces balance `49/49`; `\ornament` count is `4`; `\centerline` count is `3`. All environment order, language labels, centred delays/location, and ornament placements remain intact.
- **Scoped-diff audit:** The manuscript diff contains only the six authorised anchor loci: the two local three-door clarifications; water final-sentence deletion; black-panel taxonomy deletion; two-line Faith evidence reorder; hand-mirror pronoun correction plus strip return; and the single Mirror sentence deletion. Tracked manuscript movement is `10` added lines / `8` deleted lines, and `git diff --check` returned `0` for the two authorised paths.
- **Changed-file boundary:** This production pass wrote only `manuscript/chapters/chapter2-Mirror.tex` and this `notes/omega/chapter-2/round-01/production.md`, both via `apply_patch`. Scoped status is modified manuscript plus untracked production record; no other path was written.
- **Independent full-manuscript build attempt:** unavailable for environmental
  reasons. `latexmk -xelatex` stopped before reading the manuscript because the
  local MiKTeX installation reports that its initial setup is unfinished. This
  is not a manuscript compilation error; no generated workspace artefact was
  created.
- **Index integrity:** A scoped cached-diff check returned `0` (no staged changes to either authorised path). Nothing was staged, committed, pushed, branched, or otherwise written to the Git index/history/remotes.

## Completion

The completed arbitration brief has been executed exactly and production stops
here. No general polish pass was performed. All available validation gates pass;
the only unavailable gate is the environmentally blocked full build recorded
above.
