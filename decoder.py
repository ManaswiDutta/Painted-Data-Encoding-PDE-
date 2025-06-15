from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageDraw
import math
letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!@#"
output = ""
def openfile():
    global letters , output
    filepath = filedialog.askopenfilename(title="select image" , filetypes=[("Encrypted file" , "*.png")])
    filename.insert(0,filepath)

def decrypt():
    global letters , output 
    img = Image.open(filename.get())
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

    output="The Data is :  "+data.strip() 
    m = Label(root,text = output)
    m.grid(row=3,column=0)


root = Tk()
root.geometry("400x200")

select = Button(root, text = "Load image", font = ("arial" , 10 , "bold") ,  command=openfile)
select.grid(row=0,column=0)

filename=Entry(root)
filename.grid(row=0 , column =1)

work = Button(root, text = "Decrypt", font = ("arial" , 10 , "bold") , command=decrypt)
work.grid(row=1,column=0)

root.mainloop()
