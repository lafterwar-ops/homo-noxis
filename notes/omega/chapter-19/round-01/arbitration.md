# KingJack Arbitration - Chapter 19 - Round 01

## Jurisdiction and seal verification

This arbitration used only the four sealed Round 01 reports and the sealed target chapter authorized in the brief. The manuscript was read but not edited. No canon, ledger, status, production, adjacent chapter, prior Omega material, Git history, or agent status was consulted.

| Evidence | Required SHA-256 | Observed SHA-256 | Ruling |
|---|---|---|---|
| John | `22C5C7B171EFD1AC64DC84453516084534D94B3179ECAA32C5DAFE0A9FAF4E94` | `22C5C7B171EFD1AC64DC84453516084534D94B3179ECAA32C5DAFE0A9FAF4E94` | Admissible; exact seal |
| Patrick | `04925DAF6519E0AA8B6AE59E88C55EFE25A00AD0E523C0A3E740EF563848ADB6` | `04925DAF6519E0AA8B6AE59E88C55EFE25A00AD0E523C0A3E740EF563848ADB6` | Admissible; exact seal |
| Theo | `4BC2EA8CE24B78CA033E2B2610ADA4BDD12AFBDBEF210503D7558BEF41A26CCA` | `4BC2EA8CE24B78CA033E2B2610ADA4BDD12AFBDBEF210503D7558BEF41A26CCA` | Admissible; exact seal |
| Chris | `82F2E6408CA34C817BEB674BA34894A6D09D46849FA57E89247EE83C0EC7F7E3` | `82F2E6408CA34C817BEB674BA34894A6D09D46849FA57E89247EE83C0EC7F7E3` | Admissible; exact seal |
| Target | `F40D8E4FAD57C5DFA534233F90D215AC200BFAB8C437B61ABE8BAFB8E7BEFA4D` | `F40D8E4FAD57C5DFA534233F90D215AC200BFAB8C437B61ABE8BAFB8E7BEFA4D` | Baseline exact |

Baseline canonical count is `7424`; fixed band is `6682..8166`. Baseline physical form is `40351` bytes, UTF-8 without BOM, with `354` LF line endings, `0` CRLF line endings, and `0` lone CR characters.

## Neutral synthesis

### Convergence

All four reports independently protect the chapter's governing achievement: a procedural climax in which five divided offices make an irreversible decision without converting the surviving denial road into certainty. All protect the same-small-room opening, Kailan's explicit return to first person, the five distinct office roads and arches, the Justice road's five rooms, the antechamber hearing, the Threshold Exception, the isolated depositions and custody chain, the complete refusal audit, Roger's call, the one-in-five denial road, the possession ruling, Ka-Elun's death and the damage to Faith succession, the Greater Seal, Jean-Charles's unresolved absence and return, Sarah's non-condemnation, and the final Pendulum with reel and separate breaths. None supports structural rewriting.

The reports also converge that the chapter's physical carriers are its strength: recorder and reel, counted objects, separated rooms, wet clay, hands, stone, handset, gates, and Pendulum. The arbitration therefore refuses any package that explains away their ambiguity or adds a new plot road.

### Orthogonal complementarity

- John contributes the only exact mathematical continuity audit and the most exacting distinction between recorded words and unrecorded sights. John also identifies the pre-Exception recorder-custody gap.
- Patrick contributes the live blocking audit. Its strongest unique findings are Jean-Charles's missing initial stage position and Shield's apparent second beginning during Kailan's finding.
- Theo supplies the cold-reader control: the architecture, moral uncertainty, and terminal images already survive without amplification. This limits the intervention package and weighs strongly against optional compression or reveal-order changes.
- Chris supplies the material/form control: custody and physical carriers should bear meaning without a general explanatory rewrite. This becomes a selection rule, not permission to sand away Kailan's judgments.

### Disagreement resolved against the current text

