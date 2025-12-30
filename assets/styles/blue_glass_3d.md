# Blue Glass 3D Style

The style used in all `showcase/examples/` images.

## Quick Start

```bash
# Using --style flag (recommended)
uv run python main.py output.png "a gear icon" --style styles/blue_glass_3d.md

# Multiple subjects at once
uv run python main.py output.png "cube" "sphere" "pyramid" --style styles/blue_glass_3d.md

# With reference image for extra consistency
uv run python main.py output.png "rocket icon" --style styles/blue_glass_3d.md --ref styles/blue_glass_3d.png
```

## Prompt Template

Used automatically when you pass `--style styles/blue_glass_3d.md`:

```
SOLID BLACK BACKGROUND ONLY. NO gradients, NO vignettes, NO fog, NO environmental elements. Premium 3D render of glass objects ONLY. NO TEXT. {subject}. All objects are thick frosted royal blue glass (#1e3a8a). Sharp Electric Cyan (#00D4FF) rim lighting on top edges. Soft internal volumetric glow. Minimal mirrored reflection beneath objects only. Glass objects centered in frame. Background must be pure solid black (#000000).
```

## Color Palette

| Element | Hex | Description |
|---------|-----|-------------|
| Glass Body | `#1e3a8a` | Royal blue, frosted |
| Rim Lighting | `#00D4FF` | Electric cyan, sharp edges |
| Internal Glow | White/Cyan | Soft, volumetric |
| Background | `#000000` | Pure black |

## Material Properties

- **Opacity:** ~80% semi-transparent
- **Finish:** Satin/frosted (not glossy)
- **Feel:** Heavy, physical, not ghostly
- **Refraction:** Internal depth and light scattering

## Prompt Principles

1. **Front-load prohibitions** - Start with "SOLID BLACK BACKGROUND ONLY. NO gradients..."
2. **Single dense paragraph** - Gemini responds better to flowing prose than bullets
3. **Explicit black background** - End with "Background must be pure solid black (#000000)"
4. **Describe literally** - "4 circular nodes" not "milestone markers"

## What NOT to Include

- Gradients, vignettes, fog, environments
- Text, titles, labels
- Warm colors (only blue, cyan, white, black)
- Human characters
- Circuit board patterns
- Flat/sticker appearance

## With Reference Image

When using `--ref`, the reference provides the WHAT (shapes/icons), your prompt provides the HOW (style):

```bash
# Reference defines the icons, prompt defines the style
uv run python main.py output.png \
  "Replicate the exact icons from reference. Thick frosted royal blue glass (#1e3a8a). Electric Cyan (#00D4FF) rim lighting. Solid black background. No text." \
  --ref original_icons.png --aspect 16:9
```

## Examples Generated With This Style

See `showcase/examples/`:
- `roadmap.png` - Flask, test tubes, pathway nodes, rocket
- `agentic_coding.png` - Terminal, robot, floating shapes
- `ai_agents.png` - Pyramid wireframe, paperclip abstract
- `local_ai.png` - GPU render
- `llm_fundamentals.png` - Python + TypeScript logos
