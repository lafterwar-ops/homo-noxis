# Chapter 5 — KingJack Round 01 — Production Record

- Producer: fresh constrained KingJack producer retry
- Target: `manuscript/chapters/chapter5-Shadow.tex`
- Authorised brief: `notes/omega/chapter-5/round-01/arbitration.md`
- Corrected baseline SHA-256 required: `01D45E6484F7FDAB72A738E473C2E49D88335BC014D21677C51FCBB406EA9BCB`
- Corrected baseline lexical count required: `4504` by strict UTF-8 decoding and `\b[\p{L}\p{N}’'-]+\b`
- Fixed permitted band: `4054..4954`
- Required post-production count: `4517` (`+13`)
- Required post-production SHA-256: `65D05BD1A4D6B8654B2CB8DB77B9F073639C3B2874211545127E614C75C4FE92`

## Attempt history

### Attempt 1 — safe pre-edit pause

The first fresh constrained producer observed target SHA-256 `01D45E6484F7FDAB72A738E473C2E49D88335BC014D21677C51FCBB406EA9BCB`, a strict-UTF-8 lexical count of `4504`, and an empty Git index. The then-recorded administrative baseline required `4505`, projected `4518`, and gave the band as `4054..4956`. Because the observed count did not equal that then-locked value, the producer correctly stopped before operation 1.

- Manuscript movement: `0`
- Manuscript edit: none
- Partial operation: none
- Interpretive substitute: none
- Terminal state for attempt 1: `PAUSED`

The completed arbitration's administrative correction superseded only those mechanical count/band values and clarified that operation 4's deletion span includes its leading single space. It did not reopen or change any editorial decision. The manuscript remained at the original locked hash with movement `0` before this retry.

### Attempt 2 — corrected mechanical retry

The retry observed strict UTF-8 decoding success, target SHA-256 `01D45E6484F7FDAB72A738E473C2E49D88335BC014D21677C51FCBB406EA9BCB`, lexical count `4504`, and an empty Git index (`git diff --cached --quiet` exit `0`). All corrected preconditions passed before editing.

## Ordered operations applied

1. **Repair the toy's drive and arithmetic:** applied both exact paragraph replacements in the opening room. The full containing room was reread afterward. The toy remains a handled scale demonstration; Kailan still supplies forty teeth; the later maintenance inference and twice-yearly Pendulum claim remain unchanged.
2. **Source the divided-route conclusion:** applied the exact two-sentence replacement in the final room. The full containing room was reread afterward. Paul's compartment conclusion is now explicitly inferential; the preceding transport facts, following paraphrase, and unknown intervening road, fields, and hands remain intact.
3. **Replace knowledge of Roger's mind with observable conduct:** applied the exact sentence replacement in the final room. The full containing room was reread afterward. Roger's observed acts remain unchanged, and the following uncertainties about owner, motive, destination, order, and allegiance remain intact.
4. **Let the put-away stone carry the ending:** deleted exactly the authorised sentence together with its corrected leading single space. The full containing room was reread afterward. The paragraph now ends at `a name to carry to your grave.` Paul's next line and the later lens line remain unchanged.

No operation required interpretation, no half-applied state occurred, and no editorial decision was reopened.

## Departures

- Departure from the executable brief: none.
- Additional manuscript change: none.
- Interpretive substitution or improvement: none.
- Full build: not attempted. The constrained read scope excludes locating or inspecting the repository entry point; the independent build remains for KingJack.

## Changed files

- `manuscript/chapters/chapter5-Shadow.tex`: changed only by the four ordered operations.
- `notes/omega/chapter-5/round-01/production.md`: replaced with this retry record while preserving attempt 1 as history.
- No other project file was written by this retry.

## Counts and hashes

- Baseline lexical count: `4504`
- Final lexical count: `4517`
- Arithmetic movement: `4517 - 4504 = +13`
- Final permitted band: `4054..4954`; `4517` is within band.
- Baseline SHA-256: `01D45E6484F7FDAB72A738E473C2E49D88335BC014D21677C51FCBB406EA9BCB`
- Final SHA-256: `65D05BD1A4D6B8654B2CB8DB77B9F073639C3B2874211545127E614C75C4FE92`
- Encoding/line form: strict UTF-8, no BOM, LF line endings, final LF present.

