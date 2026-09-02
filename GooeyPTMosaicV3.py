from PIL import Image
import numpy as np
import os
from tqdm import tqdm

# Define the size of the tiles
TILE_SIZE = 24

# Get the path to the directory containing the smaller images
sm_images_path = input("Enter path to directory containing smaller images: ")

# Load the set of images
images = []
for i in range(3871, 3875):
    image_filename = os.path.join(sm_images_path, f"{i}.png")
    image = Image.open(image_filename).resize((TILE_SIZE, TILE_SIZE))
    images.append(image)

# Get the path to the larger image file
lg_image_path = input("Enter path to larger image file: ")

# Load the larger image
large_image = Image.open(lg_image_path)
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

# Get the name of the file to save the mosaic image as
output_file = input("Enter name of file to save mosaic image as (including extension): ")

# Save the mosaic image
mosaic_image.save(output_file)
