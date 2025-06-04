from PIL import Image, ImageDraw
import math

letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!@#"
# assert len(letters) == 64  # critical

data = input("Enter your text: ")

# Pad with spaces to make length a multiple of 4
if len(data) % 4 != 0:
    data += " " * (4 - len(data) % 4)

# Calculate image size
num_pixels = len(data) // 4
dimension = math.ceil(math.sqrt(num_pixels))

# Create white background image
img = Image.new("RGB", (dimension, dimension), (255, 255, 255))
draw = ImageDraw.Draw(img)

x, y = 0, 0
dec = 0
p = 3

for char in data:
    index = letters.find(char)
    dec += index * (64 ** p)
    p -= 1

    if p < 0:
        # Convert dec to RGB
        r = dec // 65536
        g = (dec % 65536) // 256
        b = dec % 256

        draw.point((x, y), fill=(r, g, b))

        # Move to next pixel
        y += 1
        if y >= dimension:
            y = 0
            x += 1

        # Reset
        dec = 0
        p = 3

img.save("trial2.png")
