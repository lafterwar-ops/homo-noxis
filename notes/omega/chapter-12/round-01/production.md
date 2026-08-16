# Production — Chapter 12 — Round 01

- Role: producer, fresh constrained context; applied the approved brief (arbitration.md §5–7) and nothing else
- Read set: arbitration.md, this log, and the target working copy only. No trace file, status file, other chapter, or canon file was opened.
- Tools: Read/Edit/Write file tools for the target and this log; shell used read-only (sha256sum, validation script). No git, no device/MCP tools.

## Baseline identity

- Target working copy: `/home/user/omega/chapter-12/round-01/chapter12-produced.tex`
- Pre-edit SHA-256: `cb6c827ec2f53fd6fb3b96dc0a40412b3eed645ff168ff558a6ad0d1ef18a244` — verified equal to the brief's baseline before the first edit (V1)
- Baseline word count reproduced with the mandated method: **3,649** (matches assignment basis exactly)
- Post-edit SHA-256: `31e6d9c2577c599fe917a5754cbd1e0987193d9d2910e084f08b36fe92b6afa1`
- Every anchor verified to match **exactly once** before editing, including E3's full three-turn sequence (V2). Edits applied in brief order E1→E9 by anchor string, smallest sufficient movement each.

## Edits applied

**E1 (chris S1) — delete the pre-gloss. Δ −14.**
Before: `…could not be reduced to fever, pride or error. Every passage I carried it through gave another person the chance to find it.\par`
After: `…could not be reduced to fever, pride or error.\par`
Sentence and its preceding space deleted; nothing else touched.

**E2 (patrick P8, minimal) — ribbon locator. Δ −3.**
Before: `In the Tomb, below the three Shield seals, I had found the dark ribbon caught in old blood.`
After: `Below the three Shield seals I had found the dark ribbon caught in old blood.`
(`I knew the uneven edge.` and the two open readings untouched.)

**E3 (patrick P2) — exposure rung. Δ +8.**
Between the unique sequence's ` ``No.''\par ` and ` ``What did you read?''\par `, inserted two turns in the file's format (own paragraphs, single blank lines):
` ``How long have you carried it?''\par ` then ` ``Two days.''\par `

**E4 (patrick P4, transformed) — tools named aloud. Δ +2.**
Before: `Water was counted, and tools --- a needle, …`
After: `Water was counted, and tools named aloud --- a needle, a blade for cloth, two cooking hooks --- shown, witnessed, sealed.`
Triad `shown, witnessed, sealed` untouched.

**E5 (john B2) — empty-seam gesture. Δ +2.**
Before: `I felt cold spread from my spine outward.\par`
After: `My hand went to the empty seam of my robe.\par`
Following one-line paragraph `The Lesser Seal.\par` untouched (verified).

**E6 (theo P2 = patrick P1 fallback) — slit-silence merge. Δ −6; paragraph count −1.**
The two consecutive anchor paragraphs replaced by the single paragraph:
`I studied the lamp. The flame stood too steady. The wall slit no longer whispered as it had while Va-Sheva sat with me. If I shouted, the sound might fail. If I spoke, who would hear? I heard no feet beyond the door.\par`
No doubled blank line left at the site (verified file-wide).

**E7 (theo P1, base) — arm the family count. Δ +17.**
Before: `The sounds continued, deeper, farther, then nearer again.\par`
After: `The sounds continued, deeper, farther, then nearer again. Somewhere in them the count was walking toward a door where my name would receive no answer.\par`
`Time became difficult.` at the paragraph head retained verbatim.

**E8 (patrick P3) — SKIPPED per its own conditional. Δ 0.**
E8 is gated on V9 (read-only grep of Chapters 1–11 for `Sa-Tavan`). Chapters 1–11 are outside the producer's readable set (the brief's authorized-files section names the target only; the producer mandate forbids reading any other manuscript chapter). V9 therefore could not be executed, so it did not confirm the absence E8 requires; E8's instruction — "Apply only if V9 confirms…; otherwise skip and record" — resolves this case to skip-and-record. The anchor `Someone other than Sa-Tavan.` stands unchanged (verified). The brief's arithmetic anticipates this landing (≈3,654 without E8). V9's execution and the E8 decision remain open to a context with read access to Chapters 1–11; ledger 11 / canon 07 currency (arbitration §7.4) stays unresolved.

**E9 (all four, colon form) — room-convention repair. Δ −1.**
Before: `Not that room --- but into the deep of it, past the wall,`
After: `Not that room: into the deep of it, past the wall,`

Net movement: −14 −3 +8 +2 +2 −6 +17 +0 −1 = **+5** (per-edit deltas each match the brief's arithmetic; brief's no-E8 projection ≈3,654 hit exactly).

## Departures