Three reports treat the deposition source as already legal because the reel carries the private testimony into the present room. John identifies the narrower defect: the current sentence says it carries the *words*, while the following passage also narrates unsounded sights and actions - the reset beam, what remains cut in stone, Paul placing and checking the machine, notebook marks, and room movement. The existing text gives enough information to infer Paul as a possible source, but the absolute prohibition on omniscient narration does not permit source legality to depend on inference. John's diagnosis prevails only to that bounded extent. The explicit reel statement remains verbatim, and a single Paul-to-Kailan sight-source sentence is added.

Theo's no-mandatory-edit conclusion and Chris's no-source-repair conclusion are otherwise respected: no deposition content, office voice, outcome, or ambiguity changes. Patrick's remaining blocking concerns do not all justify additions; only the two exact discontinuities that can be repaired without new choreography are admitted.

## Minimum-sufficient package

Exactly four ordered replacements are authorized, all in `manuscript/chapters/chapter19-Seal.tex`. They repair five traced defects: the skipped Pell pair; provisional custody of a recorder already turning in the hearing; Jean-Charles's initial stage position; Shield's repeated conversational onset; and the source of deposition visuals. No other manuscript operation is authorized.

### Operation 1 - restore the omitted nearest-truth term

- Authorized file: `manuscript/chapters/chapter19-Seal.tex`
- Order: `1`
- Traceability: John, nearest-truth continuity audit.
- Reason: the displayed Pell sequence ends at `41 29 -1`, but `239/169` is not the immediate next pair. Adding `99 70 1` makes the entered `239/169` the next term while preserving both later appearances of `239/169`.
- Protected invariants: the second Justice room, its problem, Ka-Leth's answer, the later Light deposition, pace, and all plot facts remain unchanged.
- Canonical word delta: `+3`
- UTF-8 byte delta: `+9`

Exact old block:

```text
\textit{1 1 -1; 3 2 1; 7 5 -1; 17 12 1; 41 29 -1.}
```

Exact replacement block:

```text
\textit{1 1 -1; 3 2 1; 7 5 -1; 17 12 1; 41 29 -1; 99 70 1.}
```

Deterministic gate: before replacement, old `1`, new `0`; after replacement, old `0`, new `1`.

### Operation 2 - establish provisional recorder custody and place Jean-Charles

- Authorized file: `manuscript/chapters/chapter19-Seal.tex`
- Order: `2`
- Traceability: John, pre-Threshold recorder custody; Patrick, Jean-Charles's missing initial stage position.
- Reason: the machine is already turning when Sarah's testimony begins, but formal binding arrives only at the Threshold Exception. The added sentences give it provisional, chamber-bound Shield custody without duplicating the later five-deposition binding. The final sentence places Jean-Charles with Shield before Va-Sheva vouches for and dispatches him, while revealing nothing about his later missing interval.
- Protected invariants: the hearing still begins only after Justice convenes it; Kailan remains bound; Paul and Sarah remain anomalously unbound; the later Threshold Exception remains the sole formal admission of Paul and reel to the five deposits; Jean-Charles's disappearance, actions while absent, return, and possible implication remain wholly unresolved.
- Canonical word delta: `+41`
- UTF-8 byte delta: `+285`

Exact old block:

```text
Only then did Ka-Leth convene the hearing. Shield bound my hands before the same five offices that had tried me. Paul and Sarah stood unbound beside me, which was not law, and was Va-Sheva's doing.\par
```

Exact replacement block:

```text
Only then did Ka-Leth convene the hearing. Before the first testimony, Sa-Tavan counted Paul's recorder, two reels, notebook and pencil. Ka-Leth allowed the machine to turn under Shield's provisional custody; nothing it carried could leave before Justice disposed of it. Shield bound my hands before the same five offices that had tried me. Paul and Sarah stood unbound beside me, which was not law, and was Va-Sheva's doing. Jean-Charles stood with Shield's wardens along the wall.\par
```

Deterministic gate: before replacement, old `1`, new `0`; after replacement, old `0`, new `1`.

### Operation 3 - make Shield's second intervention continuous

