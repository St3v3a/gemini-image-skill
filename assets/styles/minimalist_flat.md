# Minimalist Flat Style

Clean flat design with soft pastel colors and simple shapes.

## Quick Start

```bash
# Using --style flag
uv run python main.py output.png "a gear icon" --style assets/styles/minimalist_flat.md

# Multiple subjects at once
uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/minimalist_flat.md
```

## Prompt Template

```
SOLID WHITE BACKGROUND ONLY. NO shadows, NO gradients, NO 3D effects. Flat 2D design ONLY. NO TEXT. {subject}. All objects are simple flat shapes with soft pastel colors: lavender (#B19CD9), mint green (#98D8C8), peach (#FFB6A3), sky blue (#A0C4FF). Clean vector style with smooth edges. Minimal detail. Objects centered in frame. Background must be pure solid white (#FFFFFF).
```

## Color Palette

| Element | Hex | Description |
|---------|-----|-------------|
| Primary | `#B19CD9` | Soft lavender |
| Secondary | `#98D8C8` | Mint green |
| Accent 1 | `#FFB6A3` | Soft peach |
| Accent 2 | `#A0C4FF` | Sky blue |
| Background | `#FFFFFF` | Pure white |

## Design Properties

- **Style:** Flat 2D, no depth
- **Edges:** Smooth, clean
- **Detail:** Minimal, simplified
- **Colors:** Soft pastels only

## What NOT to Include

- 3D effects, shadows, gradients
- Realistic textures
- Text, labels
- Dark or saturated colors
