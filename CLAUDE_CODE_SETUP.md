# Using as a Claude Code Skill

This package can be easily used as a Claude Code skill! Follow these steps:

## Installation

### Step 1: Copy to Skills Directory

```bash
# Copy the entire directory to your Claude Code skills directory
cp -r gemini-image-gen-public ~/.claude/skills/gemini-image-gen
```

Or on Windows:
```powershell
xcopy /E /I gemini-image-gen-public %USERPROFILE%\.claude\skills\gemini-image-gen
```

### Step 2: (Optional) Add Command Shortcut

Create a command file to invoke the skill easily with `/image`:

```bash
# Copy the command file
cp gemini-image-gen-public/image-command.md ~/.claude/commands/image.md
```

Or on Windows:
```powershell
copy gemini-image-gen-public\image-command.md %USERPROFILE%\.claude\commands\image.md
```

### Step 3: Configure API Key

Set your Google AI API key (if not already set):

```bash
# Add to ~/.bashrc or ~/.zshrc (Linux/macOS)
export GOOGLE_AI_API_KEY="your_key_here"

# Or add to PowerShell profile (Windows)
$env:GOOGLE_AI_API_KEY="your_key_here"
```

Or create `.env` in your project directory:
```
GOOGLE_AI_API_KEY=your_key_here
```

## Usage with Claude Code

Once installed, Claude Code will automatically detect the skill!

### Using the /image Command (if installed)

```
/image "a vibrant sunset over mountains"
/image "rocket icon" --style purple_glass_3d
/image "database icon" --style neon_wireframe --aspect 1:1
```

### Direct Invocation

Claude Code can also invoke the skill directly when you request image generation:

```
User: "Can you generate a purple glass 3D icon of a rocket ship?"
Claude: [Uses gemini-image-gen skill automatically]
```

## Available Styles

- **purple_glass_3d** - Royal purple frosted glass
- **emerald_glass_3d** - Deep emerald glass
- **amber_glass_3d** - Rich amber glass
- **neon_wireframe** - Hot pink/cyan neon wireframe
- **gold_metallic_3d** - Brushed gold metal
- **minimalist_flat** - Soft pastel flat design
- **gradient_holographic** - Iridescent gradients

## File Locations After Installation

```
~/.claude/
├── skills/
│   └── gemini-image-gen/
│       ├── SKILL.md              # Skill definition (auto-detected)
│       ├── scripts/main.py       # Main script
│       ├── assets/styles/        # 7 style templates
│       └── ...
└── commands/
    └── image.md                  # /image command (optional)
```

## Troubleshooting

**Skill not detected?**
- Ensure `SKILL.md` exists in `~/.claude/skills/gemini-image-gen/`
- Restart Claude Code

**Command not working?**
- Ensure `image.md` is in `~/.claude/commands/`
- Check that the path in the command file is correct

**Images saving to wrong location?**
- The skill automatically handles paths using `--cwd` parameter
- Images save to your current working directory

## Documentation

- **QUICKSTART.md** - 5-minute setup guide
- **README.md** - Full documentation
- **SKILL.md** - Skill definition and advanced features
