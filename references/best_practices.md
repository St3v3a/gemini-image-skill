# Gemini Image Generation Best Practices

Distilled from production experience and showcase examples using the blue glass 3D style.

## Table of Contents

1. [Style Consistency Techniques](#style-consistency-techniques)
2. [Prompt Engineering Principles](#prompt-engineering-principles)
3. [Gradient Degradation Warning](#gradient-degradation-warning)
4. [Background Generation Strategies](#background-generation-strategies)
5. [Reference Image Techniques](#reference-image-techniques)
6. [Batch Processing Patterns](#batch-processing-patterns)
7. [Template Design Guidelines](#template-design-guidelines)

## Style Consistency Techniques

### Front-Load Prohibitions

Place explicit negatives at the **beginning** of prompts for maximum impact:

✅ **Good:**
```
SOLID BLACK BACKGROUND ONLY. NO gradients, NO vignettes, NO fog, NO environmental elements...
```

❌ **Bad:**
```
Create an image with a black background... (avoid gradients at the end)
```

**Why it works:** Gemini prioritizes information at the beginning of prompts. Starting with clear constraints sets boundaries before the generative process begins.

### Single Dense Paragraphs Over Bullet Points

The model responds better to flowing prose than structured lists.

✅ **Good:**
```
Premium 3D render of glass objects ONLY. All objects are thick frosted royal blue glass (#1e3a8a). Sharp Electric Cyan (#00D4FF) rim lighting on top edges. Soft internal volumetric glow. Minimal mirrored reflection beneath objects only. Glass objects centered in frame. Background must be pure solid black (#000000).
```

❌ **Bad:**
```
- 3D glass objects
- Blue color (#1e3a8a)
- Cyan rim lighting
- Black background
```

**Why it works:** Natural language flow helps the model understand relationships between elements. Bullet points fragment the context.

### Explicit Color Specifications

Always use hex codes for precise, repeatable colors.

| Vague | Precise | Result |
|-------|---------|--------|
| "Blue background" | "Royal blue (#1e3a8a) background" | Consistent across generations |
| "Green accent" | "Electric cyan (#00D4FF) accent" | Exact color matching |
| "Black" | "Pure solid black (#000000)" | No gray contamination |

**Best practice:** Build a color palette with hex codes and reuse them across all prompts for a cohesive look.

### Literal Descriptions

Describe what you see, not metaphors or abstract concepts.

✅ **Literal:**
```
Four circular nodes connected by straight lines forming a path
```

❌ **Metaphorical:**
```
Milestone markers representing a journey through progress
```

**Why it works:** The model generates visual elements, not concepts. Literal descriptions translate directly to pixels.

## Prompt Engineering Principles

### Negative Prompting

Be explicit about what NOT to include:

**Standard exclusions for clean renders:**
- NO gradients (unless final output)
- NO text or labels
- NO environmental elements (fog, atmosphere, particles)
- NO human characters (unless specifically requested)
- NO patterns or textures (if solid surfaces desired)

**Example negative section:**
```
SOLID BLACK BACKGROUND ONLY. NO gradients, NO vignettes, NO fog, NO environmental elements, NO text or labels, NO circuit patterns.
```

### Material Property Specification

Describe physical characteristics in detail:

**Opacity:**
- "80% semi-transparent" (not "kind of see-through")
- "Completely opaque" (not "solid")
- "50% translucent with internal depth"

**Finish:**
- "Satin/frosted, not glossy"
- "Matte black surface"
- "Polished chrome with mirror reflections"

**Physical feel:**
- "Heavy, physical, not ghostly"
- "Thick glass with substantial weight"
- "Paper-thin delicate material"

**Light interaction:**
- "Internal volumetric glow"
- "Surface rim lighting on top edges only"
- "Subsurface scattering with soft edges"

### Composition Guidance

Provide spatial and layout instructions:

**Positioning:**
- "Centered in frame"
- "Objects clustered in left third"
- "Evenly spaced across horizontal axis"

**Spacing:**
- "Minimal gaps between elements"
- "Generous padding around objects"
- "Tight composition with no empty space"

**Reflections and shadows:**
- "Minimal mirrored reflection beneath objects"
- "No shadows" (if desired)
- "Soft contact shadows only"

**Camera/perspective:**
- "Straight-on orthographic view"
- "Slight 3/4 perspective"
- "Isometric view from above"

## Gradient Degradation Warning

**Critical lesson from showcase testing:** Gradients compound artifacts through iterative generation.

### The Problem Demonstrated

Starting with a clean image, observe degradation across iterations:

1. **Original** - Clean solid black background, perfect quality
2. **Iteration 1** (+gradient) - Gradient added, looks acceptable
3. **Iteration 2** - Colors drifting slightly, minor banding
4. **Iteration 3** - Visible compression artifacts, pronounced banding
5. **Iteration 4** - Muddy colors, severe banding, unusable quality

**Source:** See `showcase/gradient_degradation/` for visual examples

### Why It Happens

- Each generation → compression → quality loss
- Gradients amplify compression artifacts (smooth color transitions show banding)
- Subtle color shifts accumulate with each iteration
- Model tries to replicate compression artifacts as intentional features
- Exponential degradation: artifacts from iteration N become source data for iteration N+1

### Solution: Solid Colors for Iteration

When planning iterative or multi-stage workflows:

1. **Use SOLID colors** for elements you'll refine or regenerate
2. **Generate gradients/atmospherics LAST** (single-pass, no further iteration)
3. **Separate layers** for foreground (iterable) and background (gradient)
4. **Composite externally** using Canva, Photoshop, GIMP, or other tools

**Workflow example:**
```bash
# Step 1: Generate foreground with solid background (iterate safely)
uv run python main.py foreground.png \
  "Icon set on pure solid black (#000000)" \
  --style blue_glass_3d.md

# Step 2: Once satisfied, generate gradient background separately
uv run python main.py background.png \
  "Abstract gradient background from deep blue to purple" \
  --aspect 16:9

# Step 3: Composite in external tool (no quality loss)
# - Import both images into Canva/Photoshop
# - Layer foreground over background
# - Add text, effects, etc.
# - Export final composition
```

### When Gradients Are Safe

Gradients are acceptable for:
- **Single-generation final outputs** (no future iteration planned)
- **Separately generated backgrounds** (composited later)
- **Non-iterated elements** (generated once and left alone)

## Background Generation Strategies

### Solid Backgrounds (Recommended for Iteration)

**Best colors:**
- Pure black: `#000000`
- Pure white: `#FFFFFF`
- Specific brand colors: Use hex codes

**Advantages:**
- No degradation through iterations
- Clean compositing
- Predictable results
- Fast generation

**When to use:**
- Icons and logos
- Iterative refinement workflows
- Elements that need transparency added later
- Assets for compositing

### Separate Background Generation

For complex backgrounds (gradients, textures, atmospherics):

**Process:**
1. Generate foreground on solid background
2. Generate background separately (no foreground elements)
3. Composite in external design tool
4. Add text, overlays, effects as needed

**Benefits:**
- Independent iteration of each layer
- No degradation from multiple passes
- Precise control over composition
- Easy A/B testing of different backgrounds
- Can generate multiple background options for one foreground

**Example:**
```bash
# Foreground: iterable objects on solid black
uv run python main.py icons.png \
  "Five icons: cube, sphere, pyramid, cylinder, cone on solid black" \
  --style blue_glass_3d.md --aspect 16:9

# Background: gradient (generated once)
uv run python main.py bg.png \
  "Abstract tech gradient from deep blue (#0a1628) to purple (#1a0a28)" \
  --aspect 16:9

# Then composite in Canva/Photoshop
```

### Background Type Selection by Use Case

| Use Case | Recommended Background | Rationale |
|----------|----------------------|-----------|
| Icons | Solid black or white | Maximum versatility, clean look |
| Thumbnails | Separate gradient + composite | Vibrant, eye-catching |
| Social media | Vibrant solid colors | Platform-specific branding |
| Presentations | Subtle gradients (external composite) | Professional, not distracting |
| Print | High-quality solid backgrounds | Predictable color reproduction |
| Transparent PNGs | Solid black (remove in post) | Easy background removal |

## Reference Image Techniques

### Reference Role: WHAT vs HOW

**Key principle:** Reference images define content/structure, prompts define style/materials.

**Reference images define:**
- Specific shapes and objects
- Icon designs and symbols
- Compositional layout
- Spatial arrangement
- Number and type of elements

**Text prompt defines:**
- Visual style and aesthetics
- Material properties (glass, metal, wood)
- Lighting and rendering
- Colors and finish
- Background treatment

### Example: Combined Approach

```bash
# Reference shows: 5 specific tech icons (shapes/symbols)
# Prompt specifies: blue glass material, lighting, colors, background

uv run python main.py output.png \
  "Replicate the exact icons from reference image. Each icon rendered as thick frosted royal blue glass (#1e3a8a). Sharp Electric Cyan (#00D4FF) rim lighting on top edges. Soft internal volumetric glow. Minimal mirrored reflection beneath each icon. Icons evenly spaced and centered in frame. Background must be pure solid black (#000000). NO text or labels." \
  --ref original_icons.png --aspect 16:9
```

**Result:** Same icons as reference, but in blue glass style instead of original appearance.

### Using Multiple Reference Images (Up to 14)

**When to use multiple references:**

**Style consistency (2-3 references):**
- Show multiple examples of desired aesthetic
- Demonstrate style across different subjects
- Reinforce visual consistency

**Composition variety (3-5 references):**
- Different angles or layouts to synthesize
- Variations of similar concepts
- Range of acceptable outputs

**Element library (5-14 references):**
- Collection of objects to combine
- Multiple components to assemble
- Comprehensive style guide

**Priority order matters:**
- **First reference** has strongest influence
- **References 2-3** provide supporting context
- **References 4+** offer additional guidance
- Don't include conflicting styles

### Maximum Consistency: Templates + References

For the highest possible consistency across generations:

```bash
uv run python main.py output.png "rocket icon" \
  --style assets/styles/blue_glass_3d.md \
  --ref assets/styles/examples/1.png \
  --ref assets/styles/examples/2.png
```

**Combines:**
- Style template (blue glass prompt structure)
- Multiple reference images (visual examples)
- Specific subject (rocket)

**Trade-off:** Less creative freedom, more predictable output

**Best for:**
- New objects in established style
- Brand consistency requirements
- Large batch generation across project
- Client work with specific style requirements

## Batch Processing Patterns

### Consistent Style Across Multiple Subjects

Generate multiple images with identical style in one command:

```bash
# Generates icon_1.png, icon_2.png, icon_3.png, icon_4.png
uv run python main.py icon.png \
  "cube" "sphere" "pyramid" "cylinder" \
  --style assets/styles/blue_glass_3d.md
```

**Best for:**
- Icon sets
- Presentation slide series
- Social media content series
- Product variation renders
- Tutorial step illustrations

### Naming Convention

The script automatically numbers outputs:
- Input: `output.png` + 3 prompts
- Output: `output_1.png`, `output_2.png`, `output_3.png`

**Pro tip:** Track the order of your subjects to know which file is which.

### Quality Control Workflow

After batch generation:

1. **Review all outputs** for style consistency
2. **Identify outliers** (images that don't match the set)
3. **Regenerate individually** for any that need refinement
4. **Use successful outputs as references** for regenerating outliers
5. **Iterate selectively** rather than regenerating entire batch

### Iteration Strategy for Batches

**First pass:** Broad batch with style template
```bash
uv run python main.py icons.png "cube" "sphere" "pyramid" "cylinder" \
  --style blue_glass_3d.md
```

**Second pass:** Refine outliers individually
```bash
# If icon_3.png (pyramid) doesn't match style
uv run python main.py icon_3_v2.png "pyramid" \
  --style blue_glass_3d.md \
  --ref icon_1.png \  # Use successful examples as references
  --ref icon_2.png
```

**Third pass:** Fine-tune remaining issues
```bash
# Very specific prompt for final tweaks
uv run python main.py icon_3_final.png \
  "Geometric pyramid identical in style to references. Ensure same blue tone, same rim lighting intensity, same reflection size" \
  --style blue_glass_3d.md \
  --ref icon_1.png \
  --ref icon_2.png \
  --ref icon_4.png
```

## Template Design Guidelines

### Structure of a Style Template

```markdown
# Style Name

Brief description and usage instructions.

## Prompt Template

Used automatically when you pass --style path/to/style.md:

```
[PROMPT TEXT WITH {subject} PLACEHOLDER]
```

## Color Palette (optional but recommended)

| Element | Hex | Description |
|---------|-----|-------------|
| Primary | #1e3a8a | Royal blue |
| Accent  | #00D4FF | Electric cyan |
| Background | #000000 | Pure black |
```

### The {subject} Placeholder

The script automatically replaces `{subject}` with each prompt:

```python
# Template
template = "A {subject} made of frosted blue glass on black background"

# Subjects
subjects = ["cube", "sphere", "pyramid"]

# Generates these prompts:
# "A cube made of frosted blue glass on black background"
# "A sphere made of frosted blue glass on black background"
# "A pyramid made of frosted blue glass on black background"
```

**Important:**
- Use exactly `{subject}` (lowercase, singular)
- Place it where the variable content belongs
- If no `{subject}` found, subject is prepended to template

### Template Testing Process

1. **Start with successful manual prompt**
   - Generate a good image manually first
   - Verify the prompt produces desired results

2. **Identify subject-specific words**
   - Find the parts that change per image
   - Usually the object/subject being rendered

3. **Replace with `{subject}` placeholder**
   - Swap variable parts with placeholder
   - Keep all style/material details intact

4. **Test with 3-5 different subjects**
   - Try diverse subjects: concrete (cube) and abstract (innovation)
   - Verify consistency across all outputs

5. **Refine based on results**
   - Adjust wording if some subjects fail
   - Add more prohibitions if unwanted elements appear
   - Fine-tune color descriptions for precision

### Template Reusability Criteria

Good templates are:

**Subject-agnostic:**
- Work with concrete subjects (cube, car, tree)
- Work with abstract concepts (innovation, speed, growth)
- Don't assume specific object properties

**Style-specific:**
- Explicit about materials (frosted glass, polished metal)
- Clear about lighting (rim lit, volumetric glow)
- Precise about composition (centered, reflected beneath)

**Explicit about exclusions:**
- List what NOT to include
- Front-load prohibitions
- Cover common unwanted elements

**Compact:**
- Single paragraph preferred
- 100-200 words typical
- Dense prose, not bullet points

### Example: Blue Glass 3D Template

```
SOLID BLACK BACKGROUND ONLY. NO gradients, NO vignettes, NO fog, NO environmental elements. Premium 3D render of glass objects ONLY. NO TEXT. {subject}. All objects are thick frosted royal blue glass (#1e3a8a). Sharp Electric Cyan (#00D4FF) rim lighting on top edges. Soft internal volumetric glow. Minimal mirrored reflection beneath objects only. Glass objects centered in frame. Background must be pure solid black (#000000).
```

**Why this works:**
- Front-loaded prohibitions (SOLID BLACK BACKGROUND ONLY)
- Explicit colors with hex codes (#1e3a8a, #00D4FF, #000000)
- Material properties (80% opacity implied by "frosted", "thick")
- Composition guidance (centered, minimal reflection)
- Subject placeholder in logical position
- Works for any object: cube, rocket, brain, innovation, etc.

### Template Evolution

Start simple, add detail as needed:

**Version 1 (basic):**
```
{subject} made of blue glass on black background
```

**Version 2 (more specific):**
```
{subject} made of frosted royal blue glass (#1e3a8a) with cyan rim lighting on solid black (#000000) background
```

**Version 3 (production-ready):**
```
SOLID BLACK BACKGROUND ONLY. NO gradients. Premium 3D render of {subject}. Thick frosted royal blue glass (#1e3a8a). Sharp Electric Cyan (#00D4FF) rim lighting on top edges. Soft internal volumetric glow. Minimal mirrored reflection beneath. Centered in frame. Background pure solid black (#000000).
```

**Test each version with edge cases:**
- Very simple objects (cube, sphere)
- Complex objects (circuit board, brain)
- Abstract concepts (teamwork, innovation)
- Multiple objects (set of five icons)

## Summary: Quick Reference

| Technique | Key Point | Example |
|-----------|-----------|---------|
| **Front-load prohibitions** | Start with "NO X, NO Y, NO Z" | "SOLID BLACK ONLY. NO gradients..." |
| **Use hex codes** | Specify exact colors | "#1e3a8a not "blue" |
| **Literal descriptions** | Describe visuals, not metaphors | "Four circles connected by lines" not "journey milestones" |
| **Avoid gradients in iteration** | Solid colors for iterable elements | Generate gradients last, composite separately |
| **Separate backgrounds** | Foreground + background → composite | Two generations + external compositing |
| **References define WHAT** | Prompts define HOW | Ref = shapes, Prompt = materials/style |
| **Template testing** | Test with diverse subjects | Concrete AND abstract concepts |
| **Batch with style** | Multiple subjects, one template | "cube" "sphere" "pyramid" --style template.md |

## Additional Examples from Showcase

All examples in `assets/styles/examples/` were generated using these techniques:

- **Consistent blue glass 3D style** across all subjects
- **Solid black backgrounds** for clean compositing
- **Front-loaded prohibitions** in every prompt
- **Explicit hex codes** for royal blue and cyan
- **Subject variety:** icons, abstract concepts, technical symbols
- **No gradients** to preserve iteration capability

These demonstrate that following these best practices produces reliable, professional results across diverse subjects.
