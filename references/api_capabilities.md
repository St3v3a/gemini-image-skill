# Gemini Image API Capabilities

Reference for `gemini-3-pro-image-preview` model capabilities and limitations.

## Model Information

- **Model ID:** `gemini-3-pro-image-preview`
- **Modalities:** IMAGE + TEXT (accepts text and images, generates images and optional text)
- **Image Size:** 1K (1024px on longest side)
- **Response Format:** Inline data (base64 encoded binary in response)

## Aspect Ratios

| Ratio | Orientation | Common Use Cases |
|-------|-------------|------------------|
| 1:1   | Square      | Social media posts, profile pictures, icons, avatars, Instagram grid |
| 3:4   | Portrait    | Traditional photo prints, portrait photography, posters |
| 4:3   | Landscape   | Traditional photo prints, presentations, computer monitors (legacy) |
| 4:5   | Portrait    | Instagram posts (taller feed presence) |
| 5:4   | Landscape   | Instagram posts (landscape feed) |
| 9:16  | Vertical    | Mobile video, Instagram/TikTok stories, vertical displays |
| 16:9  | Horizontal  | YouTube thumbnails, presentations, modern monitors, TV displays |
| 21:9  | Ultra-wide  | Cinematic content, ultra-wide monitors, YouTube banners |

### Aspect Ratio Selection Guide

**Content Type:**
- Video thumbnails → 16:9 (YouTube, Vimeo)
- Social media posts → 1:1 (all platforms), 4:5 (Instagram portrait)
- Stories/Reels → 9:16 (Instagram, TikTok, Snapchat)
- Profile pictures → 1:1 (always square)
- Presentations → 16:9 (modern) or 4:3 (legacy)
- Icons/logos → 1:1 (square for versatility)
- Website headers → 21:9 (ultra-wide)
- Print photography → 3:4 or 4:3 (traditional)

## Reference Images

### Limits
- **Maximum:** 14 images per request
- **Edit mode:** 13 reference images + 1 main image = 14 total
- **Generation mode:** 14 reference images for style/composition guidance

### Purpose
Reference images guide the model's understanding of:
- **Style:** Visual aesthetics, color palette, rendering technique
- **Composition:** Layout, arrangement, spatial organization
- **Content:** Specific objects, shapes, or elements to include or emulate

### File Formats
- **Supported:** PNG, JPEG, WebP
- **Recommended:** PNG for graphics/icons, JPEG for photos
- **Size considerations:** Larger images consume more tokens but provide more detail

### Usage Patterns

**Single reference (1 image):**
- Style transfer from one example
- Matching a specific aesthetic
- Replicating a particular composition

**Multiple references (2-5 images):**
- Consistent style across varied subjects
- Combining elements from different sources
- Providing multiple perspectives of desired outcome

**Many references (6-14 images):**
- Brand consistency across large asset sets
- Very specific style requirements
- Maximum guidance for complex compositions

**Best practice:** Start with 1-2 references, add more only if needed for consistency.

## Generation Modes

### Text-to-Image (Standard Generation)

**Input:**
- Text prompt (required)
- Reference images (optional, up to 14)
- Aspect ratio configuration

**Output:**
- Generated image in specified aspect ratio
- Optional text response from model

**Streaming:**
- Available when no reference images
- Faster user experience with progress updates
- Not available with reference images (uses standard generation)

**Configuration:**
```python
config = types.GenerateContentConfig(
    response_modalities=["IMAGE", "TEXT"],
    image_config=types.ImageConfig(
        aspect_ratio="16:9",  # or any supported ratio
        image_size="1K",       # 1024px on longest side
    ),
)
```

### Image-to-Image (Editing)

**Input:**
- Base image to edit (required)
- Text instructions describing the edit (required)
- Reference images (optional, up to 13 additional)

**Output:**
- Edited image
- Optional text response from model

**Use cases:**
- Background changes or removal
- Color adjustments and recoloring
- Adding or removing elements
- Style transfer to existing image
- Composition modifications

**Example instructions:**
- "Change the background to solid blue (#0066CC)"
- "Remove all text from the image"
- "Convert to black and white"
- "Add a reflection beneath the object"
- "Make the lighting more dramatic"

**Limitations:**
- Quality depends on complexity of edit
- Major structural changes may be unpredictable
- Subtle edits generally more successful than complete transformations

## API Authentication

### API Key Setup

**Obtaining a key:**
1. Visit https://aistudio.google.com/apikey
2. Sign in with Google account
3. Create new API key
4. Copy the key immediately (not shown again)

**Configuration methods:**

**Environment variable (recommended):**
```bash
# Linux/macOS
export GOOGLE_AI_API_KEY="your_key_here"

# Windows PowerShell
$env:GOOGLE_AI_API_KEY="your_key_here"
```

