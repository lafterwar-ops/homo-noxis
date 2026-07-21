# REORDER PROTOTYPE — the Ch9–17 interleave (Pass 2, §3.3/§9)

**Status:** ✅ **MINIMAL VARIANT EXECUTED (Pass 2, Session 5).** New order in the repo: `…12 Claim · 13 Trial · 14 Horizon · 15 Knocks · 16 Mock · 17 Return`. Validated: the account now ends at Horizon(14) before Knocks(15) "the account is finished"; Trial→Horizon adjacent (exile follows trial); Mock→Return adjacent (departure→desert). Filenames match headers; 1–24 contiguous, no dups; LaTeX bodies untouched (only `\typesetchapter` digits changed via `mv`+`sed`, plain — not committed).
**Still OPEN for the author (the RECOMMENDED variant's extra step):** detach Ch11 Infiltration's live-signal cliffhanger tail ("the southern array… it is your shape… It is drawing again… Now, while we are standing here", ~L127–147) and move it to the **head of Ch16 Mock**, so the P2 crisis is one continuous run and the cliffhanger no longer dangles 11→16. This is a craft/chapter-split call left to the author.

---
*(Original diagnostic retained below for reference.)*

## The three threads braided through Ch9–17

- **A — Kailan's past account** (chronological): 1 Ascension · 2 Mirror · 3 Oasis · 4 Mountain · 5 Shadow · 6 Festival · 7 Chain · 8 Light(martyrdom) · **10 Tomb**(the crime) · **12 Claim**(disclosure→arrest) · **14 Trial** · **16 Horizon**(exile; the account ENDS here — "There is no more Mountain to give you… Rest, Kailan").
- **B — Sarah's past account** (interleaved): **9 Reggane**(origin) · **11 Infiltration**(reaching the Mountain via Amastan). Both are Sarah testifying to Paul.
- **Present-day frame** (Swiss house, during/after interviews) — TWO sub-threads:
  - **P1, knock-convergence = 13 Knocks.** Opens *after* the account is done ("The account is finished… I should be gone by morning"); Paul asks the one question the account stepped over (what follows an Ascension); K describes the succession knock; then **Sarah enters** (L103) and reveals she holds the seismic record of every knock "longer than you have been alive" — the knock is "the sound of the Mountain changing hands." Three-hander. Must sit AFTER both A (Horizon) and B.
  - **P2, live-signal crisis = tail of 11 Infiltration → 15 Mock.** Ch11 ENDS on a cliffhanger ("It is drawing again. The same five. Now, while we are standing here."); **Mock resumes that exact scene** ("It is a rising… the interval is holding, eleven minutes… someone has put a machine on the desert floor") = a counterfeit/forced Ascension → the enemy is AT the Mountain → they leave south (Mock ends with departure) → **17 Return** (desert crossing).

## The confirmed defect
Current order 13 Knocks · 14 Trial · 15 Mock · 16 Horizon puts **P1 (Knocks, "the account is finished") BEFORE account chapters 14 Trial and 16 Horizon.** Impossible: the account cannot still be delivering itself after Paul says it is complete. Also **16 Horizon (a past-account chapter) is jammed between 15 Mock's departure and 17 Return's continuation of that same journey.** (The Tomb/Claim inversion, a third break, was already fixed by the author.)

## The entanglement (why it is not a clean 4-file swap)
P2's crisis is currently SPLIT with its opening cliffhanger welded to the end of **11 Infiltration** (a Sarah *account* chapter that sits early, at position 11) while its payoff (Mock) sits late. If Knocks (P1) must move after Horizon, and the crisis (P2) must be one continuous run into Return, then Ch11's crisis-tail wants to travel with Mock — i.e., a **chapter split**, not just a reorder. This requires deciding the intended present-day timeline:
- **Does the live crisis (P2) erupt BEFORE or AFTER the knock-convergence (P1)?** Logic favors **after**: the account finishes → Knocks convergence (they realize the knock is detectable / the Mountain is findable and countable) → then a *live* knock appears where none should (P2) → horror → they run. "It is drawing again, NOW, while we are standing here" reads as an eruption during/just after that convergence, not something left dangling for five chapters.

## RECOMMENDED resolution (author decision required)
Target reading order for the block:
`9 Reggane · 10 Tomb · 11 Infiltration · 12 Claim · 13 Trial · 14 Horizon · 15 Knocks · 16 Mock · 17 Return`
plus **detach the live-signal cliffhanger** (Ch11 L127–147: "the southern array… it is your shape… It is drawing again… Now, while we are standing here") from the end of **Infiltration** and move it to the **head of Mock**, so P2 is one continuous crisis (Knocks convergence → live signal appears → Mock analysis → departure → Return). Infiltration then ends on its account beat (Sarah's reaching the Mountain), not on a crisis it no longer adjoins.

### Minimal variant (if the author wants NO chapter split this pass)
Just reorder the four files and accept a longer suspense-cut on the Ch11 cliffhanger:
`…12 Claim · 13 Trial · 14 Horizon · 15 Knocks · 16 Mock · 17 Return`
Renames + `\typesetchapter` renumbers:
- `chapter14-Trial.tex` → `chapter13-Trial.tex`  ({Chapter 14}→{Chapter 13})
- `chapter16-Horizon.tex` → `chapter14-Horizon.tex` ({Chapter 16}→{Chapter 14})
- `chapter13-Knocks.tex` → `chapter15-Knocks.tex` ({Chapter 13}→{Chapter 15})
- `chapter15-Mock.tex` → `chapter16-Mock.tex`  ({Chapter 15}→{Chapter 16})
(Use temp names to avoid collision — it is a 4-cycle: 14→13, 16→14, 13→15, 15→16. Do renames with plain `mv` like the author's Tomb/Claim swap, NOT `git mv`; do not commit.) Residual cost: Ch11's "it is drawing again, now" then dangles 11→16 (five chapters). The recommended variant above avoids this.

### Validation checklist after any execution
- Every `\typesetchapter{Chapter N}` matches its new filename number and neighbors.
- Read the four seams: Horizon END → Knocks OPEN ("account is finished" now true); Knocks END → Mock OPEN (crisis); Mock END (departure south) → Return OPEN (desert). 
- Confirm no name/knowledge is referenced before introduction after the move (Reggane/Amastan/Noxius-Zero/Threshold-Exception orderings already verified fine).
- Grep the four `\typesetchapter` lines; re-list the directory to confirm 1–24 contiguous, no dup numbers.

**Why left for the author:** the recommended fix needs a timeline ruling + a chapter split (authorial craft calls), and the author is live in the repo. The minimal variant is safe and mechanical and can be done by the next session if the author signals it should proceed.
