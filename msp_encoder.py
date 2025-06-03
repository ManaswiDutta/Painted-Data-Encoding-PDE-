from PIL import Image, ImageDraw
letters=" ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?abcdefghijklmnopqrstuvwxyz"

img = Image.new("RGB", (144, 144), (255, 255, 255))
draw = ImageDraw.Draw(img) 
data = str(input("enter your text:  "))
if len(data) % 4 != 0:
    data+= " " * (4 - len(data) % 4)  # Padding to make length a multiple of 4
x,y = 0,0
dec = 0
p = 3
for char in data:
    index = letters.find(char)
    if p != 0:
        dec += index*(64**p)
        p-=1
    else:
        dec += index
        p = 3
        a = dec // 65536
        dec = dec % 65536
        b= dec // 256
        c = dec % 256

        draw.point((x,y),fill =(a,b,c) )
        if y==144:
            x+=1
            y=0
        else:
            y+=1
        dec = 0


img.save("trial2.png")
