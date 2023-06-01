#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
import cv2
import numpy as np
import laptop_password_match
import Face_Recognitions

import time
before_img = "before_img.png"
after_img  = "after_img.png"

global before_img_read
global after_img_read
global win2


before_img_read = cv2.imread(before_img)
after_img_read  = cv2.imread(after_img)

#Create an instance of tkinter frame

global pswd_entry
pswd_entry = 0

global pattern_entered
pattern_entered = []

global check_pattern
check_pattern = 0

global pattern_to_check
pattern_to_check = [0,0,0,0,0]

global pswd_correct
pswd_correct = 0

global done
done = 0


def win_get():

    win = Tk()
    win.geometry("874x600+10+10")
        
    def draw_line(e):
        global before_img_read
        global after_img_read
        global win2
        global pswd_entry
        global pattern_entered
        global pswd_correct
        global psw
        global pswdEntry
        global done
        global check_pattern
        global pattern_to_check
        
        x, y = e.x, e.y
        trophy = [310,430,100,200]  
        apple = [345,400,210,270]
        cup = [310,430,340,410]
        glasses = [310,430,450,550]
        books = [310,430,600,700]
        lamp = [100,170,450,550]
        dustbin = [430,530,570,650]
        shoes = [450,570,700,810]
        curtains = [150,370,800,874]
        laptop = [290,390,265,355]
        photo = [160,250,520,690]

        contents = [trophy,apple,cup,glasses,books,lamp,dustbin,shoes,curtains,laptop,photo]
        content_name = ["trophy","apple","cup","glasses","books","lamp","dustbin","shoes","curtains","laptop","photo"]

        for i in range(len(contents)):        
            if contents[i][0] <= y and contents[i][1] >= y and contents[i][2] <= x and contents[i][3] >= x:
                if content_name[i] == "laptop" and pswd_correct == 0:
    ##                print(pattern_to_check[0])
                    win.destroy()
                    pswd_correct,pattern_to_check = laptop_password_match.get()
                    print(pswd_correct)
                    win_get()

                if pswd_correct == 1 and done != 1 and check_pattern!= 3:
                    crop = after_img_read[contents[i][0]:contents[i][1], contents[i][2]:contents[i][3]]
                    before_img_read[contents[i][0]:contents[i][1], contents[i][2]:contents[i][3]] = crop
                    
                    blue,green,red = cv2.split(before_img_read)
                    img = cv2.merge((red,green,blue))
                    im = Image.fromarray(img)
                    img= ImageTk.PhotoImage(im)
                    canvas.itemconfig(container_img,image=img)
                    print(content_name[i])
                    if content_name[i] != "laptop":
                        pattern_entered.append(content_name[i])
                    print(pattern_entered)
                    if len(pattern_entered) >= 3:
                        done = 1
     
                if done == 1:
                    check_pattern = 0
                    for ind in range(3):
                        if pattern_to_check[ind+1] == pattern_entered[ind]:
                            check_pattern += 1
                    print(check_pattern)
                    
                    if check_pattern == 3:
                        done = 2
                        pattern_entered = []
                        pswd_correct = 0
                        win.destroy()
                        laptop_password_match.display_message("Pattern matched","green")
                        win_get()
                    else:
                        done = 0
                        pattern_entered = []
                        pswd_correct = 0
                        before_img = "before_img.png"
                        before_img_read = cv2.imread(before_img)
                        blue,green,red = cv2.split(before_img_read)
                        img = cv2.merge((red,green,blue))
                        im = Image.fromarray(img)
                        img= ImageTk.PhotoImage(im)
                        canvas.itemconfig(container_img,image=img)

                        win.destroy()
                        laptop_password_match.display_message("Pattern not matched","red")
                        win_get()
                                            
                if content_name[i] == "photo" and check_pattern== 3:
                        print("Face Recognition")
                        check_pattern = 0
                        done = 0
                        pattern_entered = []
                        pswd_correct = 0
                        
                        if pattern_to_check[4] == Face_Recognitions.face_id():
                            win.destroy()
                            laptop_password_match.display_message("Login Success","green")
                            win_get()
                        else:
                            win.destroy()
                            laptop_password_match.display_message("Face not matched","red")
                            win_get()
                                                    
                win.mainloop()
        print(x,y)

    canvas= Canvas(win, width= 874, height= 600)

    blue,green,red = cv2.split(before_img_read)
    img = cv2.merge((red,green,blue))
    im = Image.fromarray(img)

    img= ImageTk.PhotoImage(im)

    container_img = canvas.create_image(0,0,anchor="nw",image=img)
    canvas.pack()

    win.bind('<ButtonPress-1>', draw_line)


    win.mainloop()

win_get()