- Authorized file: `manuscript/chapters/chapter19-Seal.tex`
- Order: `3`
- Traceability: Patrick, Shield's apparent double beginning.
- Reason: Ka-Dhavar has already answered during Kailan's finding. `spoke again` makes the next intervention a continuation instead of resetting his entrance; it changes no evidence, timing, voice, or jurisdiction.
- Protected invariants: Shield's war-board comparison, prior warnings, station losses, ridge-cell request, clipped evidentiary voice, and Kailan's continuing finding all remain verbatim.
- Canonical word delta: `+1`
- UTF-8 byte delta: `+3`

Exact old block:

```text
Ka-Dhavar of Shield answered before I finished. ``I have said this table was under an eye for two years,'' he said, ``and I was told I was seeing shapes in the dark, which is Shield's disease. The wrong tremors began before the bore. Our outer stations went silent in order. I take no pleasure in the shapes having faces now.'' He asked for the disposition of the ridge cells and no one asked whether he believed me.\par
```

Exact replacement block:

```text
Ka-Dhavar of Shield spoke again before I finished. ``I have said this table was under an eye for two years,'' he said, ``and I was told I was seeing shapes in the dark, which is Shield's disease. The wrong tremors began before the bore. Our outer stations went silent in order. I take no pleasure in the shapes having faces now.'' He asked for the disposition of the ridge cells and no one asked whether he believed me.\par
```

Deterministic gate: before replacement, old `1`, new `0`; after replacement, old `0`, new `1`.

### Operation 4 - source the visible connective tissue of the depositions

- Authorized file: `manuscript/chapters/chapter19-Seal.tex`
- Order: `4`
- Traceability: John, narration provenance audit; bounded by Theo's and Chris's finding that the spoken testimony already has a valid reel carrier.
- Reason: the existing, locked statement continues to establish that the reel carried every private deposition's words into the present small room. The added sentence establishes Paul as the source of only the visible circumstances he personally saw or enacted. It grants him no access to another person's thoughts and gives Kailan no external camera.
- Protected invariants: the explicit reel-source statement remains verbatim; Kailan remains the first-person teller; Paul and the sealed reel remain the only travellers through all five rooms; every deposition remains isolated; custody, no-copy rules, voices, facts, and uncertainty remain unchanged.
- Canonical word delta: `+26`
- UTF-8 byte delta: `+138`

Exact old block:

```text
The five rooms were cleared and shut again. Sa-Tavan took the Keepers into them in the order Justice named, returned alone, and brought Paul to each door. At every threshold he counted the recorder's two reels, Paul's notebook and the pencil in Paul's hand; when Paul came out, he counted them again. He made no copy. The deposing Keeper left by the same road and returned to the separated seat before the next was called. No Keeper heard another's deposition. I remained bound in the antechamber and heard none of them then. I know the words because the machine carried them into the same small room where Paul and I now sit; the reel remained under the Seal, as Justice ordered. Only Paul and that reel travelled the whole road.\par
```

Exact replacement block:

```text
The five rooms were cleared and shut again. Sa-Tavan took the Keepers into them in the order Justice named, returned alone, and brought Paul to each door. At every threshold he counted the recorder's two reels, Paul's notebook and the pencil in Paul's hand; when Paul came out, he counted them again. He made no copy. The deposing Keeper left by the same road and returned to the separated seat before the next was called. No Keeper heard another's deposition. I remained bound in the antechamber and heard none of them then. I know the words because the machine carried them into the same small room where Paul and I now sit; the reel remained under the Seal, as Justice ordered. What lay around those words---the rooms, the hands, the movements of the machine---Paul gave me before I began: only what he saw and did. Only Paul and that reel travelled the whole road.\par
```

Deterministic gate: before replacement, old `1`, new `0`; after replacement, old `0`, new `1`.

## Classification of all serious proposals

