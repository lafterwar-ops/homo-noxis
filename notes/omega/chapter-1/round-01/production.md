# Chapter 1 — KingJack Round 01 — Production Record

- State: `COMPLETE`
- Authoritative input: completed `arbitration.md`
- Production mode: fresh constrained producer; three authorized loci only
- Git: nothing staged, committed, or pushed

## Baseline

- Manuscript: `manuscript/chapters/chapter1-Ascension.tex`
- SHA-256: `6A9404FE2EF85D3723679F5FBCF7EF34251DBC8B253FB3E27CC55D6565FC042A`
- Baseline verification: exact match before the first intervention
- Authoritative count: `W0 = 5,069`, using Unicode regex
  `\b[\p{L}\p{N}’'-]+\b`
- Permitted final band: `4,563..5,575`

## Applied interventions

Applied in the brief's order, with no intervening manuscript work:

1. **Opening Noxius room — recorder referent.** Replaced Kailan's unsupported
   `this` with `this machine` inside the existing question. No gesture, action,
   prop, turn, credential, or explanation was added; Paul's answer and the
   mutual-disbelief exchange remain substantively unchanged.
2. **Hall/Pendulum orientation — measurement provenance.** Added the minimal
   first-person retrospective attribution `I later learned that` to the one
   sentence containing the Pendulum's `a hundred and twenty-five metres` drop
   and `five metres and more` lateral travel. Both quantities and all protected
   mechanics remain unchanged; the sentence does not claim that fifteen-year-old
   Kailan measured them.
3. **Final monitoring room — bounded inference pass.** Kept Paul's readiness
   question tentative; made Blackwood own the answer as inference; retained
   `readiness test` once; removed the two bare `Yes` turns; folded the gates'
   timing into Paul's evidence turn; and marked whole-Earth mode as Paul's
   working hypothesis and planetary coupling as Blackwood's possible inference.
   Keeper-change recurrence, five sources, return, source schedule,
   fifth-interval prediction, gate meaning, whole-Earth mode, and possible
   coupling each remain once. No adjacent material changed.

## Departures

- None. No brief item required scope expansion or material interpretation.
- No rejected, deferred, out-of-scope, structural, staging, lore, continuity,
  or general-polish change was attempted.

## Source audit

- **Recorder question:** teller Kailan; addressee Paul; acquisition path Kailan's
  immediate perception of the already-present machine. The change identifies a
  referent and adds no factual claim about its operation.
- **Pendulum measurements:** teller Kailan; addressee Paul; acquisition path
  Kailan's explicit later learning. The hundred-and-twenty-five-metre drop and
  five-metres-and-more travel are therefore retrospective knowledge, while the
  disk's appearance and motion remain his witnessed perception.
- **Readiness and schedule:** teller Blackwood; addressee Paul; acquisition path
  expert inference from Paul's elicited count and interval together with her
  named Reggane trace. The Keeper-change recurrence, five sources, return,
  source schedule, and fifth-interval prediction remain owned inference.
- **Gates:** teller Paul; addressee Blackwood; acquisition path Kailan's account
  as elicited by Paul, followed by Paul's professional inference about what the
  return means to the institution.
- **Whole-Earth mode:** teller Paul; addressee Blackwood; acquisition path his
  professional working hypothesis from Kailan's account and Blackwood's trace.
- **Possible coupling:** teller Blackwood; addressee Paul; acquisition path her
  expert hypothesis from the same independent trace-and-testimony comparison.
  `may be coupled` leaves the mechanism and conclusion unsettled.

## Validation

- Final authoritative count: `W1 = 5,083`; net movement: `+14` words. The result
  is inside `4,563..5,575` and remains essentially word-neutral.
- Final manuscript SHA-256:
  `8925F44F291EC8F6F0C207808DCFA06843E46C947609A7D34D33F8C1AB614C61`.
- Changed-file boundary: the producer wrote only this production record and the
  authorized Chapter 1 manuscript, both through `apply_patch`. No other path was
  written, generated, renamed, or moved. The manuscript diff contains exactly
  three hunks, one at each authorized locus, with no opportunistic cleanup.
  Target-limited `git status --short` reports only `M` for the manuscript and
  `??` for this previously untracked production record; neither has an index
  status.
- `git diff --check -- manuscript/chapters/chapter1-Ascension.tex`: exit `0`;
  no whitespace errors.
- LaTeX/environment counts are balanced and unchanged: `center 2/2`,
  `room 7/7`, `scripture 6/6`. The diff adds, removes, moves, or renames no
  environment. The chapter title, two named locations, transcript form,
  language labels, plot events, outcomes, and present characters are unchanged.
- Complete revised-chapter read: passed. The Hall is lived before technical
  reclassification. The ladder remains Kailan's observation/later learning ->
  Paul's elicitation -> Blackwood's independent trace -> Paul/Blackwood
  hypothesis. Kailan receives neither the Reggane account nor the coupling
  inference.
- Protected facts/outcomes: passed. Faith transfers from living Mereth to Elun;
  Kailan becomes Sa-Kailan of Light; Shield bars then releases the gates; five
  equal hard strokes occur; the next equal interval contains a different broad
  return; all five Keepers return before the gates open; Reggane remains dated
  `1960` and carried for sixty-six years; Blackwood orders secrecy, continued
  non-leading testimony, recovery of the trial and exile, and gaining Kailan's
  trust.
- Ambiguity: passed. No mechanism beneath the Bowl, Temple, Mountain, sources,
  return, or Chains is certified; no one-to-one five-source/five-office mapping
  is asserted; planetary coupling remains an owned expert hypothesis.
- Independent full-manuscript build attempt: unavailable for environmental
  reasons. `latexmk -xelatex` stopped before reading the manuscript because the
  local MiKTeX installation reports that its initial setup is unfinished. This
  is not a manuscript compilation error; no generated workspace artefact was
  created.
- Index integrity: global `git diff --cached --quiet` and the same check limited
  to the two authorized files both returned exit `0`. No file is staged. The
  index SHA-256 before and after writing this record was unchanged at
  `9F3BDA7DE1753EDBD9702A5FC82D8A21ACA15A8125DD09EB50F86D7D9F084A39`;
  production issued no Git mutation, branch, commit, or remote command.

## Completion

The three ordered minimum-sufficient interventions are complete. All available
invariants and validation gates pass, with no departure from the arbitration
brief; the only unavailable gate is the environmentally blocked full build
recorded above.
