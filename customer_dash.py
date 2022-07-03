
from ast import Lambda
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter.messagebox as tmsg
import sqlite3

from PIL import Image, ImageTk
from time import strptime
from datetime import datetime
import sqlite3

try:
    conn=sqlite3.connect("customer.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE customers (
        cust_id int PRIMARY KEY,
        name text,
        mobile int,
        gender text,
        email text,
        nationality text
        ) """)
    conn.commit()
    conn.close()
except:
    pass

def cust_win():
    root5=Tk()
    root5.title("CUSTOMER Dashboard")
    root5.geometry('1550x800+0+0')
    root5.configure(bg="#39065D")
    # bg = PhotoImage(file="77.png")
    # lbl_2= Label(root5, image=bg)
    # lbl_2.place(x=0, y=0)  
    txtid=StringVar()
    x=random.randint(1,100)
    txtid.set(str(x))

    def add_data2():
        if  txtname.get()=="" or txtid.get()=="":
            messagebox.showerror("Error","All field are required")
        else:
            try:
                conn= sqlite3.connect("customer.db")
                c=conn.cursor()
                # print("yes")
                c.execute("INSERT INTO customers values(:cust_id,:name,:mobile,:gender,:email,:nationality)",
                          {"cust_id":txtid.get(),
                           "name":txtname.get(),
                           "mobile":txtphone.get(),
                           "gender":txtgender.get(),
                           "email":txtemail.get(),
                           "nationality":txtnationality.get()
                           })
            
                conn.commit()
                fetch_data2()
                conn.close()
                messagebox.showinfo("Success","CUSTOMER is Addded!!")
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}")
                
    def verify():
        a=txtid.get()
        b=txtname.get()
        c=txtphone.get()
        d=txtgender.get()
        e=txtemail.get()
        f=txtnationality.get()

        if (a=="" or a=="First Name") or (b=="" or b=="Last Name") or (c=="") or (d=="") or (e=="") or (f==""):
            messagebox.showerror("Signup","One or More Fields Empty.")
        elif "@" and ".com" not in e:
            messagebox.showerror("Signup","Invalid Email")
        elif len(c)!=10:
            messagebox.showerror("Signup","Invalid Phone Number Length")
        else:
            add_data2()


                
    def fetch_data2():

        conn= sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("select * from customers")
        row_2=c.fetchall()
        if len(row_2)!=0:
            details_1.delete(*details_1.get_children())
            for i in row_2:
                details_1.insert("",END,values=i)
            conn.commit()
        conn.close()

    def del_1():
        del_my=messagebox.askyesno("Hotel Mangement system","Do you want to delete this Entry!")
        if del_my>0:
            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            # query="DELETE FROM customers WHERE cust_id=%s"
            # value=(txtid.get())
            c.execute("DELETE FROM customers WHERE cust_id="+txtid.get())
        else:
            if not del_my:
                return
        conn.commit()
        fetch_data2()
        conn.close()

    def search_my2():
        conn= sqlite3.connect("customer.db")
        c=conn.cursor()

        c.execute("SELECT * FROM customers WHERE "+str(search_var.get())+ " LIKE '%" +str(search_txt.get())+"%'")
        row_2=c.fetchall()
        if len(row_2)!=0:
            details_1.delete(*details_1.get_children())
            for i in row_2:
                details_1.insert("",END,values=i)
        conn.commit()
        conn.close()

    def logout():
        y=messagebox.askyesno("Sure","Are you Sure want to Logout")
        if y=='yes':
        #set user status to inactive
            conn=sqlite3.connect('customer.db')
            c=conn.cursor()
            c.execute("""UPDATE customers SET
            status= :off
            WHERE status= :on""",
            {
                'off':False,
                'on':True
            })
            conn.commit()
            conn.close()

            try:
            #destroy window and import logout
                root5.destroy()
                import login
            except:
                pass
                messagebox.showinfo("Thank you","Thank you for using this application")
                root5.destroy()
            else:
                pass

    txtname=StringVar()
    txtgender=StringVar()
    txtphone=StringVar()
    txtnationality=StringVar()
    txtemail=StringVar()

    
#====================================================== Frame ======================================================#        
    frame=Frame(root5,bg="white")
    frame.place(x=550,y=200,width=750,height=360)
    scroll_x=Scrollbar(frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(frame,orient=VERTICAL)
    details_1=ttk.Treeview(frame,column=("ref","kryss","Na","Nep","ktm","mas"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=details_1.xview)
    scroll_y.config(command=details_1.yview)

    details_1.heading("ref",text="CUSTOMER ID")
    details_1.heading("kryss",text="NAME")
    details_1.heading("Na",text="MOBILE NO.")
    details_1.heading("Nep",text="GENDER")
    details_1.heading("ktm",text="EMAIL")
    details_1.heading("mas",text="NATIONALITY")
    details_1["show"]="headings"
    details_1.pack(fill=BOTH,expand=1)
    fetch_data2()


    txtid =ttk.Entry(root5, font=("Arial", 12))
    txtid.place(x=250, y=180)
    txtname =ttk.Entry(root5, font=("Arial", 12))
    txtname.place(x=250, y=230)
    txtphone =ttk.Entry(root5, font=("Arial", 12))
    txtphone.place(x=250, y=280)
    search_txt=StringVar()
    txtsearch =ttk.Entry(root5,textvariable=search_txt,font=("Arial", 9))
    txtsearch.place(x=820, y=160)
    txtgender =ttk.Combobox(root5, font=("Arial", 12),width=18,state='readonly')
    txtgender['value']=("Male","Female","Other")
    txtgender.current(0)
    txtgender.place(x=250, y=330)
    search_var=StringVar()
    search =ttk.Combobox(root5,textvariable=search_var, font=("Arial", 9),width=18,state='readonly')
    search['value']=("MOBILE","Customer ID")
    search.current(0)
    search.place(x=650, y=160)
    txtemail=ttk.Entry(root5, font=("Arial", 12))
    txtemail.place(x=250, y=380)
    txtnationality =ttk.Combobox(root5, font=("Arial", 12),width=18,state="readonly")
    txtnationality["value"]=("Nepali","Indian","US","Others")
    txtnationality.current(0)
    txtnationality.place(x=250, y=430)
    details=Label(root5,text="CUSTOMER DETAILS:",font=('Consolas',13,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=100,y=130)
    id=Label(root5,text="CUSTOMER ID",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=120,y=180)
    custmor=Label(root5,text="NAME",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=180,y=230)
    room=Label(root5,text="MOBILE NO",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=130,y=280)
    gender=Label(root5,text="GENDER",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=155,y=330)
    email=Label(root5,text="EMAIL",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=165,y=380)
    national=Label(root5,text="NATIONALITY",font=('Consolas',13,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=110,y=430)
    dashboard=Label(root5,text="CUSTOMER DASHBOARD",font=('Consolas',28,"bold"),bg="#39065D",border=0,fg="white",activebackground="#39065D",activeforeground="#39065D").place(x=535,y=50)
    save =Button(root5, text="ADD",command=verify,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=220, y=500,width=100)
    search =Button(root5, text="SEARCH",command=search_my2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1000, y=155,width=80)
    delete =Button(root5, text="DELETE",command=del_1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=355, y=500,width=100)
    showall =Button(root5, text="REFRESH LIST",command=fetch_data2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1100, y=155,width=115)
    root5.mainloop()
    
cust_win()