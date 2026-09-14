---
name: kingjames
description: Rebuild a Homo Noxius chapter from four blind, complete rewrites by John, Patrick, Theo, and Chris, then select passages and rewrite them into one coherent manuscript. Use when the user invokes KingJames(chapter N), asks to continue KingJames, or requests the four-full-drafts and editorial-synthesis workflow. Keep KingJack unchanged; this is not its brainstorm-and-constrained-production process. Never stage, commit, or push.
---

# KingJames

Commission four fully realised versions of the same chapter. Read the versions as literature, choose the strongest compatible passages, and rewrite the assembly until it reads as one chapter. A contribution needs no agreement from another editor. Do not turn this into an intersection of recommendations, a vote, or an equal-share anthology.

KingJack and the four native editor skills remain unchanged. KingJames supplies the isolated-draft execution contract below; the native skills supply their distinct methods.

## Invocation and scope

- `KingJames(chapter N)` or `KingJames(N)`: start one new round, obtain all four full rewrites, synthesise, validate, and apply the finished chapter.
- `continue KingJames(chapter N)`: resume the latest unfinished round after checking its inputs. If no chapter is named and several rounds could be meant, ask which one.
- An explicit request for drafts only or no manuscript changes ends with the assembled candidate and a review; do not install it.
- A request to create, inspect, or amend this skill does not start a chapter round.

Resolve the target against the chapter sources actually included by `manuscript/00 Intro/chapter001-latexIntro.tex`. Require one unambiguous file. Start with `manuscript/Supporting document/00 — Canon Map & Index.md`; follow its current source hierarchy and `Current/Reference-Status.md`. Read THE VOICE in full before any prose work.

Latest explicit author decisions govern. No earlier agent score, workshop diagnosis, historical canon, or retired scene is a prompt to restore material. Carry author instructions into the round brief without inherited editorial diagnoses. Do not reopen Ravar or repair the deferred signal cadence without explicit authority for that change.

## Boundaries

1. Preserve all pre-existing work, including staged changes. Never stage, commit, push, reset, or restore the manuscript from Git HEAD.
2. All four writers start from the exact same current-text snapshot. They write private drafts, never the live chapter, other chapters, ledgers, or their normal status paths.
3. Obey the no-omniscient-narrator rule, speaker and source ownership, knowledge gates, room conventions, and explicit author locks. A performance-first draft cannot insert an external camera into a room.
4. Internal arrangement and prose may change substantially within the chosen method and author locks. Full rewrite means a complete considered version, not a quota of changed words. Strong passages may remain verbatim.
5. Default to the native skills' inclusive 90–110 percent word-count band, measured against the common baseline with one recorded deterministic method. Apply it to each completed candidate and the final assembly unless the author sets another range. Do not pad or cut merely to advertise an editor's presence.
6. Never create backward incoherence. By default only the target chapter can be installed. Other sources are read-only: record potential forward work, but reject or repair within the target any change that would leave an actual continuity contradiction. A larger repair requires explicit authority and an exact expanded write set.
7. Four independent complete manuscripts are required before synthesis. Do not substitute reports, excerpts, a sequential chain of revisions, or four roles played in one context.
8. Completed writer submissions remain immutable. Synthesis does not return to the writers to manufacture consensus.

## Round storage

Use `notes/kingjames/chapter-N/round-RR/`, taking the next unused round number. Never reuse KingJack's `notes/omega/` paths. Create files as needed with `apply_patch`; do not create empty draft placeholders that can be mistaken for submissions.

| Path within the round | Purpose / owner |
|---|---|
| `baseline.tex` | Exact immutable start-of-round target text; controller |
| `brief.md` | Shared source contract and explicit author instructions; controller |
| `status.md` | Phase, input hashes, permissions, submissions and resume point; controller |
| `john/chapter.tex`, `john/process.md` | John's complete rewrite and native work record |
| `patrick/chapter.tex`, `patrick/process.md` | Patrick's complete rewrite and native work record |
| `theo/chapter.tex`, `theo/process.md` | Theo's complete rewrite and native work record |
| `chris/chapter.tex`, `chris/process.md` | Chris's complete rewrite and native work record |
| `selection.md` | Ordered passage choices, dependencies and exclusions; synthesist |
| `assembled.tex` | Complete integrated chapter; synthesist |
| `synthesis.md` | Revision decisions, validation and resume point; synthesist |

The brief identifies the target, baseline path and hash, word-count method and allowance, explicit locks, current guide paths, authorized writes, and relevant adjacent-source paths. Do not pre-diagnose weak passages or prescribe an outline for all four writers. Let Theo consult later context at the point its own method requires; no synopsis or outgoing revelations in its cold-read prompt.

Status uses `PREFLIGHT`, `REWRITING`, `SYNTHESISING`, `VALIDATING`, `READY_TO_APPLY`, `PAUSED`, `SUPERSEDED`, or `COMPLETE`. Record:

