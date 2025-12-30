# Gold Metallic 3D Style

Luxurious gold metal objects with premium rendering quality.

## Quick Start

```bash
# Using --style flag
uv run python main.py output.png "a gear icon" --style assets/styles/gold_metallic_3d.md

# Multiple subjects at once
uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/gold_metallic_3d.md

# With reference image for extra consistency
uv run python main.py output.png "rocket icon" --style assets/styles/gold_metallic_3d.md --ref assets/styles/gold_metallic_3d/examples/1.png
```

## Prompt Template

```
SOLID DARK BACKGROUND ONLY. NO gradients, NO environmental elements. Premium 3D render of metallic objects ONLY. NO TEXT. {subject}. All objects are polished brushed gold metal (#D4AF37). Warm amber (#FFB84D) highlights on reflective surfaces. Subtle dark bronze (#8B4513) shadows and depth. Minimal metallic reflection beneath objects only. Metal objects centered in frame. Background must be solid dark charcoal (#1a1a1a).
```

## Color Palette

| Element | Hex | Description |
|---------|-----|-------------|
| Metal Body | `#D4AF37` | Rich gold, brushed finish |
| Highlights | `#FFB84D` | Warm amber glow |
| Shadows | `#8B4513` | Dark bronze depth |
| Background | `#1a1a1a` | Dark charcoal |

## Material Properties

- **Finish:** Brushed/satin metal (not mirror)
- **Reflection:** Subtle, not chrome-like
- **Weight:** Heavy, solid, premium feel
- **Lighting:** Warm studio lighting

## What NOT to Include

- Gradients, vignettes, fog
- Text, labels, titles
- Cool colors (stick to gold/amber/bronze)
- Plastic or glass materials