**.env file (project-specific):**
```
GOOGLE_AI_API_KEY=your_key_here
```

**Security considerations:**
- Never commit API keys to version control
- Add `.env` to `.gitignore`
- Use environment variables for production
- Rotate keys periodically
- Monitor usage in AI Studio dashboard

## Rate Limits and Quotas

### Free Tier
- Limited requests per minute (exact limits vary)
- Daily quota restrictions
- May experience throttling during peak times
- Suitable for development and testing

### Paid Tier (Recommended for Production)
- Higher rate limits
- Increased daily quotas
- Priority processing
- More reliable availability

**Recommendation:** Use free tier for development, upgrade to paid tier for production use or when generating multiple images.

### Monitoring Usage
- Dashboard: https://aistudio.google.com/
- View request counts
- Track quota consumption
- Monitor spending (paid tier)
- Set up usage alerts

## Response Structure

### Successful Response

```python
response.candidates[0].content.parts[]
```

**Image data:**
- Located in: `part.inline_data.data`
- Format: Binary image data (PNG/JPEG)
- Usage: Write directly to file

**Optional text:**
- Located in: `part.text`
- Contains: Model's commentary or description
- Usage: Informational, can be ignored

### Response Iteration

```python
for part in response.candidates[0].content.parts:
    if part.inline_data and part.inline_data.data:
        # Image data found
        with open(output_path, "wb") as f:
            f.write(part.inline_data.data)
    elif hasattr(part, "text") and part.text:
        # Text response found
        print(part.text)
```

## Error Codes and Common Issues

### 400 Bad Request
**Causes:**
- Invalid parameters (malformed prompt, unsupported aspect ratio)
- Reference image format issues
- Request payload too large
- Malformed JSON in request

**Solutions:**
- Verify aspect ratio is in supported list
- Check image files are valid PNG/JPEG/WebP
- Reduce number of reference images
- Validate request structure

### 401 Unauthorized
**Causes:**
- Missing API key
- Invalid API key
- Expired API key
- API key not set in environment

**Solutions:**
- Verify `GOOGLE_AI_API_KEY` is set
- Check key value matches AI Studio
- Generate new API key if expired
- Ensure environment variable is loaded

### 429 Too Many Requests
**Causes:**
- Rate limit exceeded (requests per minute)
- Quota limit exceeded (daily/monthly)
- Too many concurrent requests

**Solutions:**
- Wait before retrying (exponential backoff)
- Upgrade to paid tier for higher limits
- Batch requests to stay under rate limits
- Monitor usage in AI Studio dashboard
- Implement retry logic with delays

### 500 Internal Server Error
**Causes:**
- Temporary API issues
- Service degradation
- Unexpected backend error

**Solutions:**
- Retry after brief delay
- Check Google AI status page
- Simplify request (fewer references, shorter prompt)
- Try again later if persistent

### Content Safety Filtering
**Causes:**
- Prompt triggers safety filters
- Generated content violates policies
- Request blocked for policy reasons

**Solutions:**
- Rephrase prompt to avoid triggering filters
- Remove potentially sensitive subjects
- Review content policy guidelines
- Ensure prompt aligns with acceptable use

## API Limitations

### Technical Constraints
- Maximum 14 reference images per request
- Image size fixed at 1K (1024px longest side)
- No control over compression/quality settings
- No batch generation in single API call (requires multiple requests)

### Content Constraints
- Subject to content safety policies
- Cannot generate certain categories (check Google's policies)
- May refuse prompts with sensitive subjects
- Quality varies based on prompt complexity

### Performance Considerations
- Streaming unavailable with reference images
- Generation time increases with more references
- Complex prompts may take longer
- Network latency affects response time

## Best Practices

### For Optimal Results
1. Use specific, detailed prompts
2. Include explicit colors with hex codes
3. Start with 1-2 reference images, add more if needed
4. Choose appropriate aspect ratio for use case
5. Test prompts iteratively and refine

### For Reliability
1. Implement retry logic with exponential backoff
2. Handle all error codes gracefully
3. Validate inputs before making requests
4. Monitor quota usage regularly
5. Use paid tier for production workloads

### For Cost Efficiency
1. Minimize unnecessary reference images
2. Cache successful prompts for reuse
3. Batch similar requests together
4. Use free tier for development/testing
5. Monitor spending in AI Studio

## Additional Resources

- **Official Documentation:** https://ai.google.dev/gemini-api/docs
- **API Key Management:** https://aistudio.google.com/apikey
- **Content Policies:** https://ai.google.dev/gemini-api/terms
- **Status Page:** Check Google Cloud Status Dashboard
- **Community:** Google AI Developer Forums
