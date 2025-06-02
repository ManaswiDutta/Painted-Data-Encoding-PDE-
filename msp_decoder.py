import pyautogui
import keyboard
import time
import random
letters=" ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?abcdefghijklmnopqrstuvwxyz"
output = ""
x,y=40,279
print("press p to start...")
number = 1
bin_srt = ""
black = pyautogui.pixel(1091, 120)
while number ==1:
    if keyboard.is_pressed('p'):
        time.sleep(0.06)
        while number==1:
            bin_srt = ""

            for _ in range(6):
                if pyautogui.pixel(x, y) == black:
                    bin_srt += "1"
                else:
                    bin_srt += "0"

                    # Move to next pixel down, then right after 313
                if y == 313:
                    x += 1
                    y = 279
                    pyautogui.moveTo(x, y)                    
                    # time.sleep(0.1)  
                else:
                    y += 1

                    # time.sleep(0.1)
            index = int(bin_srt,2)
            output=output+letters[index]
            index=0
               
            if keyboard.is_pressed('esc'):
                number+=1
                print("exiting....")

    elif keyboard.is_pressed('esc'):
        number+=1
        print("exiting....")


print("the output is:   " + output)


