# Neon Wireframe Style

Vibrant neon wireframe objects with glowing edges on dark backgrounds.

## Quick Start

```bash
# Using --style flag
uv run python main.py output.png "a gear icon" --style assets/styles/neon_wireframe.md

# Multiple subjects at once
uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/neon_wireframe.md
```

## Prompt Template

```
SOLID BLACK BACKGROUND ONLY. NO solid fills, NO gradients, NO fog. Wireframe line art ONLY. NO TEXT. {subject}. All objects are glowing neon wireframe with bright pink (#FF1493) and electric cyan (#00FFFF) edges. Thin luminous lines forming geometric shapes. Slight glow effect around lines. Objects centered in frame. Background must be pure solid black (#000000).
```

## Color Palette

| Element | Hex | Description |
|---------|-----|-------------|
| Primary Lines | `#FF1493` | Hot pink neon |
| Secondary Lines | `#00FFFF` | Electric cyan |
| Glow Effect | Pink/Cyan | Soft luminescence |
| Background | `#000000` | Pure black |

## Material Properties

- **Style:** Wireframe/outline only
- **Line Weight:** Thin, consistent
- **Glow:** Soft neon luminescence
- **Complexity:** Clean geometric forms

## What NOT to Include

- Solid fills, surfaces
- Gradients, fog, environments
- Text, labels
- Realistic materials