- original live-target hash, baseline hash, input paths/hashes and author-lock version;
- starting working-tree and Git-index state, especially pre-existing edits;
- each contributor's identity, private write set, state, output hash, word count and isolation attestation;
- synthesis state, chosen backbone if any, unresolved dependencies and final hash;
- validation results, authorized installation paths, before/after hashes and whether installation occurred;
- exact remaining action and `continue KingJames(chapter N)` instruction.

Record source dependencies as they are read, including native skill versions. This permits meaningful checks after an interruption rather than trusting a stale report.

## Phase 1 — Snapshot and dispatch

At the start of each editing turn, including a resumed round, snapshot the current contents of every source or instruction file that may change; record absence for new files. Inspect the live chapter and relevant pre-existing diff. Save the exact current text as `baseline.tex` at round start, verify its hash against the source, record the initial index, count words, and prepare the brief. Keep the live chapter untouched until installation.

Spawn four independent writers using `fork_turns="none"`. Use their inherited model unless the user or applicable instructions specify otherwise. Each receives only the brief, snapshot, its native skill path, its two private output paths, and this execution contract:

> Use your complete native rewrite method, not brainstorm mode. First read your SKILL.md and all references required for this target. For this KingJames assignment, every instruction to edit the target or persist native status is redirected to your private `chapter.tex` and `process.md`. Never write the live manuscript, native status files, other chapters, or ledgers; record later obligations in your private process file. Start from the common snapshot. Do not consult previous editorial traces or any sibling submission, the selection, assembly, or controller status. Read only current source and governing references needed by your method, and record their paths and hashes. Produce the entire chapter, including retained passages, in valid project LaTeX with no omitted sections or editorial placeholders. Your process file records your actual native work, tests, word count, unresolved issues, and output hash. Attest isolation and zero live-manuscript changes. Mark COMPLETE only when the full candidate passes your native checks and the shared boundaries.

Give each writer its own method, without importing another's diagnostic apparatus:

- **John** — `.codex/skills/john/SKILL.md`: causal and emotional architecture, complete drafting, bounded iteration, continuity and compression. Keep scores private to his process; they do not rank the four submissions. Exclude old diagnoses/status even where native preflight normally consults them. Read conditional references, such as the Chapter 23 guide, when applicable; protected-text authority still applies.
- **Patrick** — `.codex/skills/patrick/SKILL.md`: playable objectives, spoken rhythm, tactics, physical action and pressure. Preserve complete prose modes, not only dialogue extracts.
- **Theo** — `.codex/skills/theo/SKILL.md`: cold read, unaided reconstruction, expectation, retention and disclosure order. Preserve its native ordering of context reads and safety checks.
- **Chris** — `.codex/skills/chris/SKILL.md`: material images, ordinary work, recurring form, social consequence and moral reversal. Preserve unresolved resonance rather than supplying symbolic keys.

The execution contract redirects native baseline, persistence and write paths, excludes earlier editorial traces, and limits writes to private work. It does not flatten the methods into a common checklist of editorial priorities. The shared author/canon boundaries remain binding.

With three child slots, run three writers then the fourth as a slot becomes available. Never reuse a writer context for a different writer or for synthesis. While writers work, the controller can check completion metadata and scope, but must not circulate partial results or steer later writers using earlier submissions.

If a submission is partial or only notes, return it to its still-isolated author for completion. For a failed context, permit one fresh retry with only the common inputs and that writer's own unfinished files. Preserve the attempt; if no complete uncontaminated draft can be obtained, pause without synthesising from three.

## Phase 2 — Accept four complete manuscripts

Check all four actual `chapter.tex` files, not just reports claiming completion:

- Each covers the whole chapter, including its opening, ending and retained material; it is not a patch, outline or selection of scenes.
- Each process record is complete, matches its draft hash, lists source dependencies and attests the firewall. A draft may preserve good original text, but an unchanged copy with only recommendations has not fulfilled a rewrite assignment.
- Word counts, hard locks and basic LaTeX structure pass. No live-manuscript or index mutation was performed by the contributors.
- The live target and recorded dependencies still match the round inputs.

Seal the four submissions. If a writer crossed the firewall, its result is not an independent fourth version; restart that contribution cleanly or pause. Report unauthorized changes without reverting someone else's work. If the underlying manuscript or author locks changed, use the version-change rule below.

## Phase 3 — Read, select, and synthesise

Use a fresh synthesist context. Give it all four sealed full drafts, the original snapshot, brief, current source/voice references and contributor process records. Its only writes are `selection.md`, `assembled.tex`, and `synthesis.md`. It must read all four manuscripts completely before choosing passages; summaries, diagnoses and numerical scores cannot substitute for reading. Read the process notes afterward for dependencies, unresolved issues and protections.

### Select movements, not trophies

Compare equivalent dramatic movements, even when versions rearrange them. Choose a chapter-level throughline and, where useful, one version as the backbone. There is no obligation to select a backbone or take material from every writer. The original is also eligible wherever it remains strongest. Do not average voices or reward convergence: one singular passage can defeat three similar alternatives.

