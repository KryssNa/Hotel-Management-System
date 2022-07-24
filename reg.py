##import important module
from tkinter import font, messagebox
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import random

#creating window
window=Tk()
window.title("New Registration")
window.geometry('1550x800+0+0')
window.config(bg="#501F1F")

#background image
photo=Image.open("image/signuppic.jpg")
load=photo.resize((1550,750))
resize_img=ImageTk.PhotoImage(load)
imgs=Label(window,image=resize_img)
imgs.place(x=0,y=35)

# creating a database table
try:
    conn=sqlite3.connect('admins.db')##connecting database
    c=conn.cursor()
    c.execute("""CREATE TABLE users(
        fname text,
        lname text,
        email text PRIMARY KEY,
        phone text,
        password text,
        cpass text,
        q1 text,
        q2 text,
        q3 text,
        status boolean
    )""" )
    conn.commit()
    conn.close()
except:
    pass

##bring back to login
def backlogin():
    window.destroy()
    import login


#signup function
def signup():
    def openlogin():
        window.destroy()
        import login
    
    def remove(event):
        a=fname_ent.get()
        if a=="First Name":
            fname_ent.delete(0, END)

    def remove1(event):
        a=lname_ent.get()
        if a=="Last Name":
            lname_ent.delete(0, END)
    
    #show password functions for passwords
    def show():
        if (showw.get()==1):
            password_ent.config(show='')
        else:
            password_ent.config(show='*')

    #function to show
    def show2():
        if (showww.get()==1):
            cpass_ent.config(show='')
        else:
            cpass_ent.config(show='*')
    #==============================frame==================================
    frame = Frame(window, bg="black")
    frame.place(x=400, y=140, width=620, height=450)

    # ===========================Varibales============================#

    Get_started = Label(window, text="NEW REGISTRATION", font=("Montserrat SemiBold", 16, "bold"), fg="white",
                        bg="black", borderwidth=0).place(x=605, y=190)

    fname_ent=Entry(window,font=("Arial", 11,), bg="white")
    fname_ent.insert(0, 'First Name')
    fname_ent.place(x=630, y=250, width=85,height=23)
    fname_ent.bind('<FocusIn>', remove) #bind function is used to montior the movement of mouse

    lname_ent=Entry(window,font=("Arial", 11,), bg="white")
    lname_ent.insert(0, 'Last Name')
    lname_ent.place(x=730, y=250, width=85,height=23)
    lname_ent.bind('<FocusIn>', remove1)

    email_ent = Entry(window, text=2, font=("Arial", 12,), bg="white")
    email_ent.place(x=630, y=300)

    phone_ent = Entry(window, font=("Arial", 12,), bg="white")
    phone_ent.place(x=630, y=350)

    password_ent  = Entry(window,show="*", font=("Arial", 12,), bg="white")
    password_ent.place(x=630, y=400)
    password_ent.bind('<FocusIn>')
    showw=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=showw,bg='white',command=show).place(x=830,y=400) #show password checkbutton
    ##entry bbox for label
    cpass_ent = Entry(window,show="*",font=("Arial", 12,), bg="white")
    cpass_ent.place(x=630, y=444)
    cpass_ent.bind('<FocusIn>')
    showww=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=showww,bg='white',command=show2).place(x=830,y=444) #show password checkbutton
    ##label names
    l_name = Label(window, text="Name:", font=("Montserrat", 12), fg="white", bg="black").place(x=565,y=250)
    l_email = Label(window, text="Email:", font=("Montserrat", 12), fg="white", bg="black").place(x=565, y=300)
    l_Pass = Label(window, text="Password:", font=("Montserrat", 12), fg="white",bg="black").place(x=535, y=400)
    l_CPass= Label(window, text="Confirm Password:", font=("Montserrat", 12), fg="white",bg="black").place(x=475, y=440)
    l_phone   = Label(window, text="Phone Number:", font=("Montserrat", 12), fg="white", bg="black").place(x=500, y=350)
    
       
