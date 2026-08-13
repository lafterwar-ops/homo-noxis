---
name: john
description: Perfect a specified Homo Noxius manuscript chapter from diagnosis through architectural rebuild, iterative scored rewrites, adversarial audit, continuity repair, compression, and freeze. Use when the user invokes John(chapter N), asks to run or continue John on a chapter, or requests the established chapter-perfection process. Work autonomously until the chapter earns a freeze or a genuine pause is required, keep the chapter within 10 percent of its John-start word count, persist resumable status, allow newly created continuity obligations to move only into later chapters, and never create commits or push.
---

# John

Perfect one chapter of *Homo Noxius* without losing its soul. Treat `John(chapter N)` as authority to inspect and edit the chapter, its notes, continuity ledgers, and later chapters when necessary. Continue through the workflow without requesting approval for ordinary editorial judgments.

## Parse the invocation

Resolve `N` to `manuscript/chapters/chapterN-*.tex`. Fail clearly if zero or multiple files match.

- `John(chapter N)`, `John(N)`, or equivalent: start or restart work on chapter N.
- `continue John`, `continue John(chapter N)`, or equivalent: resume from `notes/john/chapter-N-status.md`.
- An explicit user constraint overrides this workflow. Record it in status.

## Non-negotiable rules

1. **Never commit or push.** Never stage unless the user explicitly asks to stage. Git inspection and diffs are allowed. The user owns all commits.
2. **Preserve user changes.** Inspect the working tree before editing. Do not overwrite unrelated or overlapping work without understanding it.
3. **No backward incoherence.** Chapter N may create obligations or provisional incoherence only in chapters `M > N`. Never knowingly make any chapter `M < N` inconsistent, less legible, or dependent on a later repair.
4. **Earlier canon constrains John.** Read Chapters 1 through N−1 and governing ledgers as fixed incoming evidence. If the desired Chapter N change would require altering an earlier chapter, do not make that change. Find a Chapter N solution. If none exists, pause and report the backward conflict.
5. **Forward repair is allowed.** Edit later chapters and ledgers when the repair is clear and bounded. Otherwise record a forward obligation with affected files, required payoff, and latest safe resolution point.
6. **Do not reopen solved material without evidence.** A possible improvement is not a defect. Reopen a locked element only for a demonstrated contradiction, failed reader effect, or consequential new instruction.
7. **Expansion precedes deletion.** Discover what the chapter needs before cutting. Later, make additions pay through replacement, merger, or compression.
8. **Scores must remain honest.** Use the fixed rubric in Phase 6B. Aim for 100 and target genuine gains of 2–3 points per iteration, but never inflate a score, reward compliance with previous advice, or damage the chapter to maximise a number.
9. **Hold the word-count envelope.** Let `W0` be Chapter N's word count at John start. Every scored draft and every paused or frozen state must remain between `0.90 × W0` and `1.10 × W0`, rounded to whole words. Brief fluctuation inside an unfinished edit is allowed; a completed iteration outside the band is not.
10. **Freeze is earned.** Continue until the freeze criteria below are satisfied or a genuine pause condition occurs.

## Persistence protocol

Use `notes/john/chapter-N-status.md` as the durable checkpoint. Create it before substantive edits and update it after every phase and material ruling.

The status file must contain:

```markdown
# John — Chapter N — Status

- Chapter: path
- State: ACTIVE | PAUSED | FROZEN
- Phase: number and name
- Last updated: ISO date/time or date
- User constraints: ...
- Working-tree baseline: relevant pre-existing modifications
- John-start word count (W0): ...
- Word-count method: ...
- Permitted word-count band: ... to ...
- Current word count: ...
- Rewrite iteration: first draft | 1 | 2 | 3 | 4 | 5

## Governing diagnosis
...

## Locked decisions
- ...

## Changes made
- file: summary

## Score history
| Draft | Score /100 | Change | Word count | Defects targeted | Verdict |
|---|---:|---:|---:|---|---|
| First complete draft | ... | — | ... | ... | baseline |

## Forward obligations (chapters > N only)
- target chapter/file: obligation, reason, latest safe resolution point

## Validation completed
- ...

## Remaining work
1. ...

## Exact resume instruction
Begin with ...
```

Before resuming, read the status file, inspect current diffs, and verify that the filesystem still matches the checkpoint. Incorporate intervening user edits rather than reverting them.

If context, token capacity, tooling, time, or another external constraint prevents safe continuation:

