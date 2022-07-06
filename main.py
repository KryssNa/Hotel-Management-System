

from tkinter import *
import datetime 
import sqlite3
import random
from PIL import Image,ImageTk
from tkinter import messagebox

root4=Tk()
root4.title('WELCOME TO HOTEL MANGEMENT SYSTEM')
root4.geometry("1550x800+0+0")
load=Image.open("67.png")
# load=load.resize(1350,720)
render=ImageTk.PhotoImage(load)
imgs=Label(root4,image=render)
imgs.place(x=0,y=0)

#logout function
def logout():
    y=messagebox.askyesno("logout","are you sure you want to log out")
    if y==YES:
        root4.destroy()
        import login
    else:
        pass

##import customer dashboard
def cust_dash():
    root4.destroy()
    import customer_dash

##import booking dashboard
def book_dash():
    root4.destroy()
    import book_dash

##import 
    
#main window button
logout_1=Button(root4,text="LOG OUT",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D",command=logout).place(x=1225,y=43)
custmor=Button(root4,text="CUSTOMERS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D",command=cust_dash).place(x=350,y=100)
booking=Button(root4,text="BOOKING",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D",command=book_dash).place(x=520,y=100)
# room=Button(root4,text="CUSTOMER BILLING DASHBOARD",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=650,y=100)
contact=Button(root4,text="REPORT AN ISSUE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=830,y=100)
payment=Button(root4,text="FOOD ITEMS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=650,y=100)


root4.mainloop()

