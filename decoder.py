from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw
import math

def decrypt():
    filepath = filedialog.askopenfilename(filetypes=[("PNG file", "*.png")])
    if not filepath:
        return  # user canceled

    img = Image.open(filepath)
    pixels = img.load()

    width, height = img.size
    message = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Ignore white filler pixels (255,255,255)
            if (r, g, b) == (255, 255, 255):
                continue
            message += chr(r) + chr(g) + chr(b)

    # Trim off any padding spaces added during encryption
    message = message.rstrip()

    # Show the decoded message in the text box
    text.delete(1.0, END)
    text.insert(1.0, message)










window = Tk()



Button(window, 
       text="decode from image", 
       command=decrypt, 
       font=("Century", 10, "bold"),
       relief=RAISED, bd=5,
       background="#c0c0c0",
       activebackground="#808080"
       ).pack()

text = Text(window, height=20, width=50, font=("Arial", 12))
text.pack(padx=10, pady=10)

window.mainloop()
