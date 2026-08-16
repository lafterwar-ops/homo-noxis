# KingJack Production — Chapter 17 — Round 01

- Preconditions: PASS. Arbitration SHA-256 `900980A478D9B86777EA38E4BF33F572AFFE1F3C1997A4C39E05B915DA460F4D`; target baseline SHA-256 `57CDE7CB13ACD02E2B0DFFA635E57ED0E01E14AE647AAD2C08352F2660B4DB73`; canonical count `4382`. Exact old block occurred once and exact replacement block occurred zero times before editing.
- Operation: Applied only the sealed Edit 1 substitution to `manuscript/chapters/chapter17-Mock.tex` via `apply_patch`; no cleanup, normalization, staging, commit, or push.
- Validation: PASS. Exact old block `0`, exact replacement block `1`; SHA-256 `42D1E418B46B16649480EE6604450E78F060520388CE70FC04AA181F988A8BBC`; canonical count `4370`; `24588` bytes; UTF-8 without BOM; LF `370`; CRLF `0`; terminal LF present; room `1/1`; scripture `2/2`.
- Diff/index: PASS. Target-only `git diff` has exactly one hunk with normal context; `git diff --cached --quiet` confirms an empty index.
- Build: Not run, because the sealed files do not expose the established full-book root or command.

## Independent KingJack closure

- Recomputed target SHA-256 `42D1E418B46B16649480EE6604450E78F060520388CE70FC04AA181F988A8BBC`, canonical count `4370`, byte count `24588`, LF `370`, CRLF `0`, no BOM, and terminal LF: PASS.
- Recomputed form: room `1/1`, scripture `2/2`, centerline cues `16`, prose paragraphs `0`: PASS.
- Source-order audit: the disputed soldiers/rig assertion is absent before Jean-Charles enters; the image then establishes four trucks, a rig, and the perimeter before the dialogue identifies soldiers: PASS.
- Live-record audit: outside the two scripture environments, every nonblank content line is dialogue, an audible/minimal documentary cue, or the chapter/room wrapper; no omniscient narration or retrospective interiority was introduced: PASS.
- Boundary audit: Chapter 16's continuing drum runs directly into Chapter 17's emergency dialogue; Chapter 17's lawn tape ending remains compatible with Chapter 18's later Greater Seal framing room and Paul takeover: PASS.
- Scope audit: the target diff remains exactly one hunk and the Git index remains empty: PASS.
- Full-book build: attempted independently with `latexmk` against `manuscript/00 Intro/chapter001-latexIntro.tex`, directing output to the system temporary directory. MiKTeX stopped before manuscript processing because its fresh-install setup is unfinished; this is an environment limitation, not a detected manuscript failure.
- Word movement: `4382 -> 4370` (`-12`, approximately `-0.27%`), inside the fixed `3944..4820` band.
- Git: nothing staged, committed, or pushed.

State: COMPLETE
