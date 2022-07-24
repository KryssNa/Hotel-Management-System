#import necessary modules
from tkinter import Tk
import datetime 
import sqlite3
import smtplib as s
from tkinter import *
import random
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import datetime
import time


#main window
root6=Tk()
root6.title("Hotel Mangement System")#window title
root6.geometry('1550x800+0+0')
root6.configure(bg="#501F1F")

#background logo
phot=Image.open("image/logo.png")
lod=phot.resize((300,220))
resize_im=ImageTk.PhotoImage(lod)
img=Label(root6,image=resize_im)
img.place(x=1220,y=50)


#creating database
try:
    ##creating table room with details
    conn=sqlite3.connect("customer.db")##connecting database
    c=conn.cursor()
    c.execute("""CREATE TABLE room(
       cust_id integer PRIMARY KEY,
       check_in text,
       check_out text,
       room_type text ,
       room_no integer,
       meal text,
       nofdays integer,
       contact integer ,
       total integer
        )""")
    conn.commit()
    conn.close()   
except:
    pass

#function to go back to main page
def mainpage():
    root6.destroy()
    import main

#function to add new customer
def add_data1():
    if  contact.get()=="":
        messagebox.showerror("Error","All field are required")
    else:
        try:
            ##insserting data into table room
            conn= sqlite3.connect("customer.db")#connecting database
            c=conn.cursor()
            # print("yes")
            c.execute("INSERT INTO room VALUES(:cus_id,:check_in,:check_out,:room_type,:room_no,:meal,:nofdays,:contact,:total)",{
                "cus_id":cust_id.get(),
                "check_in":check_in.get(),
                "check_out":check_out.get(),
                "room_type":room_type.get(),
                "room_no":room_no.get(),
                "meal":meal.get(),
                "nofdays":no_ofdays.get(),
                "contact":contact.get(),
                "total":total.get()
                                        })  
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Checked In Successfully!!")
        except Exception as es:
            messagebox.showerror("Error", f"error due to:{str(es)}")##messagebox to raise exception when error occurs

##function to fetch details of customer
def fetch():
    conn= sqlite3.connect("customer.db")
    c=conn.cursor()
    c.execute("SELECT * FROM room ")
    row_2=c.fetchall()
    if len(row_2)!=0:
        room_table.delete(*room_table.get_children())
        for i in row_2:
            room_table.insert("",END,values=i)
    conn.commit()
    conn.close()

##function to delete customer
def del_2():
    del_my=messagebox.askyesno("Hotel Mangement system","Do you want to delete this Entry!")
    if del_my==YES:
        conn= sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("DELETE FROM room WHERE cust_id="+cust_id.get())
        messagebox.showinfo("Success","Entry has been deleted!!")
    else:
        if not del_my:
            return
    conn.commit()
    # fetch_data3()
    conn.close()

##function to search in table
def search_my1():
    conn= sqlite3.connect("customer.db")
    c=conn.cursor()
    c.execute("SELECT * FROM room WHERE "+str(search_var.get())+ " LIKE '%" +str(search_txt.get())+"%'")
    row_2=c.fetchall()
    if len(row_2)!=0:
        room_table.delete(*room_table.get_children())
        for i in row_2:
            room_table.insert("",END,values=i)
    conn.commit()
    conn.close()
