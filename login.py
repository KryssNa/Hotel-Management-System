from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import random

#window title 
root=Tk()
root.title("Hotel Management System")
root.geometry("1440x1024")

#background image
image1=Image.open("67.png")
photo=ImageTk.PhotoImage(image1)
image_label=Label(image=photo)
image_label.pack()

##login page
def login():
    #signup page link
    def opensignup():
        root.destroy()
        import reg
    
    ##main window
    def openstatus():
        root.destroy()
        import main

        
      
    # #login frame
    myframe=Frame(root,height=350,width=300,bg="black",pady=20,padx=35)
    myframe.place(x=505,y=110)
    
    #authorization check
    def check():
        a=email_ent.get()
        b=password_ent.get()
        try:
            conn=sqlite3.connect('admins.db')
            c=conn.cursor()
            c.execute("SELECT * from users")
            records=c.fetchall()
            i=len(records)-1
            while i>=0:
                if records[i][2]!=a or records[i][4]!=b:
                    i=i-1
                    if i==-1:
                        messagebox.showerror("Login","Invalid Credentials")
                        break
                else:
                    #change user status to active after login and set other users as inactive
                    c.execute("""UPDATE users SET
                    status=:inactive
                    WHERE status=:active""",
                    {'inactive':False,
                    'active':True})
                    conn.commit()
                    
                    c.execute("""UPDATE users SET
                    status= :val
                    WHERE email = :a""",
                    {
                        'val':True,
                        'a':a
                               })
                    conn.commit()
                    messagebox.showinfo("Login","Logged in Successfully")
                    openstatus()
                    break           
            conn.commit()
            conn.close()
        except:
            messagebox.showerror("Login","Sign Up First")
  
    #Tkinter does not support placeholders for entry so following two functions removes the default inserted text once the focus is on the entry box
    def remove(event):
        a=email_ent.get()
        if a=='Enter Your Email':
            email_ent.delete(0, END) #removes text in entry box from 0 index to end

    def remove2(event):
        b=password_ent.get()  
        if b=='Enter Your Password': 
            password_ent.delete(0, END)  

    #label get started
    l_getstarted=Label(myframe,text="Get started",font=("Montserrat SemiBold", 15, "bold"),fg="white",bg="black")
    l_getstarted.place(x=50,y=0)

    #email label and entry
    l_email=Label(myframe,text="Email",fg="white",bg="black",font=("Montserrat light", 11, "bold"))
    l_email.place(x=10,y=40)
    email_ent=Entry(myframe,font=("Regular", 12,))
    email_ent.place(x=10,y=65,height=25,width=185)

    #password label and entry
    l_pass=Label(myframe,text="Password",fg="white",bg="black",font=("Montserrat light", 11, "bold"))
    l_pass.place(x=10,y=100)
    password_ent=Entry(myframe,font=("Regular", 12,))
    password_ent.place(x=10,y=125,height=25,width=185)
    password_ent.bind('<FocusIn>', remove2)
    showw=IntVar(value=1)
    
    def show():
        if (showw.get()==1): #checkbutton passes value 1 for true and 0 for false
            password_ent.config(show='') #config is used to access widget's attributes after its initialization
        else:
            password_ent.config(show='*')
    
    #show password checkbutton
    Checkbutton(myframe,text='Show', offvalue=0, variable=showw, bg='white', command=show).place(x=200, y=125)

    #login button
    Button(myframe,text="Login",bg="#F47F16",fg="black", cursor="hand2", borderwidth=0,width=9, activebackground="#F47F16",command=login,
            font=("Montserrat SemiBold", 11, "bold")).place(x=65,y=160)

    #forgot password and registration links
    New_Reg = Button(myframe, text="NEW REGISTRATION",font=("Montserrat SemiBold",9,), fg="white", bg="black", borderwidth=0,cursor="hand2",activebackground="black",command=opensignup)
    New_Reg.place(x=0, y=260)

    For_got = Button(myframe, text="RESET PASSWORD?", font=("Montserrat SemiBold",9,), fg="white", bg="black",activebackground="black",
                            borderwidth=0, cursor="hand2",command=reset)
    For_got.place(x=0, y=285)

    #verification check
    def verify():
        a=email_ent.get()
        b=password_ent.get()
        if (a=="" or a=="Enter Your Email") or (b=="" or b=="Enter Your Password"):
            messagebox.showerror("Login","One or More Fields Empty.")
        elif "@" and ".com" not in a:
            messagebox.showerror("Password Reset","Invalid Email")
        elif len(b)<6:
            messagebox.showerror("Password Reset","Password must be more than 6 characters")
        else:
            check()
    
    #login button
    Button(myframe,text="LOG IN",bg="#F47F16",fg="black", cursor="hand2", borderwidth=0,width=9, activebackground="#F47F16",command=verify,
            font=("Montserrat SemiBold", 11, "bold")).place(x=65,y=160)
    
