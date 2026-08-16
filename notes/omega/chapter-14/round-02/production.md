# KingJack Production — Chapter 14 — Round 02

## Baseline and arbitration seal

- Arbitration was `State: COMPLETE` and its SHA-256 matched the required seal: `70177774333A227CA7F657548770AEA2054234BA685A837B5FA03F5952A8C2B9`.
- The target baseline SHA-256 matched `14F6E3F06D0E7D6629939EA14D090112539866F6E0B8BC8F0E6886CF8A0BFD0F`.
- The baseline canonical count was `7023` under `[A-Za-z0-9]+(?:[-'’][A-Za-z0-9]+)*`.
- Each of the three complete arbitration old-text blocks occurred exactly once.
- The Git index was empty before production.

## Applied operations

1. Replaced `so low that no one else heard it` with `barely above a breath` in the complete Ka-Elun paragraph. Canonical delta: `-4`.
2. Replaced `beneath his hooded lamp` with `beneath the hooded lamp kept there` in the complete token-transfer paragraph. Canonical delta: `+2`.
3. Replaced `survived both of Ka-Raedin's votes` with `survived Ka-Raedin's vote for death` in the complete utility paragraph. Canonical delta: `0`.

The substitutions were applied exactly, as complete blocks, in Operations 1–3 order. No smoothing, improvisation, deferred work, or rejected proposal was introduced.

## Changed files

- `manuscript/chapters/chapter14-Trial.tex` — exactly the three authorized substitutions.
- `notes/omega/chapter-14/round-02/production.md` — this production record replaced the `WAITING` template.

No other file was changed by this production pass.

## Deterministic validation

- Final target SHA-256: `D87263540A1E3EC96EA3024B3E830C693D744786CADB6E6C35EA66CF4E2D87CA`.
- Final canonical count: `7021` (`-2` total), within `6321..7725`.
- Exact anchor counts after production: old/new `0/1`, `0/1`, `0/1` for Operations 1–3.
- LaTeX structure: `scripture` environments `5/5`; `room` environments `1/1`; raw braces `20/20`.
- Serialization: valid UTF-8, no BOM, LF-only (`CRLF=0`, bare `CR=0`).
- Target diff: exactly three hunks, three removed lines and three added lines; no whitespace or newline normalization.
- `git diff --check` was clean.

## Source and form validation

The three edited paragraphs were read continuously with their immediate testimony context. Operation 1 asserts only Kailan's audible perception and preserves Ka-Elun's direct speech. Operation 2 remains recoverable through Kailan's sight, memory, witnessed token transfer, and bodily sensation. Operation 3 remains recoverable through Kailan's firsthand participation in the resumed hearing and Ka-Raedin's witnessed death vote. No assertion exceeds first-person source legality, and no scene, fact, route, custody outcome, vote, office position, revelation, or ambiguity changed.

## Build validation

Attempted the available established LaTeX invocation:

`latexmk -pdf -interaction=nonstopmode -halt-on-error`

It exited `1` before compilation because MiKTeX reported: `It seems that this is a fresh TeX installation. Please finish the setup before proceeding.` No dependency, generated source, or manuscript change was made in response.

## Compliance

- Read scope remained limited to `production.md`, the sealed `arbitration.md`, and `chapter14-Trial.tex`.
- Write scope remained limited to `chapter14-Trial.tex` and `production.md`, both through `apply_patch`.
- No staging, commit, push, branch, publication, or other Git mutation was performed.
- The Git index remained empty after production.

## Independent KingJack closure

- KingJack independently inspected the final target diff and confirmed exactly three authorized replacement hunks and no smoothing or unauthorized manuscript movement.
- All six fenced arbitration blocks were checked against the produced manuscript: every old block occurs zero times and every approved replacement occurs exactly once.
- Kailan remains the recoverable first-person teller. Ka-Elun's line is now bounded to what he can hear; the later hooded lamp is explicitly the one kept at Light's chamber seat; and the legal hinge now refers only to Ka-Raedin's witnessed vote for death.
- Final canonical count is `7021`, down `2` words (`-0.028%`) from `7023`, inside `6321..7725`. Final SHA-256 is `D87263540A1E3EC96EA3024B3E830C693D744786CADB6E6C35EA66CF4E2D87CA`.
- The trial and Justice rooms, Hall and Labyrinth route, five office sequence, Beast and sphere disclosures, accusation closure, Beast refusal points, death sentence, Exception petition and votes, token/tablet/wrist/record custody, household severance, Shield transfer, recording-room coda, and productive ambiguities remain unchanged.
- Structural checks pass: `scripture` environments `5/5`, `room` environments `1/1`, raw braces `20/20`, eight ornaments, 181 `\par` markers, UTF-8 without BOM, LF-only line endings, clean `git diff --check`, and empty Git index.
- Chapter 13 asks Kailan to complete the trial testimony; Chapter 14 remains that first-person account and ends under the recording-room lamp; Chapter 15 resumes live room dialogue from the stopped account. Chapters 1--13 retain their sealed hashes, no later chapter changed, and every Chapter 14 Round 01 artifact retains its preflight hash.
- A full `latexmk` build was independently attempted. MiKTeX exited before processing the manuscript with code `-1073740791`, reporting that its fresh-install setup is unfinished. This is an environment limitation, not a Chapter 14 LaTeX failure.
- User-authored commit `da3c50c4ea2f0f166be9675cb63dc5040cbb032a` landed during the round. It did not change the Chapter 14 baseline or any sealed contributor hash, so the round did not become version-mixed. KingJack performed no staging, commit, or push.

State: COMPLETE
