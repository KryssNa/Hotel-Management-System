##importing modules
from tkinter import *
import datetime 
import sqlite3
import random
from PIL import Image,ImageTk
from tkinter import messagebox

#main window
root4=Tk()
root4.title('WELCOME TO HOTEL MANGEMENT SYSTEM')
root4.geometry("1550x850")
root4.config(bg="#501F1F")

##image
load=Image.open("trypp.png")
load=load.resize((1135,800))
render=ImageTk.PhotoImage(load)
imgs=Label(root4,image=render)
imgs.place(x=400,y=45)

#logout function
def logout():
    y=messagebox.askyesno("LogOut","Are you sure you want to Log Out")
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

##import billdash
def bill_dash():
    root4.destroy()
    import bill_win
    
def main():
    messagebox.showinfo("Error","Already on Main Page")    

#label to write words on main window
Label(root4,text="L:Softwarica College,Kathmandu",font=('Consolas',11,"bold"),bg="#501F1F",fg="white").place(x=350,y=15)
        
Label(root4,text="P:+9779811787904",font=('Consolas',12,"bold"),bg="#501F1F",fg="white").place(x=180,y=15)
        
#main window button
logout1=Button(root4,text="LOG OUT",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D",command=logout).place(x=1450,y=6)
custmor=Button(root4,text="CUSTOMERS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D",command=cust_dash).place(x=1100,y=7)
booking=Button(root4,text="Book Now",font=('Consolas',14,"bold"),bg="#A0522D",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D",command=book_dash).place(x=820,y=6)
con_btn=Button(root4,text="Contact & Help",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D").place(x=1250,y=6)
foodIte=Button(root4,text="FOOD ITEMS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D",command=bill_dash).place(x=950,y=7)
homebtn=Button(root4,text="Home ",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D",command=main).place(x=700,y=6)

root4.mainloop()