Prefer coherent exchanges, paragraph groups or complete scenes over isolated quotable lines. Ask what the candidate does for this chapter: action, voice, emotional force, reader experience, material life, and the movement into the next passage. An elegant sentence can be a poor selection. Do not impose a minimum-change objective, a consensus threshold, a numerical ranking, or contribution quotas.

Write an ordered selection map covering the intended assembly. For each unit record:

- chosen source(s): file, stable line range or phrase anchors, and source hash;
- retain, transplant, combine, or rewrite; why it earns this place;
- incoming prerequisites and outgoing consequences: facts, objects, relationships, echoes and reveals;
- rejected incompatible alternatives and any necessary integration work.

The map is an evolving editorial plan, not a frozen production warrant. The synthesist may change a selection when the assembled reading proves it wrong, recording the reason. Avoid exhaustive sentence-by-sentence bureaucracy.

### Write the chapter as a whole

Create `assembled.tex` with every part of the chapter present. Rewrite transitions and chosen passages as needed for chronology, custody, source ownership, character voice, tempo, revelation timing and thematic restraint. These revisions may be substantial; synthesis is creative editorial work, not concatenation. Retain the qualities that made the selected versions worth choosing.

Check every transplant for its dependencies. Bring a necessary setup with a payoff, recast the payoff so it works with existing evidence, or decline it. Never import an outcome whose cause belonged to a discarded draft. Where versions contradict one another, choose a coherent account; do not bridge them with a new off-page event or an invented plot fact.

Remove doubled revelations, repeated introductions, duplicated answers and incompatible emotional resets. Preserve real changes of register belonging to characters or sources; do not smooth everyone into one polished voice. Integration can supply connective prose and local action within the authorized story, but cannot invent a new subplot, revelation, or expanded canon merely to rescue incompatible selections.

Read the complete assembly continuously, including its relationship to the adjacent chapters. Revise the selection map and prose together. The stopping test is a coherent, fully realised chapter whose particular gains survive combination, not the number of attractive passages saved. Do not start a second four-writer round automatically.

## Phase 4 — Independent check and installation

The controller independently reads the assembly and checks it against the baseline, selection map and current source boundaries. Test the chapter as a reading experience as well as checking mechanics:

- no causal gaps, unsupported callbacks, duplicated explanations, accidental revelation shifts or unearned changes of relationship;
- no narrator leakage, invented access to another mind, anonymous room interventions, or external-camera stage directions;
- preserved character distinctions, hard author decisions, incoming setups and necessary downstream facts;
- no earlier chapter needs repair and no unresolved contradiction is disguised as a forward obligation;
- word-count allowance, LaTeX environments, dialogue formatting and whitespace checks pass;
- all four full drafts remain available and unchanged, and substantial synthesis is traceable in the selection map without requiring verbatim copying.

Return concrete failures to the synthesist for repair within the private assembly. Do not bring the four writers back into a consensus meeting. Pause if repair needs new story authority; use a safe alternative selection where one exists.

Immediately before applying, recheck the live target and dependencies and verify that the required start-of-turn snapshots exist. Once checks pass, install the complete assembled chapter with `apply_patch`; never erase concurrent user work. Record the installed hash. Validate the actual installed source and run the canonical build when tools are available and the user has not excluded it. Inspect relevant rendered output when producing a PDF, using the PDF workflow. Distinguish a source defect from an environmental build limitation.

Default installation changes only the target chapter. Do not rewrite native skills, KingJack, supporting canons or other chapters as a side effect. If the author explicitly authorized an expanded repair, check and report each named file separately.

For drafts-only mode, mark completion as `delivered, not installed`. For an installed round, mark `COMPLETE` only after all required checks pass, or explicitly record which checks were unavailable and why. Do not claim submission readiness from completion of this one workflow.

## Pause, resume, and version changes

Keep incomplete drafts labelled incomplete and outside the live manuscript. At a pause record the completed phase, remaining action, hashes and exact resume command. On continuation inspect actual files before trusting status. Resume valid completed contributions instead of silently commissioning them again.

If the live target, a material source dependency, or author locks changed before installation, pause without overwriting anything. On continuation mark that round `SUPERSEDED` and start the next round from current sources with four fresh rewrites. Preserve old drafts as history, not as the new baseline. Unrelated external edits alone do not invalidate a round.

If installation already occurred before an interruption, match the recorded installed hash and resume validation; do not mistake KingJames's own edit for external drift or apply it twice. An intervening user change to the installed chapter must be preserved and the remaining action reconsidered explicitly.

## Handoff

Lead with the chapter-level result and the main passage choices. Link the four complete candidates, selection record, and final assembly; state what was installed, word-count movement, checks and any unresolved limits. Follow AGENTS.md: list each changed source/instruction file linked to its own UTF-8 unified diff in a unique `tmp/reviews/<turn-name>/` directory, compared against this turn's starting content, never against Git HEAD. A round-baseline comparison is useful in addition, not a substitute for the turn-specific diffs. Report generated PDF output separately.

Confirm that KingJack and all four native skills were left unchanged, and that nothing was staged, committed or pushed. Finish after one round.
