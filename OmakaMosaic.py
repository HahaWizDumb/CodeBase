from PIL import Image
import numpy as np
import os
from tqdm import tqdm

# Define the size of the tiles
TILE_SIZE = 25

# Load the set of images
images = []
for i in tqdm(range(3850, 3875), desc="Loading images"):
    image_filename = f"C:/Users/keato/Downloads/GOOEY PNG/images_copy/{i}.png"
    image = Image.open(image_filename).resize((TILE_SIZE, TILE_SIZE))
    images.append(image)

# Load the larger image
large_image = Image.open(r"C:\Users\keato\Downloads\UGWrxyY6dgsxBZpXs8GUh7yPi2iCg7BngJeoJL1qS9lDzy84NIV7MjO-ObHx4GDAZt6nsiaEPAldrRgmZIVWMraV2xPWrLcPyhOo.webp")
width, height = large_image.size

# Create a new image to store the mosaic
mosaic_image = Image.new("RGB", (width, height))

# Iterate over each pixel in the larger image
for x in tqdm(range(0, width, TILE_SIZE), desc="Building mosaic"):
    for y in range(0, height, TILE_SIZE):
        # Get the color of the pixel we are trying to replace
        pixel = large_image.getpixel((x, y))

        # Find the best tile to use to replace the pixel
        best_tile = None
        best_diff = float("inf")
        for tile in images:
            # Compute the average color of the tile
            tile_data = np.array(tile)
            tile_color = tuple(np.mean(tile_data, axis=(0, 1)).astype(int))

            # Compute the color difference between the tile and the pixel
            diff = sum(abs(tile_color[i] - pixel[i]) for i in range(3))

            # Update the best tile if this one is closer in color
            if diff < best_diff:
                best_tile = tile
                best_diff = diff

        # Paste the best tile into the mosaic image
        mosaic_image.paste(best_tile, (x, y))

# Create a list of GIF frames with the floating animation
gif_images = []
for i in tqdm(range(10), desc="Building GIF frames"):
    for image in images:
        offset = int(5 * np.sin(2 * np.pi * i / 10))
        new_image = Image.new("RGBA", (TILE_SIZE, TILE_SIZE), (0, 0, 0, 0))
        new_image.paste(image, (offset, offset))
        gif_images.append(new_image.convert("RGB"))

# Save the GIF
gif_images[0].save("mosaicgpt.gif", save_all=True, append_images=gif_images[1:], duration=50, loop=0)