#verification function to check the validation of entered data
    def verify():
        a=fname_ent.get()
        b=lname_ent.get()
        c=email_ent.get()
        d=phone_ent.get()
        e=password_ent.get()
        f=cpass_ent.get()

        if (a=="" or a=="First Name") or (b=="" or b=="Last Name") or (c=="") or (d=="") or (e=="") or (f==""):
            messagebox.showerror("Signup","One or More Fields Empty.")
        elif "@" and ".com" not in c:
            messagebox.showerror("Signup","Invalid Email")
        elif len(e)<6 or len(f)<6:
            messagebox.showerror("Signup","Password must be more than 6 characters")
        elif len(d)!=10:
            messagebox.showerror("Signup","Invalid Phone Number Length")
        elif e!=f:
            messagebox.showerror("Signup","Passwords Mismatch")
        else:
            try:
                int(d)
                sques()
            except:
                messagebox.showerror("Signup","Invalid Phone Number")


    ##function to verify and submit
    def sques():
        a=StringVar()
        b=StringVar()
        d=StringVar()

        Frame(height=330,width=350,bg='white').place(x=775,y=210)
        
        Label(text="Security Questions",font=('Arial',16,'bold'),bg='white').place(x=847,y=210)

        Label(text="Q1: What is your favourite destination?",bg='white').place(x=805,y=255)
        Entry(window, textvariable=a).place(x=805, y=280, width=290, height=30)
        
        Label(text="Q2: What is the name of your first teacher name?",bg='white').place(x=805,y=330)
        Entry(window, textvariable=b).place(x=805, y=350, width=290, height=30)

        Label(text="Q3: What is the name of your favourite idol?",bg='white').place(x=805,y=400)
        Entry(window,textvariable=d).place(x=805, y=420, width=290, height=30)

        #verification for security questions
        def verify2():
            aa=a.get()
            bb=b.get()
            cc=d.get()

            if aa=="" or bb=="" or cc=="":
                messagebox.showerror("Security Questions","One or more fields empty")
            else:
                submit()
        ##inserting details into database
        def submit():
            conn=sqlite3.connect('admins.db')
            c=conn.cursor()
            c.execute("INSERT INTO users VALUES (:fname_ent, :lname_ent, :email_ent, :phone_ent, :password_ent, :cpass_ent,:q1,:q2,:q3,:status)",
            {
                'fname_ent':fname_ent.get(),
                'lname_ent':lname_ent.get(),
                'email_ent':email_ent.get(),
                'phone_ent':phone_ent.get(),
                'password_ent':password_ent.get(),
                'cpass_ent':cpass_ent.get(),
                'q1':a.get(),
                'q2':b.get(),
                'q3':d.get(),
                'status':False
                })
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Signup","User Registered Successfully")

            openlogin()
            
        Button(window,text="Register", font=("Montserrat bold",11), bg="#F47F16",width=14,height=1,fg="black",command=verify2,
                cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black").place(x=855, y=462,width=135)
    Button(window,text="Register", font=("Montserrat bold",11), bg="#F47F16",width=14,height=1,fg="black",command=verify,
                cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black").place(x=650, y=492,width=135)
    
    # Button(window,text="Back LogIN", font=("Montserrat bold",11), bg="#5C4B90",width=14,height=1,fg="black",command=backlogin,
    #             cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black").place(x=565, y=492,width=105)
    
signup()

#logout function
def login():
    window.destroy()
    import login
    
    # messagebox.showerror("Error","Sign Up first?")
    # if y==YES:
    #     window.destroy()
    #     import login
    # else:
    #     pass

##import customer dashboard
def cust_dash():
    messagebox.showerror("Error","Sign Up first?")
    # window.destroy()
    # import customer_dash

##import booking dashboard
def book_dash():
    messagebox.showerror("Error","Sign Up first?")
    # window.destroy()
    # import book_dash

##import billdash
def bill_dash():
    messagebox.showerror("Error","Sign Up first?")
    # tmsg.showinfo("Error","Already on Billing Dashboard")
    
##head to main window
def main():
    messagebox.showerror("Error","Sign Up first?")
    # window.destroy()
    # import main
    
##reports and feedback function
def reports():
    root=Toplevel()
    root.title("REPORT AN ISSUE")
    root.geometry('680x420')
    root.configure(bg="#39065D")

    try:
        #creating table reports
        conn=sqlite3.connect("customerS.db")##connecting database
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
                conn= sqlite3.connect("customerS.db")##connecting database
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
            except Exception as es:##exception
                messagebox.showerror("Error", f"error due to:{str(es)}")##print exception if error occurs


    #report label
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

    ##entry to write reports
    txtreport=Entry(root,textvariable=txt54,font=("Arial", 10))
    txtfield=Entry(root,font="Montserrat")
    txtfield.place(x=300,y=200,height=150,width=350)
    report_button =Button(root, text="SUBMIT  REPORT",command=add_data,font=("Montserrat bold",9,"bold"),width=18,bg="#FFA726",fg="black",activebackground="#FFA726",activeforeground="#FFA726",cursor="hand2")
    report_button.place(x=400,y=370)


#main window button
logout1=Button(window,text="Log In",font=('Consolas',14,"bold"),bg="#A0522D",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=login).place(x=1450,y=0)
custmor=Button(window,text="CUSTOMERS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=cust_dash).place(x=1100,y=1)
booking=Button(window,text="Book Now",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=book_dash).place(x=820,y=0)
con_btn=Button(window,text="Contact & Help",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=reports).place(x=1250,y=0)
foodIte=Button(window,text="FOOD ITEMS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=bill_dash).place(x=950,y=1)
homebtn=Button(window,text="Home ",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=main).place(x=700,y=0)


window.mainloop()


