from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

import sqlite3

conn=sqlite3.connect("kryss.db")
c=conn.cursor()
# c.execute("""CREATE TABLE  userdetail(
#     f_name text,
#     l_name text,
#     username text,
#     password text,
#     c_password text,
#     id_num integer
#     )""")
# print("Table created successfully")

root=Tk()
root.title("Hotel Management System")
root.geometry("1440x1024")

#for bg image
image1=Image.open("67.png")
photo=ImageTk.PhotoImage(image1)
image_label=Label(image=photo)
image_label.pack()



##login page

#for frame
myframe=Frame(root,height=350,width=290,bg="black",pady=20,padx=35)
myframe.place(x=505,y=110)

#for username &password, entry widget and submit button

label_getstarted=Label(myframe,text="Get started",font=("Montserrat SemiBold", 15, "bold"),fg="white",bg="black")
label_getstarted.place(x=50,y=0)

user=Label(myframe,text="Username",fg="white",bg="black",font=("Montserrat light", 11, "bold"))
user.place(x=10,y=40)
userentry=Entry(myframe,font=("Regular", 12,))
userentry.place(x=10,y=65,height=25,width=185)

password=Label(myframe,text="Password",fg="white",bg="black",font=("Montserrat light", 11, "bold"))
password.place(x=10,y=100)
passentry=Entry(myframe,font=("Regular", 12,))
passentry.place(x=10,y=125,height=25,width=185)

b=Button(myframe,text="Login",bg="#F47F16",fg="black", cursor="hand2", borderwidth=0,width=9, activebackground="#F47F16",
          font=("Montserrat SemiBold", 11, "bold"))
b.place(x=65,y=160)


New_Reg = Button(myframe, text="NEW REGISTRATION",font=("Montserrat SemiBold",9,), fg="white", bg="black", borderwidth=0,cursor="hand2",activebackground="black")
New_Reg.place(x=0, y=260)

For_got = Button(myframe, text="RESET PASSWORD?", font=("Montserrat SemiBold",9,), fg="white", bg="black",activebackground="black",
                         borderwidth=0, cursor="hand2")
For_got.place(x=0, y=285)

root.mainloop()