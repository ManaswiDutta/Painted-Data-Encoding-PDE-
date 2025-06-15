from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageDraw
import math

letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!@#"
data=""
def encrypt():
    global data , letters
    data+=input.get()
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
    filepath = filedialog.asksaveasfilename(filetypes=[("png file","*.png")])
    img.save(filepath)


window = Tk()
window.title("title")
window.geometry("300x200")

label=Label(window, text = "Enter text" , font = ("arial" , 10 , "bold"))
label.grid(row=0 , column=0)
input = Entry(window , bd = 2)
input.grid(row=0,column=1)

submit = Button(window , 
                text = "Encrypt" , 
                font = ("arial" , 10 , "bold"),
                relief=RAISED , bd = 5 ,
                command=encrypt
                )
submit.grid(row=1, column=1, padx=10 , pady=10 , ipadx=50)




window.mainloop()
