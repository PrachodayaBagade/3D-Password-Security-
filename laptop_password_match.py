

#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
import cv2
import numpy as np
import time
import mysql.connector

import time
from mysql.connector import Error


def get():
    global attempts
    attempts = 0
    global pswd_status
    pswd_status = 0
    global pswdEntry2
    global psw
    global psw2
    global user_name
    global user_name_entry
    global pattern_to_check
    pattern_to_check = [0,0,0,0,0]

    
    def click2(*args):
        global pswdEntry2
        global psw
        global psw2
        pswdEntry2.insert(0, 'Enter password')
        pswdEntry2.delete(0, 'end')
        psw = StringVar()
        pswdEntry2 = Entry(win2, textvariable=psw,justify=CENTER,show="*")
        pswdEntry2.place(x =274,y=330,height=30, width=250)
        pswdEntry2.config(font=("Times New Roman", 15))
        pswdEntry2.configure(background="#FFEBF9")

    def click3(*args):
        global pswdEntry2
        global psw
        global psw2
        global user_name
        global user_name_entry
        user_name_entry.insert(0, 'Enter password')
        user_name_entry.delete(0, 'end')
        user_name = StringVar()
        user_name_entry = Entry(win2, textvariable=user_name,justify=CENTER)
        user_name_entry.place(x =274,y=280,height=30, width=250)
        user_name_entry.config(font=("Times New Roman", 15))
        user_name_entry.configure(background="#FFEBF9")



    def check_pswd():
        global attempts
        global pswd_status
        global pswdEntry2
        global psw
        global psw2
        global user_name
        global user_name_entry
        global pattern_to_check
        
        pswd = psw.get()
        un = user_name_entry.get()

        mySQLconnection = mysql.connector.connect(host='localhost',database='threed_password',user='root',password='')
        sql_select_Query = "select * from password3d"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        if len(un) == 0 or len(pswd) == 0:
            label3 = Label(win2, text="Consider all fields")
            label3.configure(bg='yellow')
            label3.config(font=("Times new roman",20))
            label3.place(x = 200,y=200,height=35, width=400)
            win2.configure(bg='red')
            win2.update()
                
        else:
            matched = 0
            for r in records:
                if r[0]==un and r[1]==pswd:
                    matched = 1
                    break

            if matched == 1:
                label3 = Label(win2, text="Welcome " + r[0])
                label3.configure(bg='green')
                label3.config(font=("Times new roman",20))
                label3.place(x = 200,y=200,height=35, width=400)
                pattern_to_check=[r[1],r[2],r[3],r[4],r[0]]
                pswd_status = 1
                win2.update()
                time.sleep(2)
                win2.destroy()
            
            else:
                label3 = Label(win2, text="Incorrect Username or password")
                label3.configure(bg='red')
                label3.config(font=("Times new roman",20))
                label3.place(x = 200,y=200,height=35, width=400)
                win2.configure(bg='red')
                win2.update()
                time.sleep(2)
                win2.destroy()



    win2 = Tk()
    win2.title("Enter Password")
    win2.geometry("874x600+10+10")

    bg = PhotoImage( file = "before_img.png")

    label1 = Label(win2, image = bg)
    label1.place(x = 0,y = 0)


    user_name = StringVar()
    user_name_entry = Entry(win2, textvariable=user_name,justify=CENTER)
    user_name_entry.place(x =274,y=280,height=30, width=250)
    user_name_entry.config(font=("Times New Roman", 15))
    user_name_entry.configure(background="#FFEBF9")
    user_name_entry.insert(0, 'Enter Username')
    user_name_entry.bind("<Button-1>", click3)

    psw = StringVar()
    pswdEntry2 = Entry(win2, textvariable=psw,justify=CENTER)
    pswdEntry2.place(x =274,y=330,height=30, width=250)
    pswdEntry2.config(font=("Times New Roman", 15))
    pswdEntry2.configure(background="#FFEBF9")
    pswdEntry2.insert(0, 'Enter password')
    pswdEntry2.bind("<Button-1>", click2)


    B1 = Button(win2, text = "SUBMIT", command = check_pswd)
    B1.place(x = 274,y = 390 ,height=30, width=250)
    B1.config(font=("Times New Roman", 12))
    B1.configure(background="#FFcBd9")
    B1.configure(foreground="#000099")

    win2.mainloop()
    return pswd_status,pattern_to_check


##k,p=get()
##print(k)
##print(p)