1. finish no half-applied edit;
2. update status precisely;
3. set `State: PAUSED`;
4. tell the user to say `continue John(chapter N)`.

Do not mark a difficult editorial judgment as a pause. Decide and continue when the evidence supports a safe choice.

## Workflow

### Phase 0 — Establish the baseline

Read Chapter N; Chapters N−1 and N+1; fixed earlier setups as needed; relevant structure, chronology, setup/payoff, object-custody, knowledge-state, voice, worldbuilding, and methodology documents; existing John status; chapter notes; imported conversations; and the current Git diff.

If `N = 23`, read [references/chapter-23-anti-key.md](references/chapter-23-anti-key.md) in full before diagnosing or editing. Treat it as a chapter-specific author instruction that supersedes the previous Chapter 23 score and any earlier assumption that complete civilisational explanation is intrinsically desirable.

Record pre-existing modifications. Separate the user's changes from John's changes when possible. Count Chapter N's words before John's substantive edits; record this as `W0` and calculate the inclusive ±10% band. Prefer `texcount` when available; otherwise use one documented deterministic method and reuse it at every checkpoint. This budget and counting method remain fixed for the entire John pass, including after resume.

### Phase 1 — Diagnose before editing

State why the chapter does or does not work as a reading experience. Test fear, desire, adventure, discovery, conflict, reversals, consequence, whether scenes perform action or merely explain ideas, whether the chapter has a soul beyond its information function, and whether the ending creates the next chapter.

Write the governing diagnosis into status. Do not edit prose yet unless fixing an obvious blocking corruption.

### Phase 2 — Map logic and architecture

Identify the fundamental dramatic question, causal spine, emotional movement, proof structure, scene and room functions, incoming setups, outgoing promises, load-bearing elements, expansion surfaces, and dead weight.

Distinguish chapter function from current furniture. Preserve the former; challenge the latter.

### Phase 3 — Expand perpendicularly

Generate approximately thirty genuinely different candidates when the chapter needs structural invention. Candidates may be people, actions, objects, failures, places, dialogue, plot machinery, ordinary life, physical obstacles, counterarguments, or recurring assets.

Do not rank while generating. Prefer inventions that solve multiple problems, activate an underused voice, create downstream returns, make abstract exposition physical, or make the world feel inhabited rather than authored solely for payoff.

If diagnosis proves the chapter already completed expansion, document that and skip directly to arbitration. Never add thirty ideas ritualistically.

### Phase 4 — Arbitrate

For each serious candidate assess problem solved, insertion point, voice activated, prerequisites, downstream returns, word and pacing cost, historical/scientific/canon risk, and whether it creates backward incoherence.

Classify it as adopted, transformed, rejected, superseded, deferred-forward, or open. Choose a compatible package rather than a pile of individually attractive ideas.

### Phase 5 — Rebuild architecture

Design the new scene-by-scene or paragraph-block architecture before polishing lines. Ensure each unit changes knowledge, power, intention, danger, relationship, or available action. Make the chapter force N+1. Record forward obligations.

### Phase 6A — Write the first complete draft

Edit the manuscript directly. Rewrite coherent scenes or rooms rather than accumulating isolated quotable sentences. Preserve LaTeX conventions and repository style.

When a change requires a clear later payoff, implement it in later chapters if safe and bounded; otherwise record it. Never repair it backward.

Complete the intended chapter architecture before scoring. Bring the chapter back inside the ±10% word-count band before treating it as a draft.

### Phase 6B — Score the first complete draft

Read the completed chapter afresh in the context of N−1 and N+1. Score it out of 100 with this fixed rubric:

| Component | Points |
|---|---:|
| Dramatic and emotional force | 20 |
| Architecture and causal legibility | 20 |
| Character depth and voice differentiation | 15 |
| Prose, imagery, and sentence control | 15 |
| Canon, knowledge-state, and continuity integrity | 15 |
| Pacing, compression, and word-count discipline | 10 |
| Transition and downstream payoff | 5 |

For each component, identify the specific evidence that prevents full marks. Award 100 only when no material defect remains under the rubric; do not treat 100 as a mandatory outcome.

Record the score, sub-scores, word count, and top three point-recovery opportunities in status. This is the baseline for iteration, not the pre-John chapter score.

### Phase 6C — Run the rewrite/rescore loop

Perform at most five scored rewrite iterations after the first complete draft.

For each iteration:

1. Select a coherent intervention package capable of earning a genuine 2–3 point improvement under the fixed rubric. Prefer causes over symptoms.
2. Predict which rubric components should improve and what the rewrite must not damage.
3. Rewrite complete dramatic units. Keep earlier chapters coherent and handle consequences only forward.
4. Return Chapter N to the fixed ±10% word-count band.
5. Read the whole chapter afresh, then rescore every rubric component without anchoring to the predicted gain.
6. Record the new score, actual change, word count, intervention, regressions, and verdict in status.
7. Keep the new draft only if it is artistically stronger overall. If the score falls or the chapter loses force despite a nominal gain, restore the best prior draft without disturbing unrelated user changes.

Aim toward 100. Stop the loop before five iterations only when:

- the chapter honestly scores 100;
- the freeze criteria are already satisfied and another rewrite would be cosmetic;
- no further 2–3 point intervention exists without score-gaming, breaking the word budget, or creating backward incoherence.

After five iterations, stop iterating even if the score is below 100. Carry remaining real defects into Phases 7–13; do not begin a sixth scored rewrite cycle.

### Phase 7 — Test causal legibility

Explain every complicated sequence in plain causal steps. If the explanation is clearer than the chapter, rewrite until a first-time reader can recover who acts, what they know, why the obvious alternative fails, what changes, and why the next action follows.

Do not confuse productive mystery with missing causality.

### Phase 8 — Differentiate voices

For each speaker or narrator, test categories noticed, recurrent question, reasoning habit, metaphor domain, sentence rhythm, and what the character refuses to say.

Useful current tendencies, subject to the text:

- Kailan: religious, spatial, optical, embodied, moral.
- Sarah: evidentiary, commercial, operational, custodial, self-indicting.
- Paul: empirical, mechanical, dry, chronologically exact, occasionally deflationary.

Reduce the shared aphoristic house style. Usually keep the physical image or the interpretation; do not automatically keep both plus an explanation.

### Phase 9 — Audit adversarially

Run two opposing readings:

1. Attack what appears strongest for contrivance, overdetermination, self-importance, convenience, over-explanation, and unearned payoff.
2. Defend what appears weakest as intentional, then determine whether that purposeful reading survives actual reader effect.

Reassess the current text independently. Do not reward a change because it followed prior advice.

### Phase 10 — Audit systems and continuity

Check chronology, ages, setup/payoff, object custody, knowledge state, disclosure order, historical/scientific plausibility, geography, title and gravure architecture, narration provenance, adjacent transitions, and earlier-chapter invariants as applicable.

Update governing ledgers. A stale ledger is a defect.

- If an edit contradicts chapter `< N`, revise or reject it.
- If it creates work in chapter `> N`, repair it now when bounded or record it as a forward obligation.

### Phase 11 — Make the payment pass

Remove redundant explanation, duplicate interpretation, repeated beats, unnecessary names, and excess aphorisms. Protect newly dramatised material. Aim for the smallest text that preserves the full experience, not the shortest chapter.

### Phase 12 — Read continuously

Read at minimum Chapters N−1, N, and N+1 without pausing to score. Expand the run when an arc crosses more chapters.

Test whether each chapter forces the next, revelation order, object and evidence travel, chronology, emotional momentum, voice recognition without labels, and whether any incoherence moved backward.

### Phase 13 — Validate and freeze

Run proportionate checks: `git diff --check`, balanced LaTeX environments, search for superseded facts or wording, compilation when available, and focused rereading of every changed passage.

Freeze only when:

- the architecture works;
- the chapter has dramatic and emotional life;
- causal action is legible;
- voices are sufficiently differentiated;
- the final word count is inside the fixed ±10% band;
- earlier chapters remain coherent;
- forward obligations are explicit and safe;
- ledgers agree with the manuscript;
- remaining issues are cosmetic or offer negligible artistic return;
- no concrete continuity defect remains inside Chapters 1 through N.

Set `State: FROZEN` in status. Record locked decisions, forward obligations, validations, and the condition under which the chapter may be reopened.

Do not continue polishing after freeze. Reopen only for a demonstrated contradiction, a consequential later change, or an explicit user instruction.

## Communication

Provide concise progress updates while working. Lead with findings or decisions, not tool activity.

At a pause, report why continuation is unsafe, where status is stored, and the exact resume phrase.

At freeze, report what changed, why the chapter is frozen, later-chapter obligations, and validation limitations.

Never report a commit because John never commits.
