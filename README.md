# Imgify

A clean, async Python wrapper for API-based image generation.

**Supported Models:**
- DALL-E 2
- DALL-E 3
- GPT-Image 1

## Features

- Simple, intuitive API for image generation
- Async/await support
- Type-safe with full type hints
- Environment variable support with python-dotenv
- Support for OpenAI and Azure OpenAI

## Installation
```bash
pip install imgify
```

## Quick Start

### OpenAI

#### Option 1: Using Environment Variables

Set up your `.env` file:
```env
OPENAI_API_KEY=your-openai-api-key
```

Then use the client:
```python
import asyncio
from imgify import ImgifyOpenAI

async def main():
    async with ImgifyOpenAI() as client:
        image = await client.generate_image(
            "A serene mountain landscape"
        )
        print(f"Image: {image.b64_json[:50]}...")

asyncio.run(main())
```

#### Option 2: Passing API Key Directly
```python
import asyncio
from imgify import ImgifyOpenAI

async def main():
    async with ImgifyOpenAI(api_key="your-openai-api-key") as client:
        image = await client.generate_image(
            "A serene mountain landscape"
        )
        print(f"Image: {image.b64_json[:50]}...")

asyncio.run(main())
```

### Azure OpenAI

#### Option 1: Using Environment Variables

Set up your `.env` file:
```env
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
```

Then use the client:
```python
import asyncio
from imgify import ImgifyAzure

async def main():
    async with ImgifyAzure() as client:
        image = await client.generate_image_b64(
            "A futuristic city"
        )
        print(f"Image: {image.b64_json[:50]}...")

asyncio.run(main())
```

#### Option 2: Passing Credentials Directly
```python
import asyncio
from imgify import ImgifyAzure

async def main():
    async with ImgifyAzure(
        api_key="your-azure-openai-api-key",
        azure_endpoint="https://your-resource.openai.azure.com/"
    ) as client:
        image = await client.generate_image(
            "A futuristic city"
        )
        print(f"Image: {image.b64_json[:50]}...")

asyncio.run(main())
```

## Advanced Usage

### Customize Model, Size, and Quality
```python
from imgify import ImgifyOpenAI, ImageModelApiName, ImageSize, ImageQuality

async with ImgifyOpenAI() as client:
    image = await client.generate_image(
        "A peaceful forest",
        model=ImageModelApiName.DALL_E_3,
        size=ImageSize.LANDSCAPE_1792,
        quality=ImageQuality.HD
    )
    print(image.b64_json)
```

### Save Image to Disk
```python
from pathlib import Path
from base64 import b64decode

async with ImgifyOpenAI() as client:
    image = await client.generate_image("A sunset over the ocean")
    
    # Decode and save
    Path("output.png").write_bytes(b64decode(image.b64_json))
```

## Available Options

### Models

- `ImageModelApiName.GPT_IMAGE_1` (default)
- `ImageModelApiName.DALL_E_2`
- `ImageModelApiName.DALL_E_3`

### Sizes

- `ImageSize.SQUARE_256` (256x256)
- `ImageSize.SQUARE_512` (512x512)
- `ImageSize.SQUARE_1024` (1024x1024, default)
- `ImageSize.LANDSCAPE_1792` (1792x1024)
- `ImageSize.PORTRAIT_1792` (1024x1792)

### Quality

- `ImageQuality.STANDARD` (default)
- `ImageQuality.HD`