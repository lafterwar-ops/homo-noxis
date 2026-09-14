# KingJames — Chapter 16 — Shared writer brief

- Round: 01, 9 September 2026.
- User invocation: `KingJames(chapter 16)`.
- Repository: `C:/Francois/Writting/HomoNoxisGithub`.
- Live target (read-only to contributors): `manuscript/chapters/chapter16-Horizon.tex`.
- Common immutable source: `notes/kingjames/chapter-16/round-01/baseline.tex`.
- Baseline SHA-256: `F72905A8E623636154549549B320F4B486F8EB50B7DD0677C73AB0E97A4C5844`.
- Baseline prose word count: 4,877; inclusive completed-draft band: 4,390–5,364.
- Before/after neighbours: `manuscript/chapters/chapter15-Knocks.tex`, `manuscript/chapters/chapter17-Mock.tex`. Read at the point required by your native method; Theo must perform its cold read and unaided reconstruction before later material.
- Canon entry point: `manuscript/Supporting document/00 — Canon Map & Index.md`; classifications: `manuscript/Supporting document/Current/Reference-Status.md`.
- Maintained guides: `Current/Story-Canon.md`, `Current/Chronology.md`, `Current/Mechanisms.md`, `Current/Continuity-Ledgers.md` under Supporting document. Follow the source hierarchy, not historical locks.
- Read THE VOICE in full: `manuscript/Supporting document/04 — Story & Series — Structure & Craft/THE VOICE — Prose Style Canon (how we write).md`.

## Author instructions and locks

Produce a complete independent chapter rewrite through your own native method. Strong original passages may remain; a report or samples alone are not a submission. Do not import previous agent diagnoses or scores. Do not see sibling drafts or reports.

Preserve the author's recent flight decision: a Jamaican diplomatic flight to Geneva, Captain Billy, then the family's helicopter. Keep the newly authored Billy encounter, its friendliness and modest dialect touch: dialogue names him `Capt'n Billy`; preserve the remembered triple `You wanna go snorkelling? You wanna eat lobster? You wanna smoke weed?` and `You can do all dees tings. Just let Capt'n Billy know.` The invitation concerns a future visit to Jamaica. Do not add more stereotyped speech. K does not yet speak English; translation must remain possible. Do not revert the flight to a commercial cabin.

`Noxius` has not been coined at the narrated flight/manual stage: it cannot be spoken there. Use Mountain speech / your language or the existing appropriate wording. Do not broaden this into editing other chapters.

No omniscient narrator, including room stage directions. Every account has a teller and available source. Use established room speaker labels where needed and textless centreline pauses. The author rejects fake opposition between intelligent people, mechanical correction-pairs, repeated glosses and relentlessly short sentences. Follow THE VOICE without flattening concrete life or character emotion.

Keep explicit current character, outcome, source and knowledge decisions. Do not reopen Ravar, gender rules or deferred signal-cadence repairs. Current included sources govern inherited story facts. No backward inconsistency, and do not leave an actual later contradiction requiring unapproved files to be rewritten.

## Private-draft execution contract

Read your entire native SKILL.md and required references. Run the FULL rewrite method, not brainstorm mode. Redirect every native manuscript edit and native status write to your assigned private `chapter.tex` and `process.md`. Those two files are your only authorized writes. The live manuscript, other chapters, canon files, native notes/status, KingJack and all skills are read-only. Record proposed later obligations in your process file instead of editing them. Never stage, commit, push, reset or restore user work.

Admissible evidence: common baseline, latest instructions in this brief, current sources and indispensable canon as permitted by your native method. No prior diagnoses, imported critiques, sibling files, controller status, selection or assembly. Use narrow searches limited to permitted sources; do not search all notes.

Record your native phases, meaningful choices, tests, exact input paths/hashes, word count and output hash in your process file. Attest firewall compliance and zero live-manuscript edits. Mark `State: COMPLETE` only after the complete chapter and native safety checks pass. Return just completion metadata and file paths to the controller, not partial editorial findings. The controller performs canonical publication/build later; do not write build products outside your two-file allowance.

## Common deterministic word-count method

Run this PowerShell code against your private file, substituting only its path. It removes comments, chapter heading, environments and command names while retaining textual arguments, then counts Unicode words/numbers with internal apostrophes/hyphens. Use the same method at all checkpoints.

```powershell
$kjCountText = Get-Content -LiteralPath 'PATH-TO-YOUR-CHAPTER' -Raw
$kjCountText = [regex]::Replace($kjCountText,'(?m)(?<!\\)%.*$','')
$kjCountText = [regex]::Replace($kjCountText,'\\(?:begin|end)\{[^}]+\}|\\typesetchapter\{[^}]*\}\{[^}]*\}','')
$kjCountText = [regex]::Replace($kjCountText,'\\[A-Za-z@]+\*?(?:\[[^\]]*\])?','')
[regex]::Matches($kjCountText,"[\p{L}\p{N}]+(?:['’\-][\p{L}\p{N}]+)*").Count
```

## Environment note

The normal shell helper has been failing on this machine; a justified `exec_command` with `sandbox_permissions: require_escalated` works. Use `apply_patch` for content edits. If the direct patch tool fails, the working Windows fallback is a PowerShell single-quoted here-string passed to `C:/Users/Multiple Monitors/AppData/Local/OpenAI/Codex/bin/1e3e57cdf0634c02/codex.exe --codex-run-as-apply-patch`. Do not spend repeated attempts on the broken helper. No model override has been requested.
