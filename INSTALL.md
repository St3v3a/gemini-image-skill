# Installation Guide

Quick setup guide for the Gemini Image Generation Claude Skill.

## Prerequisites

- **Python 3.10+** - Check with: `python --version`
- **uv** - Fast Python package manager
- **Google AI API Key** - Get from https://aistudio.google.com/apikey

## Installation Steps

### 1. Install uv (if not already installed)

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**macOS (Homebrew):**
```bash
brew install uv
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Get Your Google AI API Key

1. Visit https://aistudio.google.com/apikey
2. Sign in with your Google account
3. Click "Create API key"
4. Copy the key

**Note:** Paid tier recommended to avoid rate limits.

### 3. Configure Your API Key

**Option A: Environment Variable (Recommended)**

```bash
# Linux/macOS - Add to ~/.bashrc or ~/.zshrc
export GOOGLE_AI_API_KEY="your_api_key_here"

# Then reload your shell or run:
source ~/.bashrc  # or ~/.zshrc
```

```powershell
# Windows PowerShell - Add to $PROFILE
$env:GOOGLE_AI_API_KEY="your_api_key_here"
```

**Option B: .env File**

```bash
# Navigate to scripts directory
cd scripts

# Copy the example file
cp .env.example .env

# Edit .env and add your API key
# GOOGLE_AI_API_KEY=your_actual_api_key_here
```

### 4. Test Installation

```bash
# Navigate to scripts directory
cd scripts

# Run a test generation (dependencies will auto-install on first run)
uv run python main.py test.png "A simple blue cube on black background" --aspect 1:1
```

**First run output:**
```
Installing required dependencies... (one-time setup)
Dependencies installed successfully!
Please run the command again.
```

**Second run:**
```bash
uv run python main.py test.png "A simple blue cube on black background" --aspect 1:1
```

**Success output:**
```
Image saved to: test.png
```

## Verification

Check that everything works:

```bash
# Test basic generation
uv run python main.py test1.png "sunset over mountains" --aspect 16:9

# Test blue glass style
uv run python main.py test2.png "rocket" --style ../assets/styles/blue_glass_3d.md

# Test batch processing
uv run python main.py test.png "cube" "sphere" "pyramid" --style ../assets/styles/blue_glass_3d.md --aspect 1:1
```

If all three commands work, you're ready to go!

## Troubleshooting

### "uv: command not found"
- Install uv using the commands in Step 1 above
- Restart your terminal after installation

### "GOOGLE_AI_API_KEY not found"
- Make sure you set the API key (Step 3)
- If using environment variable, restart your terminal
- If using .env file, make sure it's in the scripts/ directory

### "API key expired"
- Generate a new API key at https://aistudio.google.com/apikey
- Update your .env file or environment variable

### Python version error
- Requires Python 3.10 or higher
- Check version: `python --version`
- Install newer Python if needed

## Next Steps

- Read [README.md](README.md) for full usage guide
- Check [SKILL.md](SKILL.md) for Claude integration details
- Review [references/best_practices.md](references/best_practices.md) for tips

## Security Reminder

⚠️ **Never commit your .env file or API keys to version control!**

The included `.gitignore` file protects you, but always verify before pushing to GitHub/GitLab.

## Support

For issues or questions:
1. Check [README.md](README.md) troubleshooting section
2. Review [references/api_capabilities.md](references/api_capabilities.md)
3. Visit Google AI documentation: https://ai.google.dev/
