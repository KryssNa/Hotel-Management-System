
from tkinter import font, messagebox
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

window=Tk()

window.title("New Registration")
window.geometry('1550x800+0+0')
load=Image.open("67.png")
render=ImageTk.PhotoImage(load)
img=Label(window,image=render)
img.place(x=0,y=0)

# creating a database table
try:
    conn=sqlite3.connect('admins.db')
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
    
    cpass_ent = Entry(window,show="*",font=("Arial", 12,), bg="white")
    cpass_ent.place(x=630, y=444)
    cpass_ent.bind('<FocusIn>')
    showww=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=showww,bg='white',command=show2).place(x=830,y=444) #show password checkbutton

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


    
    def sques():
        a=StringVar()
        b=StringVar()
        d=StringVar()

        Frame(height=330,width=350,bg='white').place(x=775,y=210)
        
        Label(text="Security Questions",font=('Arial',16,'bold'),bg='white').place(x=847,y=210)

        Label(text="Q1: What is your favourite food?",bg='white').place(x=805,y=255)
        Entry(window, textvariable=a).place(x=805, y=280, width=290, height=30)
        
        Label(text="Q2: What is the name of your first pet?",bg='white').place(x=805,y=330)
        Entry(window, textvariable=b).place(x=805, y=350, width=290, height=30)

        Label(text="Q3: What is the name of your childhood best friend?",bg='white').place(x=805,y=400)
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
            
        Button(window,text="Register", font=("Montserrat bold",11), bg="#5C4B90",width=14,height=1,fg="black",command=verify2,
                cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black").place(x=805, y=442,width=135)
    Button(window,text="Register", font=("Montserrat bold",11), bg="#5C4B90",width=14,height=1,fg="black",command=verify,
                cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black").place(x=685, y=492,width=135)
    
    Button(window,text="Back LogIN", font=("Montserrat bold",11), bg="#5C4B90",width=14,height=1,fg="black",command=backlogin,
                cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black").place(x=565, y=492,width=105)
    
signup()

window.mainloop()


