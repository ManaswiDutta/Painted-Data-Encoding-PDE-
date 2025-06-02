import pyautogui
import keyboard
import time
import random
letters=" ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?abcdefghijklmnopqrstuvwxyz"
color_y = 120
color_x = 1091
x,y=40,279

data=str(input("enter your text:  "))
print("press p to start...")
number = 1
while number ==1:
    if keyboard.is_pressed('p'):
        for letter in data :
            index=letters.find(letter)
            binary=format(index,'06b')
            bin_srt=str(binary)
            for bit in bin_srt:
                if bit=="1":
                    pyautogui.click(x,y)
                    if y==313:
                        x+=1
                        y=279
                    else:
                        y+=1
                else:
                    if y==313:
                        x+=1
                        y=279
                    else:
                        y+=1
    elif keyboard.is_pressed('esc'):
        number+=1




# if keyboard.is_pressed('esc'):
print("exiting...")
    