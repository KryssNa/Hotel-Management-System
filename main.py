##importing necessary modules
from tkinter import *
import datetime 
import sqlite3
import random
from PIL import Image,ImageTk
from tkinter import messagebox

#main window
root4=Tk()
root4.title('WELCOME TO HOTEL MANGEMENT SYSTEM')#window title
root4.geometry("1550x850")
root4.config(bg="#501F1F")

#label moto
Label(root4,text="Feel Like Home",font=('Consolas',30,"bold"),bg="#501F1F",fg="white").place(x=10,y=620)

##background image
photo=Image.open("image/trypp.png")
load=photo.resize((1135,800))
resize_img=ImageTk.PhotoImage(load)
imgs=Label(root4,image=resize_img)
imgs.place(x=400,y=45)

##image
photoss=Image.open("image/logo.png")
loads=photoss.resize((396,380))
resize_imgs=ImageTk.PhotoImage(loads)
imgss=Label(root4,image=resize_imgs)
imgss.place(x=0,y=45)

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
    
##reports and feedback function
def reports():
    root=Toplevel()
    root.title("Contact & Help")
    root.geometry('680x420')
    root.configure(bg="#39065D")

    try:
        conn=sqlite3.connect("customerS.db")#connecting to database
        c=conn.cursor()
        c.execute("""CREATE TABLE reports(
            feedback integer,
            report text)""")
        conn.commit()
        conn.close()
    except:
        pass

    ##feedback and report function
    def add_data():
        # print(txtfield.get("1.0",END))
        a=txtfield.get()
        if a =="":
            messagebox.showerror("Error","All field are required")
        else:
            try:
                conn= sqlite3.connect("customerS.db")
                c=conn.cursor()
                # print("yes")
                c.execute("INSERT INTO reports VALUES(:feedback,:report)",{
                    "feedback":txt54.get(),
                    "report":txtfield.get()
                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Success",'''
                Thanks for reporting.
                Your Report has been sent your report to our 
                Database Engineer.
                This issue will be resolved shortly.
                Thanks!''')
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}")


    #label issue
    reort=Label(root,text="REPORT AN ISSUE",font=('Montserrat Semibold',25),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=170,y=20)
    reort1=Label(root,text='''
    If you're having trouble after using this application,
    you've come to the right place. Please use this form 
    to tell us about the issue you're experiencing.
    Please provide a detailed description of this issue,including:
    What you were doing when the problem occurred?
    What you expected to happend?
    What actually happened?
    ''',font=('Montserrat',10),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=300,y=60)
    reort2=Label(root,text="CONTACT US",font=('Montserrat',15,"bold"),bg="#39065D",border=0,fg="green",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=88,y=130)
    reort2=Label(root,text='''
    Mailing Address:
    krishna.kryss@gmail.com
    HOTEL MANAGEMENT SYSTEM
    Designed and Programed by
    Team:Hype
    220179@softwarica.edu.np
    +9779811787904
    Softwarica College of IT & E-Commerce
    ''',font=('Montserrat',12),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=0,y=150)
    txt54=StringVar()
    x=random.randint(1,100)
    txt54.set(str(x))
    print(x)

    #entry to write reports
    txtreport=Entry(root,textvariable=txt54,font=("Arial", 10))
    txtfield=Entry(root,font="Montserrat")
    txtfield.place(x=300,y=200,height=150,width=350)
    report_button =Button(root, text="SUBMIT  REPORT",command=add_data,font=("Montserrat bold",9,"bold"),width=18,bg="#FFA726",fg="black",activebackground="#FFA726",activeforeground="#FFA726",cursor="hand2")
    report_button.place(x=400,y=370)
 

#label to write words on main window
Label(root4,text="L:Softwarica College,Kathmandu",font=('Consolas',11,"bold"),bg="#501F1F",fg="white").place(x=350,y=15)
        
Label(root4,text="P:+9779811787904",font=('Consolas',12,"bold"),bg="#501F1F",fg="white").place(x=180,y=15)
        
#logout , customer ,book now, contact & help ,food item , home, button & their function
logout1=Button(root4,text="LOG OUT",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D",command=logout).place(x=1450,y=6)
custmor=Button(root4,text="CUSTOMERS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D",command=cust_dash).place(x=1100,y=7)
booking=Button(root4,text="Book Now",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D",command=book_dash).place(x=820,y=6)
con_btn=Button(root4,text="Contact & Help",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#39065D",command=reports).place(x=1250,y=6)
foodIte=Button(root4,text="FOOD ITEMS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D",command=bill_dash).place(x=950,y=7)
homebtn=Button(root4,text="Home ",font=('Consolas',14,"bold"),bg="#A0522D",border=1,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D",command=main).place(x=700,y=6)

root4.mainloop()
