#!/bin/bash
# Gemini Image Generator - Convenient wrapper script
# Usage: ./generate.sh output.png "prompt" [--style style.md] [--aspect 16:9]

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the image generator with correct paths
uv run --directory "$SCRIPT_DIR/scripts" python main.py "$@" --cwd "$SCRIPT_DIR"