#================ fetch data ===============================================
def fetch_dataa():
    if cust_id.get()=="":
        messagebox.showerror("Error","Please Provide a valid Customer Id of the CUSTOMER!")
    else:
        conn= sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("SELECT name FROM customers WHERE cust_id="+cust_id.get())
        row4=c.fetchone()
        # print(row4)

        if row4==None:
            messagebox.showerror("Error","Please Enter a Valid Customer Id")
        else:
            ##fetching all details from customer database
            showdataframe=Frame(root6,bd=0,bg="#501F1F")
            showdataframe.place(x=600,y=150,height=150,width=500)
            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT name FROM customers WHERE cust_id="+cust_id.get())
            row4=c.fetchone()
            lbl1=Label(showdataframe,text="NAME: ",font=("Consolas,5,bold"),bg="#501F1F",fg="white")
            lbl1.place(x=120,y=0)
            lbl2=Label(showdataframe,text=row4,bg="#501F1F",fg="white",font=("Consolas,5,bold"))
            lbl2.place(x=190,y=0)

            #=============== Gender =====================================
            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT gender FROM customers WHERE cust_id="+cust_id.get())
            row4=c.fetchone()
            lblgender=Label(showdataframe,text="GENDER: ",bg="#501F1F",fg="white",font=("Consolas,8"))
            lblgender.place(x=93,y=30)
            lblgender=Label(showdataframe,text=row4,bg="#501F1F",fg="white",font=("Consolas,8"))
            lblgender.place(x=190,y=30)

            #================== Email ===========================================

            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT email FROM customers WHERE cust_id="+cust_id.get())
            row4=c.fetchone()
            lblgender=Label(showdataframe,text="EMAIL :",bg="#501F1F",fg="white",font=("Consolas,8"))
            lblgender.place(x=108,y=60)
            lblgender=Label(showdataframe,text=row4,bg="#501F1F",fg="white",font=("Consolas,8"))
            lblgender.place(x=190,y=60)

            #========== Nationality -==========================================
            conn= sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT nationality FROM customers WHERE cust_id="+cust_id.get())
            row4=c.fetchone()
            lblnat=Label(showdataframe,text="NATIONALITY :",font=("Consolas,4,bold"),bg="#501F1F",fg="white")
            lblnat.place(x=40,y=90)
            lblnat=Label(showdataframe,text=row4,bg="#501F1F",fg="white",font=("Consolas,5,bold"))
            lblnat.place(x=190,y=90)

            #fetching contact from database
            conn=sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT mobile FROM customers WHERE cust_id="+cust_id.get())
            data_cont=c.fetchone()
            for details in data_cont:
                txtcontact.delete(0,END)
                txtcontact.insert(END,details)

            
            #fetching room no. from database
            conn=sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT room_no FROM room WHERE cust_id="+cust_id.get())
            data_cont=c.fetchone()
            for details in data_cont:
                txtavailableroom.delete(0,END)
                txtavailableroom.insert(END,details)

            #fetching checkin date from database
            conn=sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT check_in FROM room WHERE cust_id="+cust_id.get())
            data_cont=c.fetchone()
            for details in data_cont:
                txtcheckin.delete(0,END)
                txtcheckin.insert(END,details)

            #fetch meal from database
            conn=sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT meal FROM room WHERE cust_id="+cust_id.get())
            data_cont=c.fetchone()
            for details in data_cont:
                txtmeal.delete(0,END)
                txtmeal.insert(END,details)

            #fetch room type from database
            conn=sqlite3.connect("customer.db")
            c=conn.cursor()
            c.execute("SELECT room_type FROM room WHERE cust_id="+cust_id.get())
            data_cont=c.fetchone()
            for details in data_cont:
                room_type.delete(0,END)
                room_type.insert(END,details)

            conn.commit()
            conn.close()
##function to calculate no of days
def days_check():
    tax.set(50)
    # bill.set(4)
    # bill=txttotal.get()
    inDate=check_in.get()
    outdate=check_out.get()
    inDate=datetime.datetime.strptime(inDate,"%d/%m/%Y")
    outdate=datetime.datetime.strptime(outdate,"%d/%m/%Y")
    no_ofdays.set(abs(outdate-inDate).days)
    
    ##calculating total price and tax
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
        total.set(TT)
    elif (meal.get()=="Breakfast" and room_type.get()=="High luxury"):
        print(meal.get())
        q1=float(5000)
        q2=float(10000)
        q3=float(5)
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.10))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.10)))
        tax.set(Tax)
        total.set(TT)
    elif (meal.get()=="Breakfast" and room_type.get()=="Normal"):
        print(meal.get())
        q1=float(5000)
        q2=float(4000)
        q3=float(5)
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.10))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.10)))
        tax.set(Tax)
        total.set(TT)
    else:
        checkout()

##To remove date type set in entry box
def remove(event):
    a=txtcheckin.get()
    b=txtcheckout.get()
    if a  == "DD/MM/YYYY":
        txtcheckin.delete(0,END)
        # txtcheckout.delete(0,END)
    elif b == "DD/MM/YYYY":
        txtcheckout.delete(0,END)
        
