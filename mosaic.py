import os
import random
from PIL import Image

# Path to the folder containing the small images
image_folder = r"C:\Users\keato\Downloads\GOOEY PNG\images_copy\3871.png"

# Path to the big image
big_image_path = r"C:\Users\keato\Downloads\TwitterData\ArtPortfolio\Untitled design (12).png"

# Output mosaic image size in inches
output_width = 14
output_height = 20

# Output mosaic image resolution
output_resolution = 1280

# Load the big image
big_image = Image.open(big_image_path)

# Calculate the output mosaic image size in pixels
output_width_px = int(output_width * output_resolution)
output_height_px = int(output_height * output_resolution)

# Resize the big image to the output mosaic size
big_image = big_image.resize((output_width_px, output_height_px))

# Calculate the dimensions of each small image
small_image_width = int(output_width_px / big_image.width)
small_image_height = int(output_height_px / big_image.height)

# Get a list of all image files in the folder
image_files = os.listdir(image_folder)

# Number of small images to use in the mosaic
num_images = 500
if num_images > len(image_files):
    num_images = len(image_files)

# Choose num_images random images from the list
chosen_image_files = random.sample(image_files, num_images)

# Load the chosen images and resize them
small_images = []
for file in chosen_image_files:
    image_path = os.path.join(image_folder, file)
    image = Image.open(image_path)
    image = image.resize((small_image_width, small_image_height))
    small_images.append(image)

# Create a new blank image for the mosaic
mosaic_image = Image.new('RGB', (output_width_px, output_height_px))

# Paste the small images onto the mosaic image
x_offset = 0
y_offset = 0
for image in small_images:
    mosaic_image.paste(image, (x_offset, y_offset))
    x_offset += small_image_width
    if x_offset >= output_width_px:
        x_offset = 0
        y_offset += small_image_height

# Save the output mosaic image
mosaic_image.save('mosaicgpt.png')
