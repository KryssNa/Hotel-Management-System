
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

root=Tk()

root.title("New Registration")
root.geometry('1550x800+0+0')
load=Image.open("67.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
#==============================frame==================================
frame = Frame(root, bg="black")
frame.place(x=400, y=140, width=620, height=450)

# ===========================Varibales============================#

Get_started = Label(root, text="NEW REGISTRATION", font=("Montserrat SemiBold", 16, "bold"), fg="white",
                    bg="black", borderwidth=0).place(x=605, y=190)

name  = Entry(root, font=("Arial", 12,), bg="white")
name.place(x=630, y=250)

username  = Entry(root, font=("Arial", 12,), bg="white")
username.place(x=630, y=300)

password  = Entry(root,show="*", font=("Arial", 12,), bg="white")
password.place(x=630, y=350)

conpass = Entry(root,show="*",font=("Arial", 12,), bg="white")
conpass.place(x=630, y=400)

ran = Entry(root, text=2, font=("Arial", 12,), bg="white")
ran.place(x=632, y=444)

l_name = Label(root, text="Name:", font=("Montserrat", 12), fg="white", bg="black").place(x=565,y=250)
l_User = Label(root, text="Username:", font=("Montserrat", 12), fg="white", bg="black").place(x=535, y=300)
l_Pass = Label(root, text="Password:", font=("Montserrat", 12), fg="white",bg="black").place(x=535, y=350)
l_CPass= Label(root, text="Confirm Password:", font=("Montserrat", 12), fg="white",bg="black").place(x=470, y=400)
l_id   = Label(root, text="ID Number:", font=("Montserrat", 12), fg="white", bg="black").place(x=525, y=440)
log    = Button(root, text="Register", font=("Montserrat bold",11), bg="#5C4B90",width=14,height=1,fg="black", cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black")
log.place(x=655, y=492,width=135)

root.mainloop()