##verifying checkout
def verifycheckout():
    days_check()
    a=txtcheckout.get()
    b=txtcheckin.get()
    c=txtcontact.get()
    if c=="" or len(c)!=10:
        messagebox.showerror("CheckOut","Enter Valid Contact Number")
    elif b=="" or b=="DD/MM/YYYY":
        messagebox.showerror("CheckOut","Enter CheckIn Date First")
        
    elif a=="" or a=="DD/MM/YYYY":
        messagebox.showerror("CheckOut","Enter CheckOut Date First")   
             
    else:
        conn=sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute(" INSERT OR REPLACE INTO room values(:cus_id,:check_in,:check_out,:room_type,:room_no,:meal,:nofdays,:contact,:total)",{
            "cus_id":cust_id.get(),
            "check_in":check_in.get(),
            "check_out":check_out.get(),
            "room_type":room_type.get(),
            "room_no":room_no.get(),
            "meal":meal.get(),
            "nofdays":no_ofdays.get(),
            "contact":contact.get(),
            "total":total.get()
            })
        conn.commit()
        conn.close()
        
        
        checkout()
#checkout function
def checkout():
    x=messagebox.askyesno("CheckOut","Do You want to CheckOut?")
    if x==YES:
        a=messagebox.askyesno("Bill","Any Pending Bill?")
        if a==YES:
            root6.destroy()
            import bill_win
        else:
            root6.destroy()
            import login
    else:
        pass




#logout function
def logout():
    y=messagebox.askyesno("LogOut","Are you sure you want to Log Out")
    if y==YES:
        root6.destroy()
        import login
    else:
        pass

##import customer dashboard
def cust_dash():
    root6.destroy()
    import customer_dash

##import booking dashboard
def book_dash():
    messagebox.showinfo("Error","Already on Booking Dashboard")

##import billdash
def bill_dash():
    root6.destroy()
    import bill_win

##head to main window
def main():
    root6.destroy()
    import main

##reports and feedback function
def reports():
    root=Toplevel()
    root.title("Contact & Help")
    root.geometry('680x420')
    root.configure(bg="#39065D")

    try:
        conn=sqlite3.connect("customer.db")
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
                ##inserting reports in to database
                conn= sqlite3.connect("customer.db")
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
    ##report label
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
    ##entrybox for reports
    txtreport=Entry(root,textvariable=txt54,font=("Arial", 10))
    txtfield=Entry(root,font="Montserrat")
    txtfield.place(x=300,y=200,height=150,width=350)
    report_button =Button(root, text="SUBMIT  REPORT",command=add_data,font=("Montserrat bold",9,"bold"),width=18,bg="#FFA726",fg="black",activebackground="#FFA726",activeforeground="#FFA726",cursor="hand2")
    report_button.place(x=400,y=370)


