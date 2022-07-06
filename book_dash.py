#===========================================================Booking +===========================================
from tkinter import Tk
import os
import datetime 
import sqlite3
import smtplib as s
from tkinter import *
import random
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import datetime
import time


root6=Tk()
root6.title("Hotel Mangement System")
root6.geometry('1550x800+0+0')
root6.configure(bg="#39065D")

conn=sqlite3.connect("cust.db")
c=conn.cursor()

try:
    conn=sqlite3.connect("cust.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE room(
       cust_id text PRIMARY KEY,
       check_in text,
       check_out text,
       room_type ,
       room_no text,
       meal text,
       nofdays text,
       contact text
        )""")
    conn.commit()
    conn.close()   
except:
    pass

def mainpage():
    root6.destroy()
    import main


def add_data1():
    if  contact.get()=="":
        messagebox.showerror("Error","All field are required")
    else:
        try:
            conn= sqlite3.connect("cust.db")
            c=conn.cursor()
            # print("yes")
            c.execute("INSERT INTO room values(:cus_id,:check_in,:check_out,:room_type,:room_no,:meal,:nofdays,:contact)",{
                "cus_id":cust_id.get(),
                "check_in":check_in.get(),
                "check_out":check_out.get(),
                "room_type":room_type.get(),
                "room_no":room_no.get(),
                "meal":meal.get(),
                "nofdays":nofdays.get(),
                "contact":contact.get(),
                                        })
            
            conn.commit()
            # fetch_data3()
            conn.close()
            messagebox.showinfo("Success","DATA IS INSERTED!!")
        except Exception as es:
            messagebox.showerror("Error", f"error due to:{str(es)}")

def fetch():
    conn= sqlite3.connect("cust.db")
    c=conn.cursor()
    c.execute("SELECT * FROM room ")
    row_2=c.fetchall()
    if len(row_2)!=0:
        room_table.delete(*room_table.get_children())
        for i in row_2:
            room_table.insert("",END,values=i)
        conn.commit()
    conn.close()

def del_2():
    del_my=messagebox.askyesno("Hotel Mangement system","Do you want to delete this Entry!")
    if del_my>0:
        conn= sqlite3.connect("cust.db")
        c=conn.cursor()
        c.execute("DELETE FROM room WHERE cust_id="+cust_id.get())
        messagebox.showinfo("Success","Entry has been deleted!!")
    else:
        if not del_my:
            return
    conn.commit()
    # fetch_data3()
    conn.close()

def search_my1():
    conn= sqlite3.connect("cust.db")
    c=conn.cursor()

    c.execute("SELECT * FROM room WHERE "+str(search_var.get())+ " LIKE '%" +str(search_txt.get())+"%'")
    row_2=c.fetchall()
    if len(row_2)!=0:
        room_table.delete(*room_table.get_children())
        for i in row_2:
            room_table.insert("",END,values=i)
    conn.commit()
    conn.close()
#============================= fetch data ===============================================
def fetch_dataa():
    if contact.get()=="":
        messagebox.showerror("Error","Please Provide a valid Mobile number of the CUSTOMER!")
    else:
        conn= sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("SELECT name FROM customers WHERE mobile="+contact.get())
        row4=c.fetchone()
        # print(row4)

        if row4==None:
            messagebox.showerror("Error","Please Enter a Valid Number")
        else:
            # conn.commit()
            # conn.close()
            
            showdataframe=Frame(root6,bd=0,bg="#39065D")
            showdataframe.place(x=600,y=150,height=150,width=500)
            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT name FROM customers WHERE mobile="+contact.get())
            row4=c.fetchone()
            lbl1=Label(showdataframe,text="NAME: ",font=("Consolas,5,bold"),bg="#39065D",fg="white")
            lbl1.place(x=120,y=0)
            lbl2=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,5,bold"))
            lbl2.place(x=190,y=0)

            #========================================= Gender =====================================
            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT gender FROM customers WHERE mobile="+contact.get())
            row4=c.fetchone()
            lblgender=Label(showdataframe,text="GENDER: ",bg="#39065D",fg="white",font=("Consolas,8"))
            lblgender.place(x=93,y=30)
            lblgender=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,8"))
            lblgender.place(x=190,y=30)

            #======================================= Email ===========================================

            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT email FROM customers WHERE mobile="+contact.get())
            row4=c.fetchone()
            lblgender=Label(showdataframe,text="EMAIL :",bg="#39065D",fg="white",font=("Consolas,8"))
            lblgender.place(x=108,y=60)
            lblgender=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,8"))
            lblgender.place(x=190,y=60)

            #=================================== Nationality -==========================================
            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT nationality FROM customers WHERE mobile="+contact.get())
            row4=c.fetchone()
            lblnat=Label(showdataframe,text="NATIONALITY :",font=("Consolas,4,bold"),bg="#39065D",fg="white")
            lblnat.place(x=40,y=90)
            lblnat=Label(showdataframe,text=row4,bg="#39065D",fg="white",font=("Consolas,5,bold"))
            lblnat.place(x=190,y=90)

            conn.commit()
            conn.close()

def days_check():
    # x=random.randint(1,100)
    # cust_id.set(str(x))
    tax.set(50)
    bill.set(4)
    inDate=check_in.get()
    outdate=check_out.get()
    inDate=datetime.datetime.strptime(inDate,"%d/%m/%Y")
    outdate=datetime.datetime.strptime(outdate,"%d/%m/%Y")
    nofdays.set(abs(outdate-inDate).days)
    
    if (meal.get()=="Breakfast" and room_type.get()=="Luxury"):
        print(meal.get())
        q1=float(5000)
        q2=float(7000)
        q3=float(5)
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.10))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.10)))
        tax.set(Tax)
        bill.set(TT)
    else:
        pass

def Emails():
    ob=s.SMTP("KRISHNA.KRYSS@gmail.com",587)
    ob.starttls()
    a=contact.get()
    b=cust_id.get()
    c=check_in.get()
    d=check_out.get()
    e=nofdays.get()
    f=room_no.get()
    g=room_type.get()

    ob.login("krishna.kryss@gmail.com","--------")
    subject="HOTEL MANGEMENT SYSTEM BY KRYSS"
    body=f'''
    Dear CUSTOMER,
    Thank you for choosing our Hotel!
    You details are mentioned below:
    CUSTOMER NAME : Kryss Na 
    CONTACT NUMBER: {a}
    CUSTOMER ID   : {b}
    CHECK IN DATE : {c}
    CHECK OUT ID  : {d}
    YOUR TOTAL STAY :{e} Days
    ALLOTTED ROOM : {f}
    ROOM TYPE     : {g}
    We're eagerly looking forward to your arrival at our hotel.
    Be assured of our best services during your stay here.
    Regards,
    Hotel Mangement System
    Designed and Programed by,
    Kryss Na
    '''
    message="Subject:{}\n\n{}".format(subject,body)
    ob.sendmail("krishna.kryss@gmail.com","220179@softwarica.edu.np",message)
    print('Yes')
    ob.quit()

cust_id=StringVar()
# x=random.randint(1,100)
# cust_id.set(str(x))
check_in=StringVar()
check_out=StringVar()
room_type=StringVar()
room_no=StringVar()
meal=StringVar()
nofdays=StringVar()
tax=StringVar()
contact=StringVar()
x=random.randint(1,100)
cust_id.set(str(x))
bill=StringVar()


#====================================================== Frame ======================================================#        
frame=Frame(root6,bg="white")
frame.place(x=550,y=350,width=750,height=300)
scroll_x=Scrollbar(frame,orient=HORIZONTAL)
scroll_y=Scrollbar(frame,orient=VERTICAL)
room_table=ttk.Treeview(frame,column=("ref","kryss","Na","Nep","ktm","mas","vii","hiv"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=room_table.xview)
scroll_y.config(command=room_table.yview)

room_table.heading("ref",text="CUSTOMER ID")
room_table.heading("kryss",text="CHECK IN")
room_table.heading("Na",text="CHECK OUT")
room_table.heading("Nep",text="ROOM TYPE")
room_table.heading("ktm",text="ROOM NO.")
room_table.heading("mas",text="MEAL")
room_table.heading("vii",text="NO OF DAYS")
room_table.heading("hiv",text=" MOBILE")
room_table["show"]="headings"
room_table.pack(fill=BOTH,expand=1)
fetch()


txtid =ttk.Entry(root6,textvariable=contact, font=("Arial", 12))
txtid.place(x=250, y=140)
txtcontct =ttk.Entry(root6,textvariable=cust_id, font=("Arial",12))
txtcontct.place(x=250, y=185)
txtcheckin=ttk.Entry(root6,textvariable=check_in, font=("Arial", 12))
txtcheckin.place(x=250, y=230)
txtcheckout=ttk.Entry(root6,textvariable=check_out, font=("Arial", 12))
txtcheckout.place(x=250, y=280)
txtmeal=ttk.Combobox(root6,textvariable=meal, state="readonly",font=("Arial", 12),width=18)
txtmeal["value"]=("Breakfast","Lunch","Dinner")
txtmeal.current(0)
txtmeal.place(x=250, y=575)
search_txt=StringVar()
txtsearch =ttk.Entry(root6,textvariable=search_txt,font=("Arial", 9))
txtsearch.place(x=820, y=305)
room_type =ttk.Combobox(root6, font=("Arial", 12),width=18,state='readonly')
room_type['value']=("Luxury","High Luxury")
room_type.current(0)
room_type.place(x=250, y=330)
search_var=StringVar()
search =ttk.Combobox(root6,textvariable=search_var, font=("Arial", 9),width=18,state='readonly')
search['value']=("cust_id")
search.current(0)
search.place(x=650, y=305)
txtnofdays=ttk.Entry(root6, textvariable=nofdays,font=("Arial", 12))
txtnofdays.place(x=250, y=380)
txttax=ttk.Entry(root6, textvariable=tax,font=("Arial", 12))
txttax.place(x=250, y=480)
txttotal=ttk.Entry(root6, textvariable=bill,font=("Arial", 12))
txttotal.place(x=250, y=530)
txtavailableroom =ttk.Combobox(root6,textvariable=room_no, font=("Arial", 12),width=18,state="readonly")
txtavailableroom["value"]=("101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120")
txtavailableroom.current(0)
txtavailableroom.place(x=250, y=430)

detai=Label(root6,text="CUSTOMER NUMBER:",font=('Consolas',13,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=90,y=140)
id_l =Label(root6,text="CUSTOMER ID",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=130,y=180)
custm=Label(root6,text="CHECK IN DATE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=110,y=230)
rooml=Label(root6,text="CHECK OUT DATE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=105,y=280)
tax_l=Label(root6,text="PAID TAX",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=150,y=480)
total=Label(root6,text="TOTAL AMOUNT",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=120,y=530)
meall=Label(root6,text="MEAL",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=170,y=575)

gender=Label(root6,text="ROOM TYPE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=145,y=330)
email =Label(root6,text="NO OF DAYS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=135,y=380)
nation=Label(root6,text="AVAILABLE ROOMS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=92,y=430)
bkdash=Label(root6,text="BOOKING DASHBOARD",font=('Consolas',30,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=530,y=50)

save  =Button(root6, text="ADD",command=add_data1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=220, y=620,width=100)
search=Button(root6, text="SEARCH",command=search_my1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1000, y=300,width=80)
delete=Button(root6, text="DELETE",command=del_2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=355, y=620,width=100)
Bill  =Button(root6, text="BILL",command=days_check,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=95, y=621,width=100)

showall =Button(root6, text="REFRESH LIST",command=fetch,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1100, y=300,width=115)
fetch_data =Button(root6, text="FETCH DATA",command=fetch_dataa,font=("Consolas", 11, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=450, y=140,width=100)
email=Button(root6, text="Email Details",command=Emails,font=("Consolas", 10, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="#FFA726",activeforeground='#FFA726').place(x=520, y=305,width=110)

Button(root6,text="back",width=3,command=mainpage).place(x=0,y=2)

root6.mainloop()

