# John — Chapter 15 — Status

- Chapter: `manuscript/chapters/chapter15-Knocks.tex`
- State: FROZEN (lawful pass, 2026-08-14; author-approved move list executed exactly)
- Phase: 13 — validated and frozen (full-book compile pending on the author's machine)
- Last updated: 2026-08-14
- User constraints: **The source law governs absolutely: the chapter is the tape.** No prose narration of the present frame in any voice; staging enters only through recorded speech and the transcript conventions (`--- ` turns, vocatives, `\centerline{\textit{[\,…\,]}}` annotations as in Ch17, bare `[\,---\,]` for silence). Propose-first: every move was approved by the author before the file was touched. Never commit, push, or stage.
- History: a 2026-08-14 pass that added K-voiced frame narration was **fully reverted by the author** as a source-law violation (see "Voided pass" below). This pass replaces it.
- John-start word count (W0): 1,817 (original restored text)
- Word-count method: deterministic Python LaTeX tokenizer (documented in the voided record; unchanged; script `tokenize.py`).
- Final word count: **1,794** — inside the standard ±10% band (1,635–1,999). The earlier growth authorization (to ~2,500–3,000) went unused: under the source law the honest ceiling is the transcript itself, and dialogue was not padded to reach a number.
- Rewrite iteration: single approved draft; no further iteration (remaining gains within the law would require stuffing recorded speech — declined).

## Approved moves executed (all seven; nothing else)

1. **Four transcript annotations** in Ch17's exact form, recording only what the tape catches: `[\,Footsteps above with weight in them. Through the wall, the pen.\,]` (opening); `[\,A cord unwound. Two papers laid beneath the lamp beside the drum's sheet.\,]` (replacing the bare beat at the folder); `[\,Behind the wall the pen begins, draws, stops.\,]` (the silence before "Who."); `[\,The full reel cased. A new reel threaded.\,]` (close — hands Ch16 its road reel and keeps Ch17's Knocks-reel substitution evidence intact). The two other bare `[\,---\,]` beats remain bare.
2. **Fog reduction in-room only:** Sarah's decoupling turn now opens "That is the whole of it, Mr Morgan." One vocative; no tags, no other changes.
3. **Paul's folder turn rebuilt for agency** (the plant is public since Ch13 l227): "This folder was put into my hands the week I came here: two traces already inside it, dated down the margin in a hand that is not mine. Madame wished to see what I would do with it… So this is what I do with it: we open it now, before the road." His "Here." turn drops the duplicated origin sentences and goes straight to the traces.
4. **The mornings deepened inside K's speech:** before "These two are mine," he speaks the typed margin — "There is a day typed down the margin, and an hour. At that hour the ceremony had worn down into prayer, and I stood among the elders with my feet on the stone, counting; and this pen was turning in the dark of another country while I counted." Everything after stands verbatim.
5. **Ch16 duplicate and dangling antecedent removed:** "And no Keeper was near the chain. I said it when it drew… There was no morning due." is cut (Ch13's page shows him saying the opposite; Ch16's closing room and Ch17's opening own the rising-without-death argument). Sarah's stated-and-eliminated alternative ("One could still be an emergency readiness. Reggane taught us that.") and K's "It drew twice. Inside the single hour…" stand untouched.
6. **"until this morning" → "until tonight"** (nocturnal scene).
7. **Bowl recap trimmed to the recognition** ("The Bowl of the Last Prayer. … You are telling me the ground is a Bowl…"); the mechanics recap belongs to Ch1 and K's fuller Ear speech to Ch17. *(Presented as optional-recommended; author said go without striking it. The cut line — "You give its Ear the one true note… whether the note is the note." — is quoted here for one-line restoration if wanted.)*

Explicitly NOT done: Sarah's 1960 Reggane fold stays in her coat — Ch17's "Bring me the drill cabinet, all of it back to the first paper I ever folded" owns that reveal; bringing it out in Ch15 would pre-spend the cabinet. No narration anywhere. No new objects, characters, or mechanisms. Chapters 1–14 and 16–24 untouched.

## Score (single approved draft, scored fresh against 14 and 16)

| Component | Score |
|---|---:|
| Dramatic and emotional force | 16/20 |
| Architecture and causal legibility | 18/20 |
| Character depth and voice differentiation | 14/15 |
| Prose, imagery, sentence control | 13/15 |
| Canon, knowledge-state, continuity | 15/15 |
| Pacing, compression, word-count discipline | 9/10 |
| Transition and downstream payoff | 5/5 |
| **Total** | **90/100** |

Held points are the form's honest price: a narratorless three-voice room has a hard ceiling on staged force, and that austerity is the design — Ch17 retro-justifies it. Any future attempt to buy those points with narration is forbidden by the source law above.

## Validation completed

- Word count 1,794 by the documented method; envs `room` 1/1; brace balance 0; no doubled blank lines; no trailing whitespace; zero prose outside the room environment (verified programmatically); 4 annotations exactly matching Ch17's `\centerline{\textit{[\,…\,]}}` form; zero contractions in any turn (apostrophes are possessives only: Light's, Horizon's, teacher's, drum's); Paul never speaks K's name; no mid-sentence em-dash inside any turn.
- Continuity verified: Ch13 l221–267 (plant public, first knock named by K, double within the hour, mobilization orders); Ch14 interrupt and coda (drum continuous, second trace dry under the lamp); Ch16 closing room sole carrier of rising-without-death; Ch17 opening re-argues it and the cabinet reveal retains the 1960 fold.
- Concurrent-session check at write time: the sequential John sweep was inside Chapter 10; Chapters 14–16 untouched since baseline. Chapter committed with an mtime guard against the reverted state.
- **Limitation:** XeLaTeX unavailable in this environment; full-book compile pending on the author's machine. The chapter uses only established macros.

## Forward notes

- Scene map §2 still lists Ch15 at "(1,822)"; the current count is 1,794 by this pass's tokenizer. Left for the next map refresh by the session that owns the map's tokenizer, to avoid ledger contention; "pure present-day room" remains true and correct.
- No forward obligations created in any chapter.

## Voided pass (history — binding lesson)

The earlier 2026-08-14 pass added present-tense frame narration in Kailan's voice. **Violation:** in this manuscript no text reaches the reader unhandled; the Swiss-house present exists only as what the machines caught plus Paul's provenanced editorial matter. Kailan has no compiling hand in the Swiss frame; first-person grammar does not create provenance; the narration was an omniscient hand wearing his voice. The author reverted it in full. **Rule for Chapters 15 and 17: the chapter is the tape. No prose narration of the present frame, in any voice, under any justification.**

## Reopen conditions

A demonstrated contradiction (including a compile failure), a consequential change to Chapters 13–17, or an explicit author instruction. Otherwise do not continue polishing.

## Exact resume instruction

None — FROZEN. If reopened: `continue John(chapter 15)`, state the reason, and obey the source law above.
