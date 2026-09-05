from PIL import Image
import numpy as np
import os
from tqdm import tqdm

# Define the size of the tiles
TILE_SIZE = 24

# Load the set of images
images = []
for i in range(3871, 3875):
    image_filename = f"C:/Users/keato/Downloads/GOOEY PNG/images_copy/{i}.png"
    image = Image.open(image_filename).resize((TILE_SIZE, TILE_SIZE))
    images.append(image)

# Load the larger image
large_image = Image.open(r"C:\Users\keato\Downloads\9911959d74c9ba766b40ade400c1ace4.webp")
width, height = large_image.size

# Create a new image to store the mosaic
mosaic_image = Image.new("RGB", (width, height))

# Iterate over each pixel in the larger image
for x in tqdm(range(0, width, TILE_SIZE), desc="Building mosaic"):
    for y in tqdm(range(0, height, TILE_SIZE), desc="Building mosaic", leave=False):
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

# Save the mosaic image
mosaic_image.save("mosaicgpt.png")
