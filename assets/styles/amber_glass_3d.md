# Amber Glass 3D Style

Premium frosted amber glass objects with warm golden rim lighting.

## Quick Start

```bash
# Using --style flag
uv run python main.py output.png "a gear icon" --style assets/styles/amber_glass_3d.md

# Multiple subjects at once
uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/amber_glass_3d.md

# With reference image for extra consistency
uv run python main.py output.png "rocket icon" --style assets/styles/amber_glass_3d.md --ref assets/styles/amber_glass_3d/examples/1.png
```

## Prompt Template

```
SOLID BLACK BACKGROUND ONLY. NO gradients, NO vignettes, NO fog, NO environmental elements. Premium 3D render of glass objects ONLY. NO TEXT. {subject}. All objects are thick frosted amber glass (#D97706). Sharp bright golden yellow (#FBBF24) rim lighting on top edges. Soft internal volumetric glow. Minimal mirrored reflection beneath objects only. Glass objects centered in frame. Background must be pure solid black (#000000).
```

## Color Palette

| Element | Hex | Description |
|---------|-----|-------------|
| Glass Body | `#D97706` | Rich amber, frosted |
| Rim Lighting | `#FBBF24` | Bright golden yellow, sharp edges |
| Internal Glow | White/Amber | Soft, volumetric |
| Background | `#000000` | Pure black |

## Material Properties

- **Opacity:** ~80% semi-transparent
- **Finish:** Satin/frosted (not glossy)
- **Feel:** Heavy, physical, not ghostly
- **Refraction:** Internal depth and light scattering

## What NOT to Include

- Gradients, vignettes, fog, environments
- Text, titles, labels
- Cool colors (only warm amber/gold tones)
- Human characters
- Flat/sticker appearance