- **None requiring pause.** Every applied anchor matched exactly once and every replacement is the brief's exact string; nothing speculative was applied.
- Recorded conditions (not mismatches): (1) E8 skipped via its own "otherwise skip and record" branch because V9 is unexecutable inside the producer's read permissions — see E8 above. (2) V7's cross-file legs and V9 are read-checks of files outside the producer's readable set; the Ch12-side halves of V7 were fully verified (below) and the arbiter's cross-file verifications (arbitration §3.1, §7.1–7.3) stand unrevisited.

## Changed files

- `/home/user/omega/chapter-12/round-01/chapter12-produced.tex` (the authorized target) — only manuscript file touched.
- `/home/user/omega/chapter-12/round-01/production.md` (this log, required output).
- Nothing else read or written; no Ch1–11 or 13+ file touched (V10).

## Validation results

- **V1** PASS — pre-edit SHA = baseline; post-edit SHA recorded above.
- **V2** PASS — all nine anchors (incl. skipped E8's) matched exactly once pre-edit; E3 matched as the three-turn sequence.
- **V3** PASS — room scan post-E9: 4 turns, all opening `--- ` markers intact, **zero** mid-sentence em-dashes inside room turns; `\ldots{}` ×4 intact; no contractions introduced (no Paul turn); quote pairs balanced (room contains none; file-wide 151 `` / 151 '').
- **V4** PASS — every changed/added sentence is byte-identical to the brief's trace-sourced replacement text; plain action/state reports and free-zone dialogue only; no maxim, antithesis, first-time/epiphany marker, gloss, or prolepsis added at E1/E2/E4/E5/E6/E7/E9 sites.
- **V5** PASS — exactly one `\begin{room}`/`\end{room}` pair (terminal); three `\ornament`; every non-structural line `\par`-terminated (non-`\par` lines are exactly: `\typesetchapter`, 3× `\ornament`, `\begin{room}`, 4 room turns, `\end{room}`); no doubled blank lines; no trailing whitespace; braces balanced (0 imbalance).
- **V6** PASS — produced word count (mandated method) **3,654**, inside 3,284–4,014; equals brief's expected no-E8 landing.
- **V7** PASS (Ch12 side) — first prose line `I carried Sarah Blackwood's record against my ribs for two days.\par` unchanged; closing room unchanged except E9; terminal turn `--- Amastan.` is the literal last room content, terminal position preserved. Ch11-tail/Ch13-head legs: outside readable set; arbiter verification stands (recorded above).
- **V8** PASS — custody chain verbatim and ordered: folded cloth / one corner / two bare edges / `fingers never crossed the writing` / `two soft clicks` **before** the thigh signal **before** `second strap`; junction litany ordered (`Body held` → `Speech held` → `Proof recovered?` → `Recovered before seal.` → `Seal witnessed.`); `Va-Sheva's ribbon` possessive retained, meaning untouched; litany count = 2 exactly; `drill` count = 2 exactly; charge triplet verbatim.
- **V9** NOT EXECUTABLE in this context (recorded) — gated E8 skipped per its conditional; no speculative application.
- **V10** PASS — target and this log only; net delta +5, per-edit deltas listed above.
- **Invariant sweep** PASS — all §3/§6 invariant strings verified present verbatim post-edit, including: litany ×2; `A threshold drill.` and the child's drill line; `Proof travels.` (now hers alone, ×1); `I will wait`; latch test through `I closed it again and stayed.`; `before anyone ordered me to`; census vignette beats (sleeping boy, cut/reset seal, Faith litany, frozen lamps, `The warden gave me nothing.`); sealed-niche `exactly as before` and ceiling-seam staging; `No shout. No command.`; searched seam `Empty.`; warden count as written (`A third dropped…` / `Bound between four Shield wardens…`); `You asked Shield to handle it` and `Let me handle it` both unregularized; `I told you to wait.` / `That is why you are alive.`; double `Yes.`; `The same Seal. More force. More risk. Fewer mercies.`; `Shield counts every body it holds.`; charge triplet; `Those permitted.`; `Did you choose death?` / `No.` / `Containment before understanding.`; honorific pattern exact (`Va-Kailan` ×1, bare `Kailan` ×1, in the apology `` `Kailan,' she said. `I am sorry.' ``); anechoic paragraph verbatim incl. heart-knock; `Time became difficult.`; the three `I knew` constructions (l. 19/389/407 equivalents); seal-dye on `one hand` unlateralized; `Va-Sheva crossed the island without looking down.`
- **Forbidden-change sweep** PASS — removed strings absent (pre-gloss 0, `In the Tomb,` 0, `The wall slit had gone silent.` 0, cold-spine line 0, room em-dash construction 0); no rejected item (J-A2/A3/A4, J-B1/B3/B4, P-P5, P-P6, C-S2, T-P3-b) applied in any form; no second room or mid-account frame business; no third litany/drill; no route detail added; first line and terminal turn untouched; no edit outside the target.

State: COMPLETE
