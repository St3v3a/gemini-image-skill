# Emerald Glass 3D Style

Premium frosted emerald green glass objects with bright green rim lighting.

## Quick Start

```bash
# Using --style flag
uv run python main.py output.png "a gear icon" --style assets/styles/emerald_glass_3d.md

# Multiple subjects at once
uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/emerald_glass_3d.md

# With reference image for extra consistency
uv run python main.py output.png "rocket icon" --style assets/styles/emerald_glass_3d.md --ref assets/styles/emerald_glass_3d/examples/1.png
```

## Prompt Template

```
SOLID BLACK BACKGROUND ONLY. NO gradients, NO vignettes, NO fog, NO environmental elements. Premium 3D render of glass objects ONLY. NO TEXT. {subject}. All objects are thick frosted emerald green glass (#059669). Sharp bright lime green (#10B981) rim lighting on top edges. Soft internal volumetric glow. Minimal mirrored reflection beneath objects only. Glass objects centered in frame. Background must be pure solid black (#000000).
```

## Color Palette

| Element | Hex | Description |
|---------|-----|-------------|
| Glass Body | `#059669` | Deep emerald, frosted |
| Rim Lighting | `#10B981` | Bright lime green, sharp edges |
| Internal Glow | White/Green | Soft, volumetric |
| Background | `#000000` | Pure black |

## Material Properties

- **Opacity:** ~80% semi-transparent
- **Finish:** Satin/frosted (not glossy)
- **Feel:** Heavy, physical, not ghostly
- **Refraction:** Internal depth and light scattering

## What NOT to Include

- Gradients, vignettes, fog, environments
- Text, titles, labels
- Blue or warm colors (only green tones)
- Human characters
- Flat/sticker appearance
