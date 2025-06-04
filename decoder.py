from PIL import Image

letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!@#"
# assert len(letters) == 64  # critical

img = Image.open("trial2.png")
width, height = img.size

data = ""
x, y = 0, 0

while x < width:
    pixel = img.getpixel((x, y))

    # Stop if white pixel (end marker)
    if pixel == (255, 255, 255):
        break

    r, g, b = pixel
    dec = (r * 65536) + (g * 256) + b

    a = (dec // 262144) % 64
    dec = dec % 262144
    b = (dec // 4096) % 64
    dec = dec % 4096
    c = (dec // 64) % 64
    d = dec % 64

    data += letters[a] + letters[b] + letters[c] + letters[d]

    y += 1
    if y >= height:
        y = 0
        x += 1

print("The Data is :  "+data.strip())
