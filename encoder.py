from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageDraw
import math

def load():
    global path,text
    path = filedialog.askopenfilename(title="Open File", filetypes=[("Text file", ".txt")])
    with open(path, 'r') as file:
        file_content = file.read()
        text.delete(1.0, END)
        text.insert(1.0, file_content)

def encrypt():
    data = text.get(1.0, END)
    if len(data) % 3 != 0:
        data += " " * (3 - len(data) % 3)

    num_pixels = len(data) // 3
    dimension = math.ceil(math.sqrt(num_pixels))

    img = Image.new("RGB", (dimension, dimension), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    x, y = 0, 0
    for i in range(0, len(data), 3):
        r = ord(data[i])
        g = ord(data[i+1])
        b = ord(data[i+2])
        draw.point((x, y), fill=(r, g, b))
        x += 1
        if x >= dimension:
            x = 0
            y += 1

    filepath = filedialog.asksaveasfilename(filetypes=[("PNG file", "*.png")])
    if filepath:  # Make sure user didn't cancel
        img.save(filepath)


        


window = Tk()
# window.geometry("500x500")
window.title("Text to Image Encoder")

top = Frame(window).pack(side='left')

Button(top, text="enter text to encrypt",
        command=encrypt, 
        font = ("Century", 10 , "bold"),
        relief=RAISED, bd = 5,
        background="#c0c0c0",
        activebackground="#808080"
        ).pack()


Button(top, 
       text="load text file", 
       command=load, 
       font = ("century" , 10 , "bold"),
       relief=RAISED, bd = 5,
       background="#c0c0c0",
       activebackground="#808080"
        ).pack()


text = Text(window, height=10, width=50, font=("EB Garamond", 10))
text.pack(side='right')

window.mainloop()
