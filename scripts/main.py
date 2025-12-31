#!/usr/bin/env python3
# Gemini Image Generation Skill - Professional AI-powered image creation
# Part of gemini-image-gen skill suite - see SKILL.md for complete documentation
"""
Gemini AI Image Generation Engine

Professional image generation and editing using Google's Gemini 3 Pro Image model.
Create stunning visuals with 8 built-in style templates, reference image support,
and intelligent batch processing capabilities.

Initial Setup:
    1. Obtain API key: https://aistudio.google.com/apikey
    2. Configure .env file: GOOGLE_AI_API_KEY=your_api_key
    3. Auto-dependency installation on first execution (or manual: uv sync)

Usage:
    # Generate from prompt
    uv run python main.py output.png "A minimal 3D cube on solid black background"

    # Use a style template (reads prompt from .md file)
    uv run python main.py output.png "gear icon" --style assets/styles/purple_glass_3d.md
    uv run python main.py output.png "rocket" --style assets/styles/neon_wireframe.md
    uv run python main.py output.png "cube" --style assets/styles/gold_metallic_3d.md

    # Generate multiple variations with style
    uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/emerald_glass_3d.md

    # Edit existing image
    uv run python main.py output.png "Change the background to white" --edit input.png

    # Use reference images for style consistency
    uv run python main.py output.png "database icon" --ref assets/styles/purple_glass_3d/examples/1.png

    # Specify aspect ratio
    uv run python main.py output.png "YouTube thumbnail design" --aspect 16:9

Aspect ratios: 1:1, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

# Automatic dependency management system
def verify_and_install_skill_dependencies():
    """Verify required packages are installed, auto-install if missing for seamless user experience."""
    missing_packages = []

    # Verify Gemini AI SDK
    try:
        import google.genai
    except ImportError:
        missing_packages.append('google-genai')

    # Verify environment variable loader
    try:
        import dotenv
    except ImportError:
        missing_packages.append('python-dotenv')

    # Verify image processing library
    try:
        import PIL
    except ImportError:
        missing_packages.append('pillow')

    if missing_packages:
        print("🔧 Installing required dependencies... (one-time setup)")
        skill_directory = Path(__file__).parent
        try:
            subprocess.run(
                ['uv', 'sync'],
                cwd=skill_directory,
                check=True,
                capture_output=True,
                text=True
            )
            print("✅ Dependencies installed successfully!")
            print("📝 Please re-run the command to continue.\n")
            sys.exit(0)
        except subprocess.CalledProcessError as installation_error:
            print(f"❌ Dependency installation failed: {installation_error.stderr}")
            print("\n🔧 Manual installation required:")
            print(f"  cd {skill_directory}")
            print("  uv sync")
            sys.exit(1)
        except FileNotFoundError:
            print("❌ Error: 'uv' package manager not found.")
            print("\n📦 Install uv package manager first:")
            print("  curl -LsSf https://astral.sh/uv/install.sh | sh")
            print("  # Alternative: brew install uv")
            sys.exit(1)

verify_and_install_skill_dependencies()

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image


def load_gemini_style_template(template_file_path: Path) -> str:
    """
    Load and parse a professional style template from markdown file.

    Extracts prompt template from markdown file containing '## Prompt Template' section.
    The template must contain {subject} as a dynamic placeholder for content insertion.

    Args:
        template_file_path: Absolute path to the .md template file

    Returns:
        Parsed prompt template string with {subject} placeholder

    Raises:
        FileNotFoundError: If template file doesn't exist
        ValueError: If template file lacks proper '## Prompt Template' section
    """
    if not template_file_path.exists():
        raise FileNotFoundError(f"❌ Style template not found: {template_file_path}")

    template_content = template_file_path.read_text()

    # Extract code block following "Prompt Template" header
    # Pattern matches: ## Prompt Template or ### Template followed by ``` code block ```
    template_pattern = r'(?:##?\s*(?:Prompt\s*)?Template)[^\n]*\n+(?:.*?\n)*?```[^\n]*\n(.*?)```'
    template_match = re.search(template_pattern, template_content, re.IGNORECASE | re.DOTALL)

    if template_match:
        parsed_template = template_match.group(1).strip()
        # Normalize subject placeholder variations to standard {subject} format
        parsed_template = re.sub(
            r'\[YOUR SUBJECT[^\]]*\]|\[SUBJECT\]|\{subject\}',
            '{subject}',
            parsed_template,
            flags=re.IGNORECASE
        )
        return parsed_template

    raise ValueError(f"❌ Invalid template format in {template_file_path}. "
                     "Required: '## Prompt Template' section with code block.")


def apply_subject_to_template(prompt_template: str, subject_content: str) -> str:
    """
    Insert subject content into style template placeholder.

    Args:
        prompt_template: Template string containing {subject} placeholder
        subject_content: Content to insert into template

    Returns:
        Complete rendered prompt ready for Gemini API

    Note:
        If template lacks {subject} placeholder, subject is prepended to template.
    """
    if '{subject}' in prompt_template:
        return prompt_template.format(subject=subject_content)
    else:
        # Fallback: prepend subject when placeholder is missing
        return f"{subject_content}. {prompt_template}"


def edit_existing_image_with_gemini(
    source_image_path: Path,
    edit_instruction: str,
    destination_path: Path,
    style_reference_images: Optional[list[Path]] = None,
) -> None:
    """
    Intelligently edit existing image using Gemini AI with natural language instructions.

    Args:
        source_image_path: Path to original image file to modify
        edit_instruction: Natural language description of desired edits
        destination_path: Output path for edited image
        style_reference_images: Optional reference images for style consistency (max 13, total 14 with source)

    Raises:
        FileNotFoundError: If source image doesn't exist
    """
    gemini_client = genai.Client(
        api_key=os.environ.get("GOOGLE_AI_API_KEY"),
    )

    # Build API request: instruction first, then source image, then style references
    api_contents: list = [edit_instruction]

    # Add primary image to edit
    source_image = Image.open(source_image_path)
    api_contents.append(source_image)

    # Add style reference images if provided (Gemini API limit: 14 total images)
    if style_reference_images:
        for reference_path in style_reference_images[:13]:  # 13 refs + 1 source = 14 max
            if reference_path.exists():
                reference_image = Image.open(reference_path)
                api_contents.append(reference_image)
            else:
                print(f"⚠️  Warning: Reference image not found: {reference_path}")

    api_response = gemini_client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=api_contents,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    if api_response.candidates and api_response.candidates[0].content and api_response.candidates[0].content.parts:
        for response_part in api_response.candidates[0].content.parts:
            if response_part.inline_data and response_part.inline_data.data:
                with open(destination_path, "wb") as output_file:
                    output_file.write(response_part.inline_data.data)
                print(f"✅ Edited image saved to: {destination_path}")
                return
            elif hasattr(response_part, "text") and response_part.text:
                print(response_part.text)


def generate_new_image_with_gemini(
    generation_prompt: str,
    destination_path: Path,
    style_reference_images: Optional[list[Path]] = None,
    output_aspect_ratio: str = "16:9",
) -> None:
    """
    Generate professional images from text prompts using Gemini AI.

    Args:
        generation_prompt: Detailed text description of desired image
        destination_path: Output path for generated image file
        style_reference_images: Optional reference images for style/composition guidance (max 14)
        output_aspect_ratio: Image dimensions (1:1, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)

    Note:
        Uses streaming API when no references provided for better performance.
        Reference images enable style consistency but disable streaming.
    """
    gemini_client = genai.Client(
        api_key=os.environ.get("GOOGLE_AI_API_KEY"),
    )

    # Build API request with optional style references
    if style_reference_images:
        api_contents: list = [generation_prompt]
        for reference_path in style_reference_images[:14]:
            if reference_path.exists():
                reference_image = Image.open(reference_path)
                api_contents.append(reference_image)
            else:
                print(f"⚠️  Warning: Reference image not found: {reference_path}")

        api_response = gemini_client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=api_contents,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        if api_response.candidates and api_response.candidates[0].content and api_response.candidates[0].content.parts:
            for response_part in api_response.candidates[0].content.parts:
                if response_part.inline_data and response_part.inline_data.data:
                    with open(destination_path, "wb") as output_file:
                        output_file.write(response_part.inline_data.data)
                    print(f"✅ Image saved to: {destination_path}")
                    return
                elif hasattr(response_part, "text") and response_part.text:
                    print(response_part.text)
    else:
        # No reference images: use streaming API with aspect ratio configuration
        api_contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=generation_prompt)],
            ),
        ]

        generation_config = types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
            image_config=types.ImageConfig(
                aspect_ratio=output_aspect_ratio,
                image_size="1K",
            ),
        )

        for response_chunk in gemini_client.models.generate_content_stream(
            model="gemini-3-pro-image-preview",
            contents=api_contents,
            config=generation_config,
        ):
            if (
                response_chunk.candidates is None
                or response_chunk.candidates[0].content is None
                or response_chunk.candidates[0].content.parts is None
            ):
                continue

            chunk_part = response_chunk.candidates[0].content.parts[0]
            if chunk_part.inline_data and chunk_part.inline_data.data:
                with open(destination_path, "wb") as output_file:
                    output_file.write(chunk_part.inline_data.data)
                print(f"✅ Image saved to: {destination_path}")
                return
            elif hasattr(chunk_part, "text") and chunk_part.text:
                print(chunk_part.text)


def main():
    # Capture the original working directory before any changes
    # uv sets PWD environment variable to the original directory before --directory changes it
    # This ensures output files go to the correct location regardless of how uv runs the script
    original_cwd = Path(os.environ.get('PWD', os.getcwd()))

    argument_parser = argparse.ArgumentParser(
        description="Gemini AI Image Generation Engine - Create professional images with style templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate single image
  uv run python main.py output.png "A minimal geometric cube"

  # Use different style templates
  uv run python main.py output.png "gear icon" --style assets/styles/purple_glass_3d.md
  uv run python main.py output.png "rocket" --style assets/styles/neon_wireframe.md
  uv run python main.py output.png "cube" --style assets/styles/gold_metallic_3d.md
  uv run python main.py output.png "sphere" --style assets/styles/minimalist_flat.md

  # Generate 3 variations with style
  uv run python main.py output.png "cube" "sphere" "pyramid" --style assets/styles/emerald_glass_3d.md

  # Edit existing image
  uv run python main.py output.png "Change background to gradient" --edit input.png

  # Generate with reference images for consistency
  uv run python main.py output.png "database icon" --ref assets/styles/amber_glass_3d/examples/1.png

  # Combine style template + reference images
  uv run python main.py output.png "rocket" --style assets/styles/purple_glass_3d.md --ref assets/styles/purple_glass_3d/examples/1.png
        """,
    )
    argument_parser.add_argument("output", help="Output destination path (base name for batch processing)")
    argument_parser.add_argument("prompts", nargs="+", help="Subject(s) or prompt(s) for image generation")
    argument_parser.add_argument(
        "--style", "-s",
        help="Style template file path (.md format with {subject} placeholder)",
    )
    argument_parser.add_argument(
        "--edit", "-e",
        help="Edit mode: Path to existing image to modify (disables generation mode)",
    )
    argument_parser.add_argument(
        "--ref", "-r",
        action="append",
        dest="references",
        help="Style reference image path (repeatable flag, maximum 14 references)",
    )
    argument_parser.add_argument(
        "--aspect", "-a",
        default=None,
        choices=["1:1", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
        help="Output aspect ratio (default: 16:9 for infographics, 1:1 for icons)",
    )
    argument_parser.add_argument(
        "--cwd",
        default=None,
        help="Working directory for resolving relative paths (auto-detected from PWD)",
    )
    parsed_args = argument_parser.parse_args()

    # Override original_cwd if explicitly provided
    if parsed_args.cwd:
        original_cwd = Path(parsed_args.cwd)

    # Load environment variables from .env file (current directory and script directory)
    load_dotenv()
    script_env_file = Path(__file__).parent / ".env"
    if script_env_file.exists():
        load_dotenv(script_env_file)

    if not os.environ.get("GOOGLE_AI_API_KEY"):
        print("❌ Error: GOOGLE_AI_API_KEY not found in environment")
        print("📝 Create a .env file containing: GOOGLE_AI_API_KEY=your_api_key")
        print("🔑 Obtain API key from: https://aistudio.google.com/apikey")
        return

    # Resolve output path relative to original working directory (where user invoked the command)
    # This ensures files are saved to the correct location regardless of uv's working directory
    output_file_path = Path(parsed_args.output)
    if not output_file_path.is_absolute():
        output_file_path = original_cwd / output_file_path
    output_file_path = output_file_path.resolve()
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Load and parse style template if specified
    loaded_template = None
    is_infographic_style = False
    if parsed_args.style:
        try:
            style_path = Path(parsed_args.style)
            loaded_template = load_gemini_style_template(style_path)
            # Check if this is an infographic style
            is_infographic_style = 'infographic' in style_path.stem.lower()
            print(f"📋 Loaded style template from: {parsed_args.style}")
        except (FileNotFoundError, ValueError) as template_error:
            print(f"❌ Error: {template_error}")
            return

    # Determine default aspect ratio based on style type
    if parsed_args.aspect is None:
        if is_infographic_style:
            parsed_args.aspect = "16:9"  # Default for infographics
        else:
            parsed_args.aspect = "1:1"  # Default for icons and other styles

    # Process prompts and apply style template if provided
    processed_prompts = parsed_args.prompts
    if loaded_template:
        processed_prompts = [apply_subject_to_template(loaded_template, subject) for subject in processed_prompts]

    # Convert reference image paths to Path objects and resolve relative to original cwd
    reference_image_paths = None
    if parsed_args.references:
        reference_image_paths = []
        for ref in parsed_args.references:
            ref_path = Path(ref)
            if not ref_path.is_absolute():
                ref_path = original_cwd / ref_path
            reference_image_paths.append(ref_path.resolve())

    if parsed_args.edit:
        # Edit mode: modify existing image with AI instructions
        source_image_path = Path(parsed_args.edit)
        if not source_image_path.is_absolute():
            source_image_path = original_cwd / source_image_path
        source_image_path = source_image_path.resolve()

        if not source_image_path.exists():
            print(f"❌ Error: Source image not found: {source_image_path}")
            return
        edit_existing_image_with_gemini(source_image_path, processed_prompts[0], output_file_path, style_reference_images=reference_image_paths)
    elif len(processed_prompts) == 1:
        # Single generation mode
        generate_new_image_with_gemini(processed_prompts[0], output_file_path, style_reference_images=reference_image_paths, output_aspect_ratio=parsed_args.aspect)
    else:
        # Batch generation mode: multiple prompts create numbered outputs
        base_filename = output_file_path.stem
        file_extension = output_file_path.suffix
        output_directory = output_file_path.parent

        for batch_index, prompt_text in enumerate(processed_prompts, 1):
            numbered_output_path = output_directory / f"{base_filename}_{batch_index}{file_extension}"
            print(f"\n🎨 Generating image {batch_index}/{len(processed_prompts)}...")
            generate_new_image_with_gemini(prompt_text, numbered_output_path, style_reference_images=reference_image_paths, output_aspect_ratio=parsed_args.aspect)


if __name__ == "__main__":
    main()
