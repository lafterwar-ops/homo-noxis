---
name: kingjack
description: Orchestrate a complete Homo Noxius chapter round by running John, Patrick, Theo, and Chris as blind independent brainstorm agents, waiting for four private process traces, neutrally arbitrating their non-redundant contributions, and applying only the accepted changes through a separate constrained producer. Use when the user invokes KingJack(chapter N), asks to continue KingJack, or requests the four-agent perpendicular brainstorm, arbitration, and production workflow. Preserve resumability, existing work, the 10 percent word-count envelope, and the user's exclusive ownership of staging and commits.
---

# KingJack

Run one controlled multi-process editorial round. KingJack is a controller, not a fifth critic: do not add an editorial diagnosis of your own, vote among agents, or let production reopen arbitration.

## Parse the invocation

Resolve `N` to exactly one `manuscript/chapters/chapterN-*.tex` file.

- `KingJack(chapter N)` or equivalent: create the next numbered round and run it to completion.
- `continue KingJack(chapter N)` or equivalent: resume the latest round whose state is neither `COMPLETE` nor `SUPERSEDED`. A version-mixed round cannot resume on its old baseline; mark it `SUPERSEDED` and create the next numbered round from the current chapter.
- If zero or multiple chapter files match, stop without writing a round.

## Non-negotiable rules

1. Never stage, commit, or push. The user owns Git history. Record the initial index state and leave it untouched.
2. Preserve all pre-existing changes. Treat the current chapter text as the round baseline; never restore from `HEAD` merely because it differs.
3. Enforce the manuscript's absolute ban on omniscient narration and all explicit user-frozen plot, form, room, outcome, and character decisions.
4. Never create backward incoherence. Reject any intervention requiring a change to chapter `M < N`. Permit later-file production only when arbitration names the exact `M > N` file and bounded repair; otherwise record a forward obligation.
5. Keep every produced target chapter within 90–110 percent of its KingJack-start word count. Treat the band as a boundary, not a goal.
6. Do not arbitrate until all four independent reports are complete and uncontaminated. Do not produce until arbitration is complete.
7. Never overwrite a completed round or completed contributor report.
8. If independent subagent contexts are unavailable, pause. Never impersonate four agents sequentially in KingJack's own context.

## Round storage and persistence

Store each run under `notes/omega/chapter-N/round-RR/`, using the next unused positive two-digit round number. Existing flat reports or completed round directories remain immutable history.

Create these files before dispatch:

- `john.md`
- `patrick.md`
- `theo.md`
- `chris.md`
- `arbitration.md`
- `production.md`
- `kingjack-status.md`

Initialize each contributor report with its agent name, target chapter, round, assigned skill path, `State: READY`, private writable path, manuscript read-only rule, and cross-agent firewall. Initialize arbitration and production as waiting. Use `apply_patch` for all project-file creation and editing.

Maintain `kingjack-status.md` after every transition:

```markdown
# KingJack — Chapter N — Round RR

- State: PREFLIGHT | BRAINSTORMING | ARBITRATING | PRODUCING | PAUSED | SUPERSEDED | COMPLETE
- Chapter: path
- Baseline SHA-256: ...
- Baseline word count and method: ...
- Permitted band: ...
- Working-tree baseline: ...
- Git-index baseline: ...
- Authorized write set: ...

## Contributors
| Agent | Report | State | Firewall | Manuscript movement |
|---|---|---|---|---|

## Arbitration
...

## Production
...

## Validation
...

## Remaining work
...

## Exact resume instruction
...
```

Completed contributor reports are sealed inputs. Never ask their authors to revise them after exposure to another trace.

## Phase 0 — Preflight

1. Inspect the target, relevant existing diff, repository instructions, current index state, and any explicit user locks.
2. Hash the exact target and record a deterministic word count. Calculate the fixed 90–110 percent band.
3. Create the next round directory and files. Limit the round's authorized writes to those seven files until production.
4. Set status to `BRAINSTORMING` only after every private path and firewall exists.

Do not create generic editorial hints in report templates. A neutral header must not tell an agent where a defect supposedly lies.

## Phase 1 — Dispatch four blind brainstorms

Spawn John, Patrick, Theo, and Chris in fresh independent contexts with no inherited conversation history. Use `fork_turns="none"` when the collaboration system provides it. Give each agent only:

- its complete project-local `SKILL.md` path: `.codex/skills/john/SKILL.md`, `.codex/skills/patrick/SKILL.md`, `.codex/skills/theo/SKILL.md`, or `.codex/skills/chris/SKILL.md`;
- `Agent brainstorm(chapter N)`;
- the target chapter path;
- current explicit user locks, without earlier diagnoses;
- its one round-private report path;
- permission to read only indispensable hard canon allowed by its skill;
- an absolute prohibition on every sibling report, arbitration, production, KingJack status, John/agent status, manuscript edit, ledger edit, staging, commit, and push.

Require each contributor to use its native process, write only its assigned report, set `State: COMPLETE`, record manuscript movement `0`, and explicitly attest firewall compliance.

