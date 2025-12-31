# Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Install uv (2 minutes)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows PowerShell:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (any OS):**
```bash
pip install uv
```

## Step 2: Get API Key (2 minutes)

1. Visit: https://aistudio.google.com/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key

## Step 3: Configure (1 minute)

Create `.env` file in the `scripts/` directory:

```bash
# Copy the example
cp .env.example scripts/.env

# Edit scripts/.env and add your key
GOOGLE_AI_API_KEY=your_actual_api_key_here
```

**OR** set environment variable:

**Linux/macOS:**
```bash
export GOOGLE_AI_API_KEY="your_key_here"
```

**Windows PowerShell:**
```powershell
$env:GOOGLE_AI_API_KEY="your_key_here"
```

## Step 4: Generate Your First Image!

**From the package directory:**

**Linux/macOS:**
```bash
cd gemini-image-gen-public
./generate.sh images/my_first.png "A vibrant sunset over mountains"
```

**Windows PowerShell:**
```powershell
cd gemini-image-gen-public
generate.bat images/my_first.png "A vibrant sunset over mountains"
```

Your image will be in `images/my_first.png`!

## Try Different Styles

**Neon Icon:**
```bash
./generate.sh images/icon.png "rocket" \
  --style assets/styles/neon_wireframe.md
```

**Purple Glass 3D:**
```bash
./generate.sh images/glass.png "database" \
  --style assets/styles/purple_glass_3d.md
```

**Gold Metallic:**
```bash
./generate.sh images/gold.png "cloud storage" \
  --style assets/styles/gold_metallic_3d.md
```

## Available Styles

Located in `assets/styles/`:

**Glass Styles:**
- `purple_glass_3d.md` - Royal purple frosted glass
- `emerald_glass_3d.md` - Deep emerald glass
- `amber_glass_3d.md` - Rich amber glass

**Other Styles:**
- `neon_wireframe.md` - Hot pink/cyan neon wireframe
- `gold_metallic_3d.md` - Brushed gold metal
- `minimalist_flat.md` - Soft pastel flat design
- `gradient_holographic.md` - Iridescent gradients

## Troubleshooting

**"GOOGLE_AI_API_KEY not found"**
- Make sure `.env` is in the `scripts/` directory
- Or set the environment variable

**"uv: command not found"**
- Install uv (see Step 1)
- Restart your terminal

**Files saving to wrong place?**
- Use the wrapper scripts (`generate.sh` or `generate.bat`)
- Make sure you're in the gemini-image-gen-public directory

## Next Steps

- Read `README.md` for detailed documentation
- Check `SKILL.md` for advanced features
- Explore `assets/styles/` for example images

## Need Help?

- Check README.md for full documentation
- Review example images in `assets/styles/*/examples/`
- API documentation: https://ai.google.dev/

Enjoy creating amazing images! 🎨