| Proposal | Classification | Arbitration reason |
|---|---|---|
| Explicitly source deposition visuals through Paul while retaining the sealed reel as source of the words | **Accepted** | Operation 4 closes the only absolute narration-legality gap without changing testimony. |
| Put the already-turning recorder under provisional custody before the Threshold Exception | **Accepted** | Operation 2 distinguishes provisional chamber custody from later formal five-deposition binding. |
| Add the omitted `99 70 1` Pell pair | **Accepted** | Operation 1 repairs an exact mathematical discontinuity and changes no later value. |
| Change `the hearing could not know` to `we could not know` | **Rejected** | `The hearing` names the evidentiary body's limit, not an external knower; the sentence already preserves uncertainty and remains within Kailan's witnessed scene. |
| Make a general source-language pass | **Rejected** | A blanket pass is not minimum-sufficient. Operation 4 solves the bounded defect; ward reports, captured line, and Kailan's direct witnessing already source the rest. |
| Compress procedural explanation to pay for additions | **Rejected** | The package remains comfortably inside band. No custody, deposition, or refusal material needs to be removed to fund `+71` words. |
| Supply full reader-solvable data for every Justice problem | **Rejected** | It would convert admission pressure into puzzle exposition without serving the hearing. |
| Show Jean-Charles's missing hour | **Rejected** | It would destroy a locked ambiguity. |
| Place Jean-Charles before Va-Sheva dispatches him | **Accepted** | Operation 2 supplies only a stage position, not an account of his arrival or absence. |
| Make Sarah accuse, absolve, or otherwise settle Jean-Charles | **Rejected** | Her non-condemnation is a locked evidentiary silence. |
| Prove or disprove the one-in-five denial road | **Rejected** | Either version would erase the chapter's governing productive uncertainty. |
| Move Ka-Elun's death before the ruling | **Rejected** | It would weaken the tragedy of a valid irreversible command surviving damage to the office needed to perform it. |
| Transfer Faith's last note cleanly before Ka-Elun dies | **Rejected** | It would cancel the locked succession damage. |
| Reveal Ka-Elun's death only after the attempted rescue | **Rejected** | The current foreknowledge produces ritual dread rather than rescue suspense; Theo's cold read confirms the death still lands. |
| Add one concrete action for bound Kailan during the rescue | **Rejected** | `my bound hands useless` and the collective `we` are physically coherent; adding choreographic specificity is not needed to understand his helpless participation. |
| Carry Paul's leg injury forward with a limp or support beat | **Rejected** | `caught` establishes impact but not continued entrapment or incapacity. A new symptom would add a fact rather than repair a contradiction. |
| Strengthen the first, second, and fifth admission rooms with extra physical testing | **Deferred** | The proposal is not bounded to exact text, and the fixed rooms already pay off as deposition rooms. No general performance expansion is authorized. |
| Change Shield's repeated onset to a continuation | **Accepted** | Operation 3 is exact and removes the reset without altering content. |
| Add a cue or listener to Sarah's elided self-account | **Rejected** | The present `you have had it from her already` is Kailan addressing Paul in the framing room; the ellipsis avoids repeating testimony Paul already heard. |
| Preserve the physical counter-actions within the long Balance, Roger, and Paul speeches | **Accepted as an invariant; no textual operation** | Those counter-actions remain untouched by the package. |
| Compress the post-deposition return recap | **Rejected** | It visibly verifies custody, degrees of certainty, case control, and Faith's exact pauses before Paul combines the five headings. |
| Replace the false-witness explanatory sentence with only a wall-carving carrier | **Rejected** | The present sentence makes the room-to-office epistemic correspondence legible exactly once; the subsequent deposition then performs the distinction. |
| Trim the early world-stakes judgment, Balance's `terrible thing` conclusion, the lawful-ending judgment at the clay, or the offices' final choice-to-leave judgment | **Rejected** | These are bounded first-person or character judgments, not omniscient gloss. Removing them would flatten Kailan, Balance, and the moral pressure for no demonstrated gain. |
| Use custody and material carriers as the governing revision law | **Transformed** | It governs selection: Operations 2 and 4 strengthen custody; all other carriers are protected. It does not authorize a free-standing carrier rewrite. |
| Add ordinary-life texture or individual interiors to the ward montage | **Rejected** | The existing ward reports are sufficient and source-legal; invented interiors would violate the narration lock. |
| Expand Cataclysm mechanics, add a sixth alternative, enlarge the catastrophe, or add a post-Pendulum verdict | **Rejected** | Each would dilute the decision, pre-empt later form, or close productive uncertainty. |
| Treat zero manuscript movement as the only acceptable outcome | **Transformed** | The architecture remains frozen, but four exact replacements are warranted by text-level defects. No structural rewrite follows. |
| Alter Chapter 18, Chapter 20, Ravar's later form, Va-Sheva's later ending, or any later revelation | **Out of scope** | No backward or forward file change is exact and unavoidable here; none is authorized. |