Run as many contributors concurrently as capacity allows. If KingJack occupies one slot and only three child slots remain, dispatch any three, then dispatch the fourth as soon as a slot opens. Simultaneity is not evidence of independence; fresh context and the firewall are. Never reuse a contributor context for another contributor, arbitration, or production.

Wait for all four. Send concise progress updates, but do not inspect or summarize partial conclusions while another contributor is still working.

### Contributor failure

- If a contributor stops with a mechanical or capacity failure before completing, retry once in a new context against only its own incomplete report and admissible inputs.
- If it remains incomplete, contaminated, or changes an unauthorized file, set KingJack to `PAUSED`. Do not substitute KingJack's analysis or proceed with three reports.
- If the target hash changes from external editing before all four finish, pause the round as version-mixed. Do not arbitrate it. Preserve the reports. On explicit continuation or reinvocation, mark that round `SUPERSEDED` and start a new round with four fresh reports against the new baseline.

## Phase 2 — Integrity gate

Before arbitration, verify:

- all four reports are substantive and marked `COMPLETE`;
- each contains explicit firewall compliance and zero manuscript movement;
- the target hash still equals the baseline;
- only authorized round files changed through this phase;
- KingJack did not alter the Git index;
- no report contains unresolved placeholders.

Record only completion and integrity metadata in status. Do not copy diagnoses between reports.

## Phase 3 — Neutral arbitration

Spawn a fresh arbiter with no inherited conversation history. Its readable task inputs are the four sealed reports, the current target chapter, explicit user locks, and only indispensable canon needed to reject an illegal change. Its only writable file is `arbitration.md`; it has no manuscript authority.

Require arbitration to:

1. map genuine convergence, orthogonal complementarity, disagreement, and unique contributions;
2. judge claims against the current text rather than agent prestige, vote count, eloquence, or promised score gain;
3. protect strengths and productive ambiguity identified by any trace;
4. classify every serious proposal as accepted, transformed, rejected, deferred, or out of scope, with a reason;
5. select a compatible minimum-sufficient package rather than accumulate all attractive suggestions;
6. introduce no free-standing fifth diagnosis or invention unsupported by at least one trace;
7. produce an ordered, executable production brief with exact loci, invariants, authorized files, forbidden changes, word-count boundary, and validation requirements.

The arbiter may synthesize two compatible contributions only when the synthesis is directly traceable to both and smaller or safer than applying them separately. It must never average numerical scores or treat agreement as proof.

KingJack verifies that `arbitration.md` is complete and executable. If a material ambiguity remains, defer that intervention; do not expose contributors to one another by asking for post-hoc consensus.

## Phase 4 — Constrained production

Recheck the target hash against the baseline. Then spawn a fresh producer with no inherited conversation history.

The producer may read only:

- `production.md`;
- completed `arbitration.md`;
- the target chapter;
- any exact later chapter or canon file explicitly authorized by the arbitration brief.

The producer must never read the four source reports. It applies only accepted interventions, in order, using the smallest sufficient textual movement. It may make local grammatical joins required by an accepted deletion or insertion, but may not revive rejected ideas, solve deferred questions, or add an improvement of its own.

Authorize writes only to `production.md`, the target chapter, and exact later files named by arbitration. Require `production.md` to record the baseline, each applied intervention, any departure, changed files, word counts, and validation. Any non-mechanical departure requires a pause rather than silent re-arbitration.

## Phase 5 — Verify and close

KingJack independently inspect the final diff and confirm:

- every manuscript change maps to an accepted brief item;
- rejected, deferred, and out-of-scope ideas did not enter production;
- narrator, source, room, chronology, custody, frozen canon, and adjacent transitions remain legal;
- no earlier chapter changed;
- any later change was explicitly authorized and bounded;
- the target remains inside the fixed word-count band;
- LaTeX structure, dialogue pairs, ornaments, and `git diff --check` pass;
- the configured manuscript build passes when the environment permits, otherwise record the exact environmental limitation;
- pre-existing work and the Git index remain untouched;
- nothing was staged, committed, or pushed.

Set status and production to `COMPLETE`, recording final hashes, word counts, accepted changes, deferred issues, validation, and file links. Do not run another round automatically.

## Pause and resume

Pause only for an incomplete/contaminated trace, mixed target version, ambiguous production authority, backward-canon requirement, unsafe overlapping external edit, unavailable independent contexts, or exhausted execution capacity.

Before pausing, leave no half-applied manuscript edit. Update status with the exact completed phase, immutable inputs, remaining work, and `continue KingJack(chapter N)` instruction. On resume, verify hashes and current diffs before continuing; never silently restart completed contributors or overwrite their reports. If the pause is version-mixed, supersede rather than resume that round and begin the next numbered round with four fresh contexts.

## Communication

Report phase transitions and integrity facts, not partial editorial conclusions. At completion, lead with what changed, link the round's arbitration and production records, state word-count movement and validation limitations, and reaffirm that nothing was staged, committed, or pushed.
