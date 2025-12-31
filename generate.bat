@echo off
REM Gemini Image Generator - Windows wrapper script
REM Usage: generate.bat output.png "prompt" --style style.md --aspect 16:9

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

REM Run the image generator with correct paths
uv run --directory "%SCRIPT_DIR%scripts" python main.py %* --cwd "%CD%"
