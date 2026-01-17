import asyncio
from pathlib import Path
from base64 import b64decode
from datetime import datetime

from imgify import ImgifyAzure


async def main():
    async with ImgifyAzure() as client:
        print("Generating image with Azure OpenAI...")
        image = await client.generate_image(
            "A happy person in the rian"
        )
        print(f"Generated image: {image.b64_json[:100]}...\n")

        images_dir = Path("images")
        images_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = images_dir / f"azure_openai_{timestamp}.png"
        
        filepath.write_bytes(b64decode(image.b64_json))
        print(f"Saved image to: {filepath}")


if __name__ == "__main__":
    asyncio.run(main())