#============== Frame ======================================================#        
frame=Frame(root6,bg="white")
frame.place(x=550,y=300,width=750,height=300)
scroll_x=Scrollbar(frame,orient=HORIZONTAL)
scroll_y=Scrollbar(frame,orient=VERTICAL)
room_table=ttk.Treeview(frame,column=("ref","kryss","Na","Nep","ktm","mas","vii","hiv"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=room_table.xview)
scroll_y.config(command=room_table.yview)

##table heading
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


##assigning stringVar to entrybox inorder to enter data
cust_id=StringVar()
x=random.randint(1,100)
cust_id.set(str(x))
check_in=StringVar()
check_out=StringVar()
room_type=StringVar()
room_no=StringVar()
meal=StringVar()
no_ofdays=StringVar()
tax=StringVar()
contact=StringVar()
total=StringVar()

## entry box 
txtcontact =ttk.Entry(root6,textvariable=contact, font=("Arial", 12))
txtcontact.place(x=250, y=185)
txtid =ttk.Entry(root6,textvariable=cust_id, font=("Arial",12))
txtid.place(x=250, y=140)
##checkin entry
txtcheckin=ttk.Entry(root6,textvariable=check_in, font=("Arial", 12))
txtcheckin.insert(0,"DD/MM/YYYY")
txtcheckin.place(x=250, y=230)
txtcheckin.bind('<FocusIn>',remove)
#checkout entry
txtcheckout=ttk.Entry(root6,textvariable=check_out, font=("Arial", 12))
txtcheckout.insert(0,"DD/MM/YYYY")
txtcheckout.place(x=250, y=280)
txtcheckout.bind('<FocusIn>',remove)
##combobox to select meal
txtmeal=ttk.Combobox(root6,textvariable=meal, state="readonly",font=("Arial", 12),width=18)
txtmeal["value"]=("Breakfast","Lunch","Dinner")
txtmeal.current(0)
txtmeal.place(x=250, y=575)
search_txt=StringVar()
txtsearch =ttk.Entry(root6,textvariable=search_txt,font=("Arial", 9))
txtsearch.place(x=820, y=260)
room_type =ttk.Combobox(root6, font=("Arial", 12),width=18,state='readonly')
room_type['value']=("Luxury","High Luxury","Normal")
room_type.current(0)
room_type.place(x=250, y=330)
search_var=StringVar()
search =ttk.Combobox(root6,textvariable=search_var, font=("Arial", 9),width=18,state='readonly')
search['value']=("cust_id")
search.current(0)
search.place(x=650, y=260)
txtnofdays=Entry(root6, textvariable=no_ofdays,font=("Arial", 12))
txtnofdays.place(x=250, y=380)
txttax=Entry(root6, textvariable=tax,font=("Arial", 12))
txttax.place(x=250, y=480)
txttotal=Entry(root6, textvariable=total,font=("Arial", 12))
txttotal.place(x=250, y=530)
txtavailableroom =ttk.Combobox(root6,textvariable=room_no, font=("Arial", 12),width=18,state="readonly")
txtavailableroom["value"]=("101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120")
txtavailableroom.current(0)
txtavailableroom.place(x=250, y=430)

##label name
no_label=Label(root6,text="CUSTOMER NUMBER:",font=('Consolas',13,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=90,y=180)
id_l =Label(root6,text="CUSTOMER ID:",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=130,y=140)
checkIn_l=Label(root6,text="CHECK IN DATE:",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=110,y=230)
checkout_l=Label(root6,text="CHECK OUT DATE:",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=105,y=280)
tax_l=Label(root6,text="PAID TAX:",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=150,y=480)
total_label=Label(root6,text="TOTAL AMOUNT:",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=120,y=530)
meal_l=Label(root6,text="MEAL",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=170,y=575)

roomtype_label=Label(root6,text="ROOM TYPE:",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=145,y=330)
noofdays_label =Label(root6,text="NO OF DAYS:",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=135,y=380)
avai_label=Label(root6,text="AVAILABLE ROOMS",font=('Consolas',12,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=92,y=430)
bkdash_label=Label(root6,text="BOOKING DASHBOARD",font=('Consolas',30,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=55,y=5)

##checkin and checkout button
btn_checkin  =Button(root6, text="Check IN",command=add_data1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=220, y=620,width=100)
search=Button(root6, text="SEARCH",command=search_my1,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1000, y=250,width=80)
delete=Button(root6, text="DELETE",command=del_2,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=355, y=620,width=100)
btn_checkout  =Button(root6, text="Check Out",command=verifycheckout,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=95, y=621,width=100)

##refresh and fetchall button
showall_btn =Button(root6, text="REFRESH LIST",command=fetch,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1100, y=250,width=115)
fetch_data =Button(root6, text="FETCH DATA",command=fetch_dataa,font=("Consolas", 11, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=450, y=140,width=100)

#main window button and their function
logout1=Button(root6,text="LOG OUT",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=logout).place(x=1450,y=6)
custmor=Button(root6,text="CUSTOMERS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=cust_dash).place(x=1100,y=7)
booking=Button(root6,text="Book Now",font=('Consolas',14,"bold"),bg="#A0522D",border=1,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=book_dash).place(x=820,y=6)
con_btn=Button(root6,text="Contact & Help",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=reports).place(x=1250,y=6)
foodIte=Button(root6,text="FOOD ITEMS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=bill_dash).place(x=950,y=7)
homebtn=Button(root6,text="Home ",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=main).place(x=700,y=6)

root6.mainloop()