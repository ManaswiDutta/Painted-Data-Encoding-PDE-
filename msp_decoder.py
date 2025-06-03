from PIL import Image, ImageDraw
letters=" ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?abcdefghijklmnopqrstuvwxyz"
data = ""
img = Image.open("trial2.png")
x,y=0,0
while img.getpixel((x,y)) != (255, 255, 255):
    r, g, b = img.getpixel((x,y))
    dec = (r * 65536) + (g * 256) + b
    a = dec // 262144
    dec = dec % 262144
    b = dec // 4096
    dec = dec % 4096
    c = dec // 64
    d = dec % 64
    data += letters[a] + letters[b] + letters[c] + letters[d]
    if y==144:
        x+=1
        y=0
    else:
        y+=1

print(data)
