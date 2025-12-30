# Gradient Holographic Style

Modern holographic gradient aesthetic with iridescent colors.

## Quick Start

```bash
# Using --style flag
uv run python main.py output.png "a gear icon" --style assets/styles/gradient_holographic.md

# Multiple subjects at once
uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/gradient_holographic.md
```

## Prompt Template

```
SOLID WHITE BACKGROUND ONLY. NO realistic materials, NO hard shadows. 3D objects with holographic gradient surfaces ONLY. NO TEXT. {subject}. All objects have smooth iridescent gradients flowing from purple (#8B5CF6) to pink (#EC4899) to cyan (#06B6D4). Glossy reflective finish. Soft ambient lighting. Floating appearance with subtle drop shadow. Objects centered in frame. Background must be pure solid white (#FFFFFF).
```

## Color Palette

| Element | Hex | Description |
|---------|-----|-------------|
| Gradient Start | `#8B5CF6` | Vibrant purple |
| Gradient Mid | `#EC4899` | Hot pink |
| Gradient End | `#06B6D4` | Bright cyan |
| Shadow | `#E5E7EB` | Soft gray |
| Background | `#FFFFFF` | Pure white |

## Material Properties

- **Finish:** Glossy, reflective
- **Gradient:** Smooth, flowing
- **Effect:** Iridescent, holographic
- **Lighting:** Soft, ambient

## What NOT to Include

- Flat colors, solid materials
- Hard shadows, harsh lighting
- Text, labels
- Realistic textures
