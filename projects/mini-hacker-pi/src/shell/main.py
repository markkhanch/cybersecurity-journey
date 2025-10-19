#!/usr/bin/env python3
"""
Mini Hacker Pi shell entry point.

This script initializes the ST7789 display and shows a simple greeting. All
comments in this project are written in English to aid future contributors.
"""

import time

try:
    import ST7789 as st7789
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    # In case libraries are not installed, inform the user and exit gracefully.
    print("Required libraries not found. Did you run install.sh?")
    raise SystemExit(1)


def main() -> None:
    """Main function to initialize the display and draw a greeting."""
    # Configure the display driver. Adjust pins here if you modify wiring.
    display = st7789.ST7789(
        height=240,
        width=240,
        rotation=270,
        spi=st7789.SpiDev(0, 0, 40_000_000),
        gpio=st7789.GPIO(),
        dc=25,
        rst=27,
        cs=8,
        bl=18,
    )
    display.begin()

    # Create a blank image for drawing.
    canvas = Image.new("RGB", (240, 240), color=(0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    # Render greeting text centred on the screen.
    message = "Hello, Mini Hacker Pi!"
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(message, font=font)
    x_pos = (240 - text_width) // 2
    y_pos = (240 - text_height) // 2
    draw.text((x_pos, y_pos), message, font=font, fill=(255, 255, 255))

    # Display the image.
    display.display(canvas)
    time.sleep(5)


if __name__ == "__main__":
    main()