# Gemini Image Generation - Portable Edition

Professional AI-powered image generation using Google's Gemini API with 7 built-in style templates.

**This is a standalone, portable package ready to use on any system!**

**Can also be installed as a Claude Code skill!** See [CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md)

## ✨ What's Included

- **7 Professional Style Templates**
  - 3 Glass styles (purple, emerald, amber)
  - 4 Other styles (neon, gold, flat, holographic)
- **Cross-Platform Support** - Windows, macOS, Linux, WSL2
- **Auto Dependency Management** - No manual setup required
- **Example Images** - Reference images for each style template

## 🚀 Quick Start

**See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide!**

### Ultra-Quick Version

1. **Install uv:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
   # OR
   pip install uv  # Any OS
   ```

2. **Get API key:** https://aistudio.google.com/apikey

3. **Configure:**
   ```bash
   cp .env.example scripts/.env
   # Edit scripts/.env with your API key
   ```

4. **Generate:**
   ```bash
   # Linux/macOS - use wrapper script
   ./generate.sh images/output.png "A vibrant sunset"

   # Windows - use batch file
   generate.bat images\output.png "A vibrant sunset"
   ```

## 📁 Folder Structure

```
gemini-image-gen-public/
├── scripts/
│   ├── main.py              # Main generator script
│   ├── pyproject.toml       # Python dependencies
│   └── .env                 # Your API key (create from .env.example)
├── assets/
│   └── styles/              # 7 style templates
│       ├── purple_glass_3d.md
│       ├── neon_wireframe.md
│       └── ... (and more)
├── images/                  # Generated images go here
├── generate.sh              # Linux/macOS wrapper
├── generate.bat             # Windows wrapper
├── QUICKSTART.md            # 5-minute setup guide
├── README_PORTABLE.md       # This file
├── README.md                # Detailed documentation
├── SKILL.md                 # Advanced features
└── .env.example             # Template for configuration
```

## 🎨 Usage Examples

### Using Wrapper Scripts (Easiest!)

**Linux/macOS:**
```bash
# Simple generation
./generate.sh images/sunset.png "Vibrant sunset over mountains"

# With style
./generate.sh images/icon.png "rocket ship" \
  --style assets/styles/purple_glass_3d.md

# Batch generation
./generate.sh images/icon.png "rocket" "database" "server" \
  --style assets/styles/neon_wireframe.md
```

**Windows:**
```batch
REM Simple generation
generate.bat images\sunset.png "Vibrant sunset over mountains"

REM With style
generate.bat images\icon.png "rocket ship" --style assets\styles\purple_glass_3d.md

REM Batch generation
generate.bat images\icon.png "rocket" "database" "server" --style assets\styles\neon_wireframe.md
```

### Direct Command (Advanced)

**Linux/macOS:**
```bash
uv run --directory scripts python main.py images/output.png "prompt" \
  --style $(pwd)/assets/styles/style_name.md \
  --cwd "$(pwd)"
```

**Windows PowerShell:**
```powershell
uv run --directory scripts python main.py images\output.png "prompt" `
  --style $PWD\assets\styles\style_name.md `
  --cwd "$PWD"
```

## 📚 Style Templates

### Glass Styles (3D Icons)
- **purple_glass_3d.md** - Royal purple frosted glass
- **emerald_glass_3d.md** - Deep emerald glass
- **amber_glass_3d.md** - Rich amber glass

### Other Styles
- **neon_wireframe.md** - Hot pink/cyan neon on black
- **gold_metallic_3d.md** - Brushed gold metal
- **minimalist_flat.md** - Soft pastel flat design
- **gradient_holographic.md** - Iridescent gradients

## ⚙️ Configuration

### API Key Setup

**Option 1: .env file (Recommended)**
```bash
# Copy template
cp .env.example scripts/.env

# Edit scripts/.env
GOOGLE_AI_API_KEY=your_actual_key_here
```

**Option 2: Environment Variable**
```bash
# Linux/macOS
export GOOGLE_AI_API_KEY="your_key"

# Windows PowerShell
$env:GOOGLE_AI_API_KEY="your_key"
```

### Aspect Ratios

- **Default:** 1:1 (square icons)

- **Override:** `--aspect 16:9` or `--aspect 4:3`

- **Available:** 1:1, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

## 🌍 Platform Support

Tested and working on:
- ✅ Ubuntu Linux (20.04+)
- ✅ macOS (Intel & Apple Silicon)
- ✅ Windows 10/11
- ✅ WSL2

## 📖 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md)** - Install as Claude Code skill
- **[README.md](README.md)** - Full detailed documentation
- **[SKILL.md](SKILL.md)** - Advanced features and examples

## 🔧 Troubleshooting

**Files saving to wrong directory?**
- Use the wrapper scripts (`generate.sh` or `generate.bat`)
- Or include `--cwd "$(pwd)"` when using direct commands

**Dependencies won't install?**
- Install uv first: https://github.com/astral-sh/uv
- Run `cd scripts && uv sync` manually

**API key not found?**
- Create `scripts/.env` from `.env.example`
- Or set `GOOGLE_AI_API_KEY` environment variable

**"uv: command not found"?**
- Install uv (see Quick Start step 1)
- Restart your terminal after installation

## 🚢 Sharing This Package

This is a complete, portable package! To share:

1. **Zip the entire folder:**
   ```bash
   cd ..
   zip -r gemini-image-gen-public.zip gemini-image-gen-public/ -x "*/\.venv/*" "*/__pycache__/*" "*/\.env"
   ```

2. **Share the zip file** - Recipients can:
   - Extract anywhere
   - Follow QUICKSTART.md
   - Start generating images!

## 📝 License

Part of the Claude Code skill ecosystem.

## 🆘 Support

- API Key: https://aistudio.google.com/apikey
- API Docs: https://ai.google.dev/
- UV Docs: https://github.com/astral-sh/uv

---

**Ready to create amazing images?** Start with [QUICKSTART.md](QUICKSTART.md)!
