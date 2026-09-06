from PIL import Image, ImageDraw, ImageFont

# Get the image path
image_path = input("Enter the path to the image file: ")

# Open the image
image = Image.open(image_path)

# Convert the image to grayscale
image = image.convert('L')

# Resize the image
width, height = image.size
aspect_ratio = height/width
new_width = 120
new_height = int(aspect_ratio * new_width * 0.55)
resized_image = image.resize((new_width, new_height))

# Define the ASCII characters to represent the pixel values
ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Convert the pixels to ASCII characters
pixels = resized_image.getdata()
ascii_image = ''
for pixel in pixels:
    ascii_image += ascii_chars[int(pixel/25)]

# Create a new image from the ASCII characters
ascii_width, ascii_height = resized_image.size
ascii_image = Image.new('RGB', (ascii_width, ascii_height), color=(255, 255, 255))
ascii_draw = ImageDraw.Draw(ascii_image)
font = ImageFont.load_default()

x = y = 0
for char in ascii_image:
    if char == '\n':
        y += font.getsize(' ')[1]
        x = 0
    ascii_draw.text((x, y), char, fill=(0, 0, 0), font=font)
    x += font.getsize(char)[0]

# Print the ASCII art representation of the image
print(ascii_image)

# Save the ASCII art as a PNG file
ascii_image.save(asciiartgpt.png)


