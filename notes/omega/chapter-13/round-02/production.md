# KingJack Production — Chapter 13 — Round 02

- State: COMPLETE
- Target: `manuscript/chapters/chapter13-Infiltration.tex`
- Baseline SHA-256: `9B5CEABE28E155797D4D3949A2C8ADC28B30D67A19D6C037C6AE41F8C53B18CA`
- Baseline strict word count: `5333`
- Permitted band: `4800..5866`
- Final SHA-256: `001F22EA8B03A20156B5CFDED1FD616C92BBDBF0EFB00E4283B928B493F1F7F6`
- Final strict word count: `5330`
- Net strict movement: `-3`

## Authorization and precheck

- The completed arbitration SHA-256 matched `665F37EB95E3E36E91AB818BA5D924A63D9117908E299BF10470B3FCA478A38F`.
- The target SHA-256 matched the sealed baseline.
- The target strict count was `5333`.
- The target was UTF-8 without BOM and used LF line endings; CRLF count was `0`.
- Structure was `10` `\begin{room}` openings and `10` `\end{room}` endings.
- The target worktree diff and target index diff were empty.
- Each of the ten old arbitration anchors occurred exactly once.

## Production

All ten producer-executable substitutions were applied exactly once, in arbitration order. No smoothing, restructuring, or extra manuscript change was made.

The resulting target diff contains exactly ten hunks, ten removed lines, and ten added lines. Each of the ten new substitution anchors occurs exactly once. The deterministic final target hash matches the arbitration prediction, proving the sealed baseline was transformed into the exact authorized byte sequence.

## Validation

| Check | Required | Result |
|---|---:|---:|
| Final SHA-256 | `001F22EA8B03A20156B5CFDED1FD616C92BBDBF0EFB00E4283B928B493F1F7F6` | match |
| Strict word count | `5330` | `5330` |
| Permitted band | `4800..5866` | inside |
| Room openings | `10` | `10` |
| Room endings | `10` | `10` |
| Room sequence | balanced | balanced |
| UTF-8 BOM | absent | absent |
| CRLF sequences | `0` | `0` |
| `git diff --check` | clean | clean |
| Git index | empty | empty |

### Source anchors

Each adopted source boundary occurs exactly once:

- `I learned the number later through Amastan's line:`
- `He said it was a saying of his namesake`
- `Amastan told me afterward that it was the last great work of Ka-Xhian's office`
- `Amastan's line tells me that White Six's pieces remain in the archive`
- `from your testimony here`

### Custody anchors

Each checked custody boundary occurs exactly once:

- `one authorised copy of a photograph`
- `It was taken on Ka-Xhian's authority.`
- `Shield trusts the drawer.`
- `I have held that photograph.`
- `through the second camera he suspected and I watched`
- `We do not know whose hand receives it`
- `Shield carried it in, load by load`
- `White Six's pieces remain in the archive`

### Protected anchors

Each exact protected form occurs exactly once:

- `I wanted it`
- `I am the one hand`
- `None of it was chance`
- `--- It is drawing again.`
- `--- Look at the drum. It is drawing again. The same five. Now, while we are standing here.`
- `Then we will go and look at the thing itself.`

## Compliance

- Files written: the exact target and this Round 02 `production.md`, both via `apply_patch`.
- No other manuscript chapter, Round 01 file, report, status file, ledger, or editorial file was opened or changed.
- No staging, commit, push, or other mutating Git action was performed.

## Independent KingJack closure

- KingJack independently re-read the final Chapter 13 diff and confirmed that it consists of the ten authorized substitutions only: four source-boundary repairs, two oral-clarity repairs, and four bounded compressions.
- All twenty fenced arbitration blocks were checked against the produced manuscript: every old block occurs zero times and every authorized replacement occurs exactly once.
- Sarah remains the recoverable teller throughout the testimony. The revised White Six passage now assigns archive state and the children's drill history to Amastan's line, while Sarah explicitly derives the seal sequence from Kailan's testimony in the present room. The Foundation counterfactual is limited to Sarah's belief, and the files are allowed to prove only the work performed.
- The canonical count is `5330`, down `3` words (`-0.056%`) from `5333`, and remains inside `4800..5866`. The final SHA-256 is `001F22EA8B03A20156B5CFDED1FD616C92BBDBF0EFB00E4283B928B493F1F7F6`.
- The ten-room sequence, all sixty-three `\par` markers, the Horizon confession, Paul's recruitment revelation, both double-knock lines, and the final handoff remain present. UTF-8 without BOM, LF-only line endings, LaTeX environment balance, `git diff --check`, and the empty Git index all pass.
- Chapter 12 hands the speaking position to Sarah on `Amastan`; Chapter 13 returns the unfinished trial to Kailan; Chapter 14 resumes Kailan's first-person testimony. The sealed hashes of Chapters 1--12 and every historical Chapter 13 Round 01 artifact remain unchanged.
- A full `latexmk` build was attempted. MiKTeX exited before processing the manuscript with code `-1073740791` because its fresh-install setup is unfinished; this is an environment limitation, not a Chapter 13 LaTeX failure.
- No file was staged, committed, or pushed.

State: COMPLETE
