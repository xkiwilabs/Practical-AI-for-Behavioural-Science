#!/usr/bin/env python3
"""Generate images using DALL-E 3 for course slide placeholders.

Reads the OpenAI API key from .secrets/api_keys.json (gitignored).
Never exposes the key in output, logs, or error messages.

Usage:
    python dev/generate-image.py --prompt "A warm illustration of..." --output weeks/week-01-lecture/figures/my-image.png
    python dev/generate-image.py --prompt "..." --output path/to/image.png --size 1792x1024
    python dev/generate-image.py --prompt "..." --output path/to/image.png --quality hd
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SECRETS_FILE = REPO_ROOT / ".secrets" / "api_keys.json"
API_URL = "https://api.openai.com/v1/images/generations"


def load_api_key():
    """Load OpenAI API key from .secrets/api_keys.json."""
    if not SECRETS_FILE.exists():
        print(f"Error: {SECRETS_FILE.relative_to(REPO_ROOT)} not found.")
        print("Create it from the template in setup/getting-started.md")
        sys.exit(1)

    with open(SECRETS_FILE) as f:
        keys = json.load(f)

    key = keys.get("openai", {}).get("api_key", "")
    if not key or key.startswith("PASTE_YOUR"):
        print("Error: No valid OpenAI API key found in .secrets/api_keys.json")
        sys.exit(1)

    return key


def generate_image(prompt, output_path, size="1024x1024", quality="standard"):
    """Call DALL-E 3 API and save the resulting image."""
    api_key = load_api_key()

    payload = json.dumps({
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": size,
        "quality": quality,
        "response_format": "url",
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )

    print(f"Generating image with DALL-E 3 ({size}, {quality})...")
    print(f"Prompt: {prompt[:120]}{'...' if len(prompt) > 120 else ''}")

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        # Strip any key references from error output
        body = body.replace(api_key, "[REDACTED]")
        print(f"API error ({e.code}): {body}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}")
        sys.exit(1)

    image_url = result["data"][0]["url"]
    revised_prompt = result["data"][0].get("revised_prompt", "")

    if revised_prompt:
        print(f"Revised prompt: {revised_prompt[:200]}{'...' if len(revised_prompt) > 200 else ''}")

    # Download the image
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading to {output}...")
    urllib.request.urlretrieve(image_url, output)

    size_kb = output.stat().st_size / 1024
    print(f"Saved: {output} ({size_kb:.0f} KB)")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using DALL-E 3 for course slides"
    )
    parser.add_argument(
        "--prompt", required=True, help="Image generation prompt"
    )
    parser.add_argument(
        "--output", required=True, help="Output file path (PNG)"
    )
    parser.add_argument(
        "--size",
        default="1024x1024",
        choices=["1024x1024", "1792x1024", "1024x1792"],
        help="Image size (default: 1024x1024)",
    )
    parser.add_argument(
        "--quality",
        default="standard",
        choices=["standard", "hd"],
        help="Image quality (default: standard)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the prompt without calling the API",
    )
    args = parser.parse_args()

    if args.dry_run:
        print(f"[DRY RUN] Would generate:")
        print(f"  Prompt: {args.prompt}")
        print(f"  Output: {args.output}")
        print(f"  Size: {args.size}")
        print(f"  Quality: {args.quality}")
        return

    generate_image(args.prompt, args.output, args.size, args.quality)


if __name__ == "__main__":
    main()
