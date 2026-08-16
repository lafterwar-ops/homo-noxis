# ZEUS — round scheduler & state ledger

*Zeus chains KingJack rounds across the book. KingJack completes one chapter and stops by design ("Do not run another round automatically"); Zeus supplies the cadence. This file is Zeus's durable memory and operating spec: any session rebuilding Zeus starts by reading it.*

## Configuration (author-set, 2026-08-14)

- Mode: **EXECUTOR** — Zeus's session runs the full KingJack round itself (four blind persona agents in fresh parallel firewalled contexts, neutral arbiter, constrained producer), per `.codex/skills/kingjack/SKILL.md`, adapted to this environment's agent system. KingJack's rule 8 is honored: four genuinely independent contexts, never sequential impersonation.
- Start chapter: ~~1~~ **12** — author override, 2026-08-14: chapters 1–11 are declared complete by the author; Zeus treats ≤11 as done regardless of `notes/omega/` contents, and the ladder begins at 12. (The author may override the next target again at any time; record overrides in the log below.)
- Last chapter: **24** (chapter24-Whole). After the round for 24 completes, Zeus announces and stops.
- Cadence: **desktop scheduled task** ("Zeus", run on your computer) — each firing is a fresh session with folder access that performs exactly one tick: check, and at most one full KingJack round, then end. The card's schedule provides the cadence; overlapping firings exit instantly via the guards below. (The earlier in-chat 20-minute timer chain is DISARMED, 2026-08-14 — its pending trigger was deleted; if a stray "ZEUS TICK" message ever appears in the old session, it is void.)
- Invocation name: the author wrote "KingJames" once; the skill on disk is `kingjack` — Zeus invokes **KingJack(chapter N)**.

## Tick protocol (run on every wake)

1. **Bridge check.** If the desktop/folder is unreachable: log a quiet skip, reschedule +20, end.
2. **Activity guard.** If any file under `manuscript/` or `notes/` (excluding Zeus's own) changed in the last 20 minutes, another hand is working: skip, reschedule +20. (KingJack's baseline-hash rule additionally protects any round from mid-flight external edits.)
3. **Position.** Scan `notes/omega/chapter-N/round-RR/kingjack-status.md`:
   - X = max(highest N whose latest round is `COMPLETE`, the author-declared floor — currently **11**); next target = X+1.
   - No rounds anywhere → next target = floor+1 (currently 12).
   - Any round `PREFLIGHT/BRAINSTORMING/ARBITRATING/PRODUCING` with a live executor → in the loop: skip, reschedule.
   - Any round `PAUSED`, or in-flight with no live executor (crashed): **notify the author (push + message), hold, reschedule.** Zeus never auto-continues a paused round — pauses signal contamination, version-mix, or ambiguity that KingJack reserves for judgment.
4. **Stop rule.** If next target > 24: announce the ladder complete, final-log, do NOT reschedule.
5. **Invoke.** Otherwise run **KingJack(chapter next)** to completion in this session, honoring every KingJack rule (no staging/commits to git; author owns history; word band; source law; round files under `notes/omega/chapter-N/round-RR/`; commits of files to the author's disk use mtime guards).
6. **Log and chain.** Update this ledger, commit it, schedule the next tick +20 minutes from round end.

Notifications: a session message on each completed chapter; push notification only on PAUSED/blocked, bridge lost repeatedly, or the final stop.

## State

- Zeus armed: 2026-08-14
- Completed: **through chapter 13** (1–11 author declaration; 12 and 13 by KingJack rounds-01, COMPLETE 2026-08-14, manual Zeus ticks in the cloud session)
- Next target: **chapter 14** (inherits chapter-13/round-01 arbitration §6 records, incl. the Ch14 read-check owed from the chapter-12 round)
- Chain status: **AUTONOMOUS CHAIN RE-ARMED in the cloud session** (author instruction 2026-08-14: "click Go and come back tomorrow"). Protocol v2: each tick schedules the NEXT tick (+50 min) BEFORE opening its round, so a crashed round is found and resumed by the following tick via its status file's Exact resume instruction; quiet skips reschedule +20; a rule-PAUSED round push-notifies the author and holds; after chapter 24 completes, push-notify and stop — no further ticks. The desktop-card option remains available but is not the active executor.

## Log

- 2026-08-14 — Zeus built and armed. Config: executor mode, stop=24, 20-minute cadence. Original start=1.
- 2026-08-14 — **Author override:** chapters 1–11 declared complete; next target set to chapter 12.
- 2026-08-14 — **Migration:** author wants Zeus visible and controllable as a scheduled-task card with its own windows. In-chat timer deleted; protocol unchanged; executor is now each firing of the desktop task. Ledger remains the single source of truth across runs.
- 2026-08-14 — Chapters 12 and 13 completed by manual Zeus ticks (KingJack rounds-01, clean).
- 2026-08-14 — **Autonomous chain re-armed** in the cloud session on author instruction ("The entire point of this is for me to click Go and come back tomorrow"). Ladder runs 14→24 unattended; ~50 min/round observed pace; author's desktop must stay awake/online (Keep awake is on). NOTE to author: ensure the other (Codex) ladder stops at chapter 11 — the partition ≤11/≥12 is what keeps the two executors collision-free.
