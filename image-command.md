---
description: Generate images using Google's Gemini API with style templates
argument-hint: "[prompt]" [--style style-name] [--aspect ratio]
---

# Generate Image with Gemini AI

Generate professional images using Google's Gemini API with built-in style templates.

## How to Use This Command

When the user invokes `/image`, execute the gemini-image-gen Python script to generate images based on their request.

### Command Structure

**IMPORTANT:** Replace `SKILL_PATH` with the absolute path to where you installed the skill:
- Linux/macOS: `~/.claude/skills/gemini-image-gen`
- Windows: `%USERPROFILE%\.claude\skills\gemini-image-gen`

```bash
uv run --directory SKILL_PATH/scripts python main.py OUTPUT_PATH "PROMPT" [OPTIONS] --cwd "$(pwd)"
```

**Important:** Always include `--cwd "$(pwd)"` to ensure files save to the correct location!

### Available Style Templates

The skill includes 7 professional style templates located in `SKILL_PATH/assets/styles/`:

**Glass Styles:**
- `purple_glass_3d.md` - Royal purple frosted glass with violet rim lighting
- `emerald_glass_3d.md` - Deep emerald glass with lime green rim lighting
- `amber_glass_3d.md` - Rich amber glass with golden rim lighting

**Other Styles:**
- `neon_wireframe.md` - Hot pink/cyan glowing wireframe on black
- `gold_metallic_3d.md` - Brushed gold metal with warm highlights
- `minimalist_flat.md` - Soft pastel flat 2D design on white
- `gradient_holographic.md` - Iridescent purple-pink-cyan gradients

### Aspect Ratios

Available ratios: `1:1`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
Default: `1:1` (square)

## Usage Examples

### Basic Generation

```bash
# Simple image (saves to current directory)
uv run --directory SKILL_PATH/scripts python main.py images/sunset.png \
  "A vibrant sunset over mountains" --cwd "$(pwd)"
```

### With Style Template

```bash
# Purple glass 3D style
uv run --directory SKILL_PATH/scripts python main.py images/rocket.png "rocket" \
  --style SKILL_PATH/assets/styles/purple_glass_3d.md \
  --cwd "$(pwd)"

# Neon wireframe style
uv run --directory SKILL_PATH/scripts python main.py images/database.png "database" \
  --style SKILL_PATH/assets/styles/neon_wireframe.md \
  --cwd "$(pwd)"
```

### Different Aspect Ratios

```bash
# YouTube thumbnail (16:9)
uv run --directory SKILL_PATH/scripts python main.py images/thumb.png \
  "AI tutorial thumbnail" \
  --aspect 16:9 \
  --cwd "$(pwd)"

# Square icon (1:1 - default)
uv run --directory SKILL_PATH/scripts python main.py images/icon.png \
  "cloud storage icon" \
  --style SKILL_PATH/assets/styles/purple_glass_3d.md \
  --cwd "$(pwd)"
```

### Batch Processing

```bash
# Generate multiple variations
uv run --directory SKILL_PATH/scripts python main.py images/icon.png \
  "rocket" "database" "server" \
  --style SKILL_PATH/assets/styles/neon_wireframe.md \
  --cwd "$(pwd)"

# Outputs: icon_1.png, icon_2.png, icon_3.png
```

### Image Editing

```bash
# Edit existing image
uv run --directory SKILL_PATH/scripts python main.py images/edited.png \
  "Change background to solid blue" \
  --edit images/original.png \
  --cwd "$(pwd)"
```

## Execution Workflow

1. **Parse user request** - Extract prompt, style preference, aspect ratio
2. **Determine output path** - Use `images/` directory by default
3. **Build command** - Include all necessary parameters
4. **Execute** - Run the uv command with proper paths
5. **Verify** - Check that image was created successfully

## Common Patterns

**User says:** "Create a purple glass icon of a rocket"
**Execute:**
```bash
uv run --directory SKILL_PATH/scripts python main.py images/rocket.png "rocket" \
  --style SKILL_PATH/assets/styles/purple_glass_3d.md \
  --cwd "$(pwd)"
```

**User says:** "Generate a YouTube thumbnail for an AI tutorial"
**Execute:**
```bash
uv run --directory SKILL_PATH/scripts python main.py images/thumbnail.png \
  "AI tutorial thumbnail with vibrant colors" \
  --aspect 16:9 \
  --cwd "$(pwd)"
```

**User says:** "Make 3 neon icons: rocket, database, cloud"
**Execute:**
```bash
uv run --directory SKILL_PATH/scripts python main.py images/icon.png \
  "rocket" "database" "cloud" \
  --style SKILL_PATH/assets/styles/neon_wireframe.md \
  --cwd "$(pwd)"
```

## Notes

- First run auto-installs dependencies (takes ~10 seconds)
- Requires Google AI API key (set via `GOOGLE_AI_API_KEY` environment variable or `.env` file)
- All paths are resolved relative to the user's current working directory
- The `--cwd "$(pwd)"` parameter is critical for correct file placement