## Validation record

- **Scope gate:** passed. The manuscript diff contains exactly the two paragraph replacements in operation 1, the replacements in operations 2 and 3, and the deletion in operation 4. Production wrote only the two authorised files.
- **Hash-before gate:** passed exactly.
- **Exact-text gate:** passed. Both operation-1 old paragraph loci and each operation 2–4 old locus occurred exactly once immediately before replacement. After all operations, every old fragment occurs `0` times; each of the two operation-1 result paragraphs and each operation 2–4 result occurs exactly `1` time. The deleted wound sentence occurs `0` times.
- **Arithmetic gate:** passed: `40^2 = 1,600`; `40^5 = 102,400,000`; `40^4 × 6 = 15,360,000`. At one input turn per second, the last value is `15,360,000` seconds (`177.777778` days), close to half a year. The later `strike but twice a year` claim remains present once and unchanged.
- **Word-count gate:** passed by strict UTF-8 decoding and exactly `\b[\p{L}\p{N}’'-]+\b`: `4517`, movement `+13`, inside `4054..4954`.
- **Post-edit hash gate:** passed exactly: `65D05BD1A4D6B8654B2CB8DB77B9F073639C3B2874211545127E614C75C4FE92`.
- **Form gate:** passed. `\begin{room}` and `\end{room}` remain equal and unchanged at `4` each; brace balance is `0`; TeX commands outside the exact replacements are untouched. The manuscript remains UTF-8 without BOM, with LF endings.
- **Source gate:** passed. No unowned narrator or inaccessible mental fact was added; Paul's route conclusion is explicitly inferential, and Roger's exit is observable conduct.
- **Canon/decision gate:** passed. Scene order, five-shadow form, blood result, recorder/CCTV distinction, promise, unexplained recorder exchange, Sarah uncertainty, postponed rite, Shadow definition, summons, and final allocation are preserved.
- **Ambiguity gate:** passed. No culprit, owner, motive, destination, Sarah knowledge, taxonomy, solids completion, Veil verdict, or external-camera fact was added.
- **Diff hygiene:** `git diff --check -- manuscript/chapters/chapter5-Shadow.tex notes/omega/chapter-5/round-01/production.md` passed with exit `0` before this record replacement; it is rechecked below as the terminal gate.
- **Git gate:** index empty before editing and after manuscript validation. Nothing was staged, committed, or pushed.

## Independent KingJack verification

- The final manuscript diff was independently inspected and is confined to the five textual loci implementing the four authorized operations: two clock paragraphs, two provenance sentences, and one deletion. No rejected, deferred, or out-of-scope proposal entered production.
- Strict UTF-8 counting and SHA-256 independently reproduce `4517` and `65D05BD1A4D6B8654B2CB8DB77B9F073639C3B2874211545127E614C75C4FE92`.
- The arithmetic independently reproduces `40^2 = 1,600`, `40^5 = 102,400,000`, and `40^4 × 6 = 15,360,000`.
- Source legality passes: Paul now expressly identifies the divided route as inference, and Roger's departure is limited to conduct Paul could observe. No omniscient narrator or inaccessible mental fact remains at either revised locus.
- Chapters 1–4 retain their exact post-KingJack hashes. Chapter 6 remains clean, and its opening still receives the unassigned solids and Ka-Syphiron summons without contradiction.
- A full build was independently attempted with `latexmk -xelatex -interaction=nonstopmode -halt-on-error` against `manuscript/00 Intro/chapter001-latexIntro.tex`, directing output to a temporary directory. MiKTeX exited before reading the manuscript (`-1073740791`) and reported that its fresh-install setup must be completed. This is an environment limitation, not a manuscript diagnostic.
- The unrelated external `ADDITION/` path and `notes/zeus-state.md` remain unopened and untouched. The final Git index is empty; no stage, commit, push, branch switch, or history rewrite occurred.

State: COMPLETE
