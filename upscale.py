#!/usr/bin/env python3
"""Upscale image using high-quality Lanczos resampling"""
from PIL import Image
import sys

if len(sys.argv) < 3:
    print("Usage: python upscale.py input.png output.png [scale_factor]")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]
scale = int(sys.argv[3]) if len(sys.argv) > 3 else 2

# Open image
img = Image.open(input_path)
print(f"Original size: {img.size}")

# Calculate new size
new_size = (img.width * scale, img.height * scale)
print(f"Upscaling to: {new_size}")

# Upscale using LANCZOS (highest quality)
upscaled = img.resize(new_size, Image.Resampling.LANCZOS)

# Save with maximum quality
upscaled.save(output_path, quality=95, optimize=True)
print(f"Saved to: {output_path}")
