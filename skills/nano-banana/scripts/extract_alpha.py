#!/usr/bin/env python3
"""
extract_alpha.py - Difference matting for transparency extraction

Gemini cannot output true transparency. This script extracts alpha
by comparing the same image rendered on white vs black backgrounds.

Usage: python extract_alpha.py <white.png> <black.png> <output.png>
"""

import sys
import math
from PIL import Image


def extract_alpha(white_path: str, black_path: str, output_path: str) -> None:
    img_white = Image.open(white_path).convert('RGB')
    img_black = Image.open(black_path).convert('RGB')

    if img_white.size != img_black.size:
        raise ValueError('Dimension mismatch: Images must be identical size')

    width, height = img_white.size
    output = Image.new('RGBA', (width, height))

    px_white = img_white.load()
    px_black = img_black.load()
    px_out = output.load()

    # Distance between White (255,255,255) and Black (0,0,0)
    bg_dist = math.sqrt(3 * 255 * 255)

    for y in range(height):
        for x in range(width):
            rW, gW, bW = px_white[x, y]
            rB, gB, bB = px_black[x, y]

            # Distance between the two observed pixels
            pixel_dist = math.sqrt((rW - rB)**2 + (gW - gB)**2 + (bW - bB)**2)

            # Alpha from distance ratio
            # Opaque pixels look identical (dist=0), transparent show background (dist=max)
            alpha = 1 - (pixel_dist / bg_dist)
            alpha = max(0, min(1, alpha))

            # Recover color from black version (un-premultiply)
            if alpha > 0.01:
                rOut = min(255, int(rB / alpha))
                gOut = min(255, int(gB / alpha))
                bOut = min(255, int(bB / alpha))
            else:
                rOut = gOut = bOut = 0

            px_out[x, y] = (rOut, gOut, bOut, int(alpha * 255))

    output.save(output_path, 'PNG')
    print(f'Done: {output_path} ({width}x{height})')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('''Usage: python extract_alpha.py <white.png> <black.png> <output.png>

Extracts true alpha channel via difference matting.

Arguments:
  white    Image on pure white background
  black    Same image on pure black background (use /edit to create)
  output   Output PNG with transparency''')
        sys.exit(1)

    extract_alpha(sys.argv[1], sys.argv[2], sys.argv[3])
