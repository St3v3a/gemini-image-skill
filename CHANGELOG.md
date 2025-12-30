# Changelog

All notable changes to the Gemini Image Generation Claude Skill.

## [1.0.0] - 2025-12-30

### Initial Release

**Features:**
- Text-to-image generation using Google Gemini API (`gemini-3-pro-image-preview`)
- Image editing with text instructions
- Style template system with `{subject}` placeholders
- Reference image support (up to 14 images)
- Batch processing for multiple subjects
- 8 aspect ratio options (1:1, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)
- Auto-install dependencies on first run
- Bundled blue glass 3D style template
- 5 example reference images

**Documentation:**
- Complete README.md with usage examples
- INSTALL.md with step-by-step setup
- SKILL.md for Claude integration
- API capabilities reference (334 lines)
- Best practices guide (575 lines)
  - Prompt engineering techniques
  - Gradient degradation warning
  - WHAT vs HOW principle for references
  - Template design guidelines

**Bundled Assets:**
- Blue glass 3D style template
- 5 production-quality reference images
- .env.example template
- .gitignore for security

**Technical:**
- Python 3.10+ required
- uv package manager integration
- Auto-install: google-genai, python-dotenv, pillow
- Cross-platform support (Linux, macOS, Windows)
- Total size: 1.8MB (clean package)

### Tested Features

✅ Basic image generation
✅ Style template application
✅ Batch processing (3+ subjects)
✅ Reference image usage
✅ Image editing
✅ Multiple aspect ratios
✅ Auto-install dependencies
✅ Error handling and recovery

### Known Limitations

- Gemini API quota limits (free tier: limited requests)
- Maximum 14 reference images per request
- Fixed image size: 1K (1024px longest side)
- Requires internet connection for API calls

### Security

- API keys never committed (protected by .gitignore)
- .env.example provided for reference
- Environment variable support
- Security best practices documented

## Future Enhancements

Potential additions for future versions:
- Additional style templates
- Image optimization tools
- Format conversion utilities
- Advanced compositing workflows
- More reference image examples
- Video thumbnail generation templates