#forgot password functionality
def reset():

    #creating a toplevel
    top=Toplevel()
    top.geometry('380x350')
    top.title('Forgot Password')

    Frame(top,bg='#b4cef3',height=400,width=400).place(x=0,y=0)
    Label(top, text='RESET PASSWORD', bg="#b4cef3", fg='white', font=('Arial',20,'bold')).place(x=50, y=20)

    #remove functionalities for placeholders
    def remove(event):
        a=email_ent.get()
        if a=='Enter Your Email':
            email_ent.delete(0, END)

    def remove2(event):
        b=new_ps_ent.get()
        if b=='New Password':
            new_ps_ent.delete(0, END)

    def remove3(event):
        c=new_psc_ent.get()
        if c=='Confirm New Password':
            new_psc_ent.delete(0, END)

    #show password functionalities for passwords
    def show():
        if (showw.get()==1):
            new_ps_ent.config(show='')
        else:
            new_ps_ent.config(show='*')

    def show2():
        if (showww.get()==1):
            new_psc_ent.config(show='')
        else:
            new_psc_ent.config(show='*')
    
    #USER INPUTS
    email_ent=Entry(top)
    email_ent.insert(0, 'Enter Your Email')
    email_ent.place(x=40, y=75,width=290, height=30)
    email_ent.bind('<FocusIn>', remove)

    #security questions
    ans1=StringVar()
    a="Q1: What is your favourite food?"
    b="Q2: What is the name of your first pet?"
    c="Q3: What is the name of your childhood best friend?"
    lst=[a,b,c]
    ques=random.choice(lst)
    num=int(ques[1])-1
    Label(top,text=ques,bg='#b4cef3').place(x=40,y=118)
    Entry(top,textvariable=ans1).place(x=40,y=140,width=290,height=30)

    #new password
    new_ps_ent=Entry(top)
    new_ps_ent.insert(0, 'New Password') #default text inserted in entry box, 0 is positional argument
    new_ps_ent.place(x=40, y=190,width=210, height=30)
    new_ps_ent.bind('<FocusIn>', remove2) #bind function is used to know the mouse movement (if it is clicked or hovering and so on)
    showw=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showw,bg='#b4cef3',command=show).place(x=260,y=193)

    new_psc_ent=Entry(top)
    new_psc_ent.insert(0, 'Confirm New Password') #default text inserted in entry box, 0 is positional argument
    new_psc_ent.place(x=40, y=230,width=210, height=30)
    new_psc_ent.bind('<FocusIn>', remove3) #bind function is used to know the mouse movement (if it is clicked or hovering and so on)
    showww=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showww,bg='#b4cef3',command=show2).place(x=260,y=233)

    Button(top,text="CONFIRM",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2',command=lambda:verify()).place(x=120, y=280)

    #update new password
    def update():
        a=email_ent.get()
        b=ans1.get()
        
        #database connection for password update
        conn=sqlite3.connect('admins.db')
        c=conn.cursor()
        c.execute("SELECT * from users")
        records=c.fetchall()
        i=len(records)-1
        while i>=0:
            if records[i][2]!=a or records[i][(6+num)]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Password Reset","Invalid Credentials")
                    break
            else:
                ps_upd=new_ps_ent.get()
                psc_upd=new_psc_ent.get()
                c.execute("""UPDATE users SET
                password= :new_ps,
                cpass= :new_psc
                WHERE email = :a""",
                {
                    'new_ps':ps_upd,
                    'new_psc':psc_upd,
                    'a':a
                })
                messagebox.showinfo("Password Reset","Password Changed Successfully")
                #destroy toplevel after successful password update
                top.destroy()
                break             
        conn.commit()
        conn.close()

    #password verification for forgot password functionality
    def verify():
        a=email_ent.get()
        b=ans1.get()
        c=new_ps_ent.get()
        d=new_psc_ent.get()

        if a=="" or a=="Enter Your Email" or b=="" or c=="" or c=="New Password" or d=="" or d=="Confirm New Password":
            messagebox.showerror("Password Reset","One or More Fields Empty")
        else:
            if "@" and ".com" not in a:
                messagebox.showerror("Password Reset","Invalid Email")
            elif len(c)<6 or len(d)<6:
                messagebox.showerror("Password Reset","Password must be more than 6 characters")
            elif c!=d:
                messagebox.showerror("Password Reset","Passwords Mismatch")
            else:
                update()
login()    
root.mainloop()