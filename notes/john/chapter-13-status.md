# John - Chapter 13 - Status

- Chapter: `manuscript/chapters/chapter13-Infiltration.tex`
- State: FROZEN
- Phase: 13 - Validate and freeze
- Last updated: 2026-08-13
- User constraints: Run the full John workflow on Chapter 13. Never commit, push, or stage. New incoherence or obligations may move only into chapters greater than 13. Use a first complete draft followed by honest scoring and at most five rewrite/rescore iterations targeting genuine gains of 2-3 points. Keep the chapter within +/-10% of its John-start word count throughout every completed scored draft and at pause/freeze.
- Working-tree baseline: Chapter 13 and the tracked manuscript were clean. The repository-local `.codex/skills/john/` directory was already untracked from the preceding skill-creation work and remained untouched except for read-only use.
- John-start word count (W0): 6,213
- Word-count method: Deterministic PowerShell LaTeX-source tokenizer fixed at John start. Read the source; remove unescaped `%` comments; remove LaTeX control-sequence names and optional square-bracket arguments; count Unicode letter/number tokens with internal apostrophe or hyphen groups.
- Permitted word-count band: 5,592 to 6,834 words inclusive
- Frozen word count: 5,615 (598 words / 9.63% below W0; inside band)
- Rewrite iterations used: 3 of at most 5

## Governing diagnosis

- Soul: two damaged readers meet at opposite ends of Reggane and make a compact neither can safely refuse. The protective apparatus born from that compact becomes the instrument by which Sarah can possess the Mountain.
- Fundamental question: can a guardian build the means of protection without making herself the possessor and infiltrator?
- Causal spine: 1960 signal -> fourteen-year search -> 1974 admission and compact -> Horizon's accumulating layers -> the 1980 race breach -> defensive reach becomes extraction and veto -> Sarah admits possession -> Paul learns that he too was selected and placed -> the house receives an impossible double knock.
- Emotional movement: Sarah controls the account; Kailan strips away her claim to discovery; Ka-Xhian's offer exposes mutual coercion; Sarah owns the appetite beneath the protection; Paul recognises his instrumentalisation; the room loses its status as refuge.

## Locked decisions

- Chapters 1-12 are fixed incoming canon and were not edited.
- No commit, push, or staging operation is authorised or was performed.
- Reggane signal and Ka-Xhian's blinding occur in 1960; Sarah reaches the folds and Horizon begins in 1974.
- Ka-Xhian makes the offer, as Chapter 12 requires; Sarah negotiates its limits.
- The unknown second camera/dead-drop is not Sarah's known or monitored channel. K suspected it, Paul watched it, and both know the room's information left through it; no one in the room knows its owner.
- The photograph original remains in Shield custody; Sarah has the authorised copy; Kailan took only the names-scrap.
- Kailan carried the drawer's secret for thirty years inside the Mountain. He has been outside only weeks in the 2026 frame. Chapter 14's "six-and-sixty years" since Reggane is correct and was not changed.

## Final architecture

- Opening: Martinez's identification work and the pump inspection sit inside the seven years already established in Chapter 11.
- Threshold: Sarah is physically transferred from Martinez to Amastan's people; the route remains undisclosed.
- Compact: Ka-Xhian's blindness, Sarah's contingency instructions, ordinary Mountain life behind the door, Shield's offer, the limits, three oaths and the photograph are made on the page.
- Institutional drift: liaison -> monitoring -> secrecy management -> Foundation screen -> routes -> mapping -> five -> contingency/veto.
- Proof scenes: the 1980 race breach and White Six; the survey destroyed across eleven hands; the woman in the drawer; Paul's planted employment; the double knock.
- Ending logic: one succession-shaped trace leaves death and imitation both possible; the second trace makes lawful succession impossible and triggers mobilisation.

## Changes made

- `manuscript/chapters/chapter13-Infiltration.tex`: rebuilt and frozen.
- `manuscript/Supporting document/03 — The Outside — Blackwood & the Extraction (EMBARGOED)/Blackwood — Edward & Sarah, and How the Outside Found the Mountain — canon (EMBARGOED).md`: separated 1960 detection from 1974 contact/Horizon.
- `manuscript/Supporting document/07 — Physical Description & Bearing — canon.md`: aligned Sarah's 1960/1974 ages, photograph and present frailty.
- `manuscript/Supporting document/08 — Chronology & Timeline — continuity ledger.md`: corrected the 1960/1974 sequence and the manuscript's March 2026 interview frame.
- `manuscript/Supporting document/11 — Knowledge-State — continuity ledger.md`: corrected K/P/Sarah knowledge of the wired cameras, unauthorised camera, dead drop and unknown owner.
- `notes/john/chapter-13-status.md`: maintained the durable John record and freeze state.

## Score history

| Draft | Score /100 | Change | Word count | Defects targeted | Verdict |
|---|---:|---:|---:|---|---|
| First complete draft | 94 | - | 5,698 | 1974 chronology, staged compact, narration law, room pressure, double knock | retained provisionally |
| Rewrite 1 | 96 | +2 | 5,599 | pump-to-folds custody chain; live 1980 operation | retained |
| Rewrite 2 | 98 | +2 | 5,632 | camera-owner ambiguity; Foundation's real obligations; narrative gloss | retained |
| Rewrite 3 | 100 | +2 | 5,615 | Ka-Xhian must make the offer; K's true time outside; trace/cause logic | FROZEN |

Final rubric: dramatic/emotional 20/20; architecture/causality 20/20; voice 15/15; prose 15/15; canon/continuity 15/15; pacing/word discipline 10/10; transition/payoff 5/5.

## Forward obligations (chapters > N only)

- None created by this pass.

## Audits completed

- Phase 7 causality: every major event has a prior cause and next consequence; Chapter 12's offer and Chapter 14's trial transition agree.
- Phase 8 voices: Sarah notices instruments, permissions, routes, ledgers and ownership; Kailan reads doctrine and moral shape; Paul speaks empirically and does not use Kailan's name.
- Phase 9 adversarial: repaired the hidden offer-direction contradiction and the false assumption that Kailan had spent thirty years outside.
- Phase 10 systems: Horizon's information, legal, logistical and coercive layers now operate visibly; no capability arrives without infrastructure.
- Phase 11 payment: Ka-Xhian's eyes, the bread-carrier's secrecy, Sarah's oaths, the Foundation's real obligations, White Six and Paul's instrumentalisation all pay for the machinery.
- Phase 12 continuous read: Chapters 12 -> 13 -> 14 and target-relevant Chapters 15-24 read cleanly.

## Validation completed

- Fixed word-count band satisfied: 5,615 is between 5,592 and 6,834.
- Ten `room` environments open and close; all target `begin/end` environments and source braces balance.
- Narration-zone scan found none of the banned retrospective/gloss patterns targeted by the voice canon.
- `git diff --check` passes.
- Historical checks: Gerboise Bleue at Reggane on 13 February 1960; 1979 Reggane-In Salah direction; 1980 Reggane-Bordj Mokhtar special on 8 January; Moussa ag Amastan's France/Charles de Foucauld saying.
- Full XeLaTeX build was attempted in a temporary output directory. It could not start because the local MiKTeX installation is unfinished and denied creation of its per-user setup directory. Static LaTeX validation passed; no build artifact entered the repository.
- Working tree remains unstaged and uncommitted.

## Exact resume instruction

Chapter 13 is frozen. Do not resume or revise it unless the user explicitly says to reopen `John(chapter 13)`. If reopened, reread this file, verify W0 remains 6,213 and retain the 5,592-6,834 band. Never commit, push or stage.