## Lock and source-legality audit

The package leaves the opening in the same small Greater Seal room. Paul still sets aside the return reel, threads the fresh reel, labels it, and lets Kailan explicitly reclaim the account in first person. The five office roads and arches remain distinct; the earlier Faith labyrinth and present five-room Justice road remain explicit; the other Keepers still enter by their own arches.

Every Justice room and problem remains; the antechamber hearing remains; the Threshold Exception and five grants remain; Paul still holds no office, key, lever, or decision; all five isolated depositions, item counts, no-copy rule, and separate returns remain. Operation 2 does not anticipate those deposits: it controls an already-running machine only within the hearing until Justice disposes of it. Operation 4 sources visible detail only through Paul's direct perception and action. It neither attributes another mind to Paul nor imports a fact from outside the sealed reel, captured line, ward reports, or Kailan's own field.

Every Beast/refusal alternative remains, including the unresolved one-in-five denial road. Roger's call, the irreversible possession ruling, the distinction between command and permission, and the ban on reopening remain verbatim. Ka-Elun still dies after the ruling; Faith's succession remains operationally damaged. The Greater Seal, Jean-Charles's unexplained interval and return, Sarah's non-condemnation, and the final Pendulum, reel, breaths, distinct voices, fixed outcomes, and productive uncertainty remain intact.

No sentence is added about Chapter 18, Chapter 20, Ravar, Va-Sheva's later ending, or any later solution. No earlier repair or later authorization is created.

## In-memory package simulation

The four replacements were applied sequentially to an in-memory UTF-8 decoding of the sealed target. The target file itself was not written.

| Gate | Pre-operation old/new | Post-operation old/new | Word delta | Byte delta |
|---|---:|---:|---:|---:|
| Operation 1 | `1 / 0` | `0 / 1` | `+3` | `+9` |
| Operation 2 | `1 / 0` | `0 / 1` | `+41` | `+285` |
| Operation 3 | `1 / 0` | `0 / 1` | `+1` | `+3` |
| Operation 4 | `1 / 0` | `0 / 1` | `+26` | `+138` |
| **Package** | all four old blocks unique; all four new blocks absent | all four old blocks absent; all four new blocks unique | **`+71`** | **`+435`** |

Predicted publication state after applying only this package:

- Canonical count: `7495` (`7424 + 71`), inside `6682..8166`.
- Byte length: `40786` (`40351 + 435`).
- SHA-256: `2CF7C1430F5ECD7ADB0767C38E2C10103C856B383843460838F7C889E89378DA`.
- Encoding: UTF-8 without BOM.
- Newlines: `354` LF, `0` CRLF, `0` lone CR; unchanged.
- LaTeX/form counts: `\typesetchapter` `1`; total `\begin` `3`; total `\end` `3`; `center` open/close `2/2`; `room` open/close `1/1`; `\ornament` `10`; `\par` `137`; `\textit` `3`; `\emph` `9`. All are unchanged.
- Exact-block gates: each old block is `0` and each replacement block is `1` after the complete simulation.

The package is deterministic only on the verified target seal. If the target hash, any old/new gate, encoding, or newline form differs at production time, production must stop rather than broaden the authorized match.

State: COMPLETE