def regi():
    global attempts
    attempts = 0
    global pswd_status
    pswd_status = 0
    global pswdEntry
    global pswdEntry2
    global psw
    global psw2
    global pswd
    global user_name
    global user_name_entry
    global un

    def click(*args):
        global pswdEntry
        global psw
        global psw2
        pswdEntry.insert(0, 'Enter password')
        pswdEntry.delete(0, 'end')
        psw = StringVar()
        pswdEntry = Entry(win2, textvariable=psw,justify=CENTER,show="*")
        pswdEntry.place(x =274,y=280,height=30, width=250)
        pswdEntry.config(font=("Times New Roman", 15))
        pswdEntry.configure(background="#FFEBF9")

    def click2(*args):
        global pswdEntry2
        global psw
        global psw2
        pswdEntry2.insert(0, 'Enter password')
        pswdEntry2.delete(0, 'end')
        psw2 = StringVar()
        pswdEntry2 = Entry(win2, textvariable=psw2,justify=CENTER,show="*")
        pswdEntry2.place(x =274,y=330,height=30, width=250)
        pswdEntry2.config(font=("Times New Roman", 15))
        pswdEntry2.configure(background="#FFEBF9")

    def click3(*args):
        global pswdEntry2
        global psw
        global psw2
        global user_name
        global user_name_entry
        user_name_entry.insert(0, 'Enter password')
        user_name_entry.delete(0, 'end')
        user_name = StringVar()
        user_name_entry = Entry(win2, textvariable=user_name,justify=CENTER)
        user_name_entry.place(x =274,y=230,height=30, width=250)
        user_name_entry.config(font=("Times New Roman", 15))
        user_name_entry.configure(background="#FFEBF9")

    
    def check_pswd():
        global attempts
        global pswd_status
        global psw
        global psw2
        global pswd
        global user_name_entry
        global un
        
        pswd = psw.get()
        pswd2 = psw2.get()
        un = user_name_entry.get()
        

        print(un)
        print(pswd)
        print(pswd2)

        if len(un) != 0:


            mySQLconnection = mysql.connector.connect(host='localhost',database='threed_password',user='root',password='')
            sql_select_Query = "select * from password3d"
            cursor = mySQLconnection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            name_already_taken = 0
            for record in records:
                if record[0].lower() == un.lower():
                    name_already_taken = 1
                    break

            if name_already_taken == 0:
            
                if pswd == pswd2:
                    if len(pswd2) == 4:
                        print("Password matched")
                        label3 = Label(win2, text="Your password is set")
                        label3.configure(bg='green')
                        label3.config(font=("Times new roman",20))
                        label3.place(x = 200,y=150,height=35, width=400)
                        win2.configure(bg='yellow')
                        
                        win2.update()
                        time.sleep(2)
                        win2.destroy()

                    else:
                        print("enter 4 digit password only")
                        label3 = Label(win2, text="enter 4 digit password only")
                        label3.configure(bg='yellow')
                        label3.config(font=("Times new roman",20))
                        label3.place(x = 200,y=150,height=35, width=400)
                        win2.configure(bg='yellow')

                else:
                        print("Password not matched")
                        label3 = Label(win2, text="Password does not matched")
                        label3.configure(bg='red')
                        label3.config(font=("Times new roman",20))
                        label3.place(x = 200,y=150,height=35, width=400)
                        win2.configure(bg='yellow')
            else:
                print("Username already taken")
                label3 = Label(win2, text="Username already taken")
                label3.configure(bg='red')
                label3.config(font=("Times new roman",20))
                label3.place(x = 200,y=150,height=35, width=400)
                win2.configure(bg='yellow')            


        else:
            print("Consider all fields")
            label3 = Label(win2, text="Consider all fields")
            label3.configure(bg='red')
            label3.config(font=("Times new roman",20))
            label3.place(x = 200,y=150,height=35, width=400)
            win2.configure(bg='yellow')            

    win2 = Tk()
    win2.title("Enter Password")
    win2.geometry("874x600+10+10")

    bg = PhotoImage( file = "before_img.png")

    label1 = Label(win2, image = bg)
    label1.place(x = 0,y = 0)

    psw = StringVar()
    pswdEntry = Entry(win2, textvariable=psw,justify=CENTER)
    pswdEntry.place(x =274,y=280,height=30, width=250)
    pswdEntry.config(font=("Times New Roman", 15))
    pswdEntry.configure(background="#FFEBF9")
    pswdEntry.insert(0, 'Enter password')
    pswdEntry.bind("<Button-1>", click)


    psw2 = StringVar()
    pswdEntry2 = Entry(win2, textvariable=psw2,justify=CENTER)
    pswdEntry2.place(x =274,y=330,height=30, width=250)
    pswdEntry2.config(font=("Times New Roman", 15))
    pswdEntry2.configure(background="#FFEBF9")
    pswdEntry2.insert(0, 'Re-enter password')
    pswdEntry2.bind("<Button-1>", click2)


    user_name = StringVar()
    user_name_entry = Entry(win2, textvariable=user_name,justify=CENTER)
    user_name_entry.place(x =274,y=230,height=30, width=250)
    user_name_entry.config(font=("Times New Roman", 15))
    user_name_entry.configure(background="#FFEBF9")
    user_name_entry.insert(0, 'Enter Username')
    user_name_entry.bind("<Button-1>", click3)


    B1 = Button(win2, text = "SUBMIT", command = check_pswd)
    B1.place(x = 274,y = 390 ,height=30, width=250)
    B1.config(font=("Times New Roman", 12))
    B1.configure(background="#FFcBd9")
    B1.configure(foreground="#000099")

    win2.mainloop()
    return un, pswd

##un,k = regi()
##print("Username set to : ",un)
##print("Password set to : ",k)

def display_message(msg,colour):

    win2 = Tk()
    win2.title("Enter Password")
    win2.geometry("874x600+10+10")

    def back():
        win2.destroy()

    bg = PhotoImage( file = "before_img.png")

    label1 = Label(win2, image = bg)
    label1.place(x = 0,y = 0)


    label3 = Label(win2, text=msg)
    label3.configure(bg=colour)
    label3.config(font=("Times new roman",28))
    label3.place(x = 250,y=250,height=40, width=374)


    B1 = Button(win2, text = "Return", command = back)
    B1.place(x = 350,y = 300 ,height=27, width=174)
    B1.config(font=("Times New Roman", 17))
    B1.configure(background="#AFC8C9")
    B1.configure(foreground="#000099")
    
    win2.mainloop()

##display_message("Pattern not matched","green")
##k = get("1234")
##print(k)





