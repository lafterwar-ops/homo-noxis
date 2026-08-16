@echo off
rem Installs the five Homo Noxius skills into .claude\skills (Claude's project-local skills folder).
rem Master copies live in .codex\skills — re-run this file whenever you edit them there.
xcopy /E /I /Y "%~dp0claude-skills" "%~dp0.claude\skills"
echo.
echo Done. john, patrick, theo, chris and kingjack are now in .claude\skills.
pause
