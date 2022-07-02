

import datetime 
import sqlite3
import smtplib as s
from tkinter import *
import random
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox



def day_check():
        # pass
        # global 
        # x=random.randint(1,100)
        # cust_id.set(str(x))
        tax.set(5)
        bill.set(4)
        inDate=check_in.get()
        outdate=check_out.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
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
    
def email_check():
    ob=s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    a=contact.get()
    b=cust_id.get()
    c=check_in.get()
    d=check_out.get()
    e=nofdays.get()
    f=room_no.get()
    g=room_type.get()

    ob.login("rana5542123@gmail.com","--------")
    subject="HOTEL MANGEMENT SYSTEM BY ZAIN ALI"
    body=f'''
    Dear CUSTOMER,
    Thank you for choosing our Hotel!
    You details are mentioned below:
    CUSTOMER NAME : kryss
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
    kryss
    '''
    message="Subject:{}\n\n{}".format(subject,body)
    ob.sendmail("krishna.kryss@gmail.com","220179@softwarica.edu.np",message)
    print('Yes')
    ob.quit()



##Booking Dashboard


root=Tk()

root.title("Hotel Mangement System")
root.geometry('1440x1024')
root.configure(bg="#39065D")

#for bg image

# load=Image.open("77.png")
# load=load.resize((1400,750),Image.ANTIALIAS)
# render=ImageTk.PhotoImage(load)
# img=Label(root,image=render)
# img.place(x=0,y=0)  
# load_1=Image.open("67.png")
# load_1=load_1.resize((255,220),Image.ANTIALIAS)
# render1=ImageTk.PhotoImage(load_1)
# img1=Label(root,image=render1)
# img1.place(x=225,y=0)  
# def logout():
#     root.destory
# x=random.randint(1,100)


try:
    #creating a customer table
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE customers(
        id integer PRIMARY KEY,
        number integer,
        CID text,
        COD text,
        room_type text,
        days text,
        available_room int,
        paid_tax integer,
        total integer,
        meal text
    )""" )
    conn.commit()
    conn.close()
except:
    pass


# #table function
def table():
    #setting all rooms to available
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number from room")
    avrooms=c.fetchall()
    for i in avrooms:
        c.execute("""UPDATE room SET
        Room_Status=:st""",{'st': 'Available'})
        conn.commit()
    conn.close()

    #updating rooms to occupied according to users
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number from customers")
    rnum=c.fetchall()
    for i in rnum:
        c.execute("""UPDATE room SET
        Room_Status=:st
        WHERE Room_Number=:rn""",{
            'st': 'Occupied',
            'rn': i[0]
        })
        conn.commit()
    conn.close()

    #creating a table
    table=Frame(root,height=580,width=950,bg='white')
    table.place(x=603,y=198)

    #connection with database
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT * from room")
    lst=c.fetchall()

    #table heading
    lst.insert(0,('S.No.','Room Number','Room Type','Status','Price'))

    #table
    total_rows =len(lst)
    total_columns=len(lst[1])
    for i in range(total_rows):
        #table heading
        if i==0:
            fontt=('Arial',16,'bold')
            jus=CENTER
            bgc='#9cc2e5'
        else:
            #table data
            fontt=('Arial',16)
            jus=LEFT
            state=(lst[i][3])
            if state=="Occupied":
                bgc='#f79b9b'
            else:
                bgc='#a8d08d'
        for j in range(total_columns):
            #setting colomn width
            if j==0:
                wid=7
            else:
                wid=16
            e=Entry(
                table,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            e.grid(row=i,column=j)
            e.insert(0,lst[i][j])
            e.config(state=DISABLED)
    conn.commit()
    conn.close()
    

#fetch data function
def fetch():
    a=cid.get()
    if a=="":
        messagebox.showerror("Fetch","Enter CustomerID")
    else:
        try:
            #database connection
            conn=sqlite3.connect('booking.db')
            c=conn.cursor()
            c.execute("SELECT * from customers where oid=:cid",{'cid':a})
            rec=c.fetchall()
            #inserting values into entry boxes
            cid.insert(0,rec[0][0])
            contct.insert(0,rec[0][1])
            checkin.insert(0,rec[0][2])
            checkout.insert(0,rec[0][3])
            meal.insert(0,rec[0][4])
            room_type.insert(0,rec[0][5])
            nofdays.insert(0,rec[0][6])
            availableroom.insert(0,rec[0][7])
            tax.insert(0,rec[0][8])
            total.insert(0,rec[0][9])
            conn.commit()
            conn.close()
            #update button status to normal
            update.config(state=NORMAL)
        except:
            messagebox.showerror("Fetch","Invalid CustomerID")

#submit function
def submit():
    #add values to database
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("INSERT INTO customers VALUES (:id, :number, :CID, :COD, :room_type,:days, :available_room, :paid_tax, :total ,:meal)",
        {
            "id":id,
            'number':contct.get(),
            'CID':checkin.get(),
            'COD':checkout.get(),
            'room_type':room_type.get(),
            'days':nofdays.get(),
            'available_room':availableroom.get(),
            'paid_tax':tax.get(),
            'total':total,
            "meal":meal.get()
        })
    conn.commit()

    #get customer id for just booked customer
    c.execute("SELECT oid from customers where id=:phn",{'phn':contct.get()})
    cid=c.fetchall()

    #display customer id
    messagebox.showinfo("Booking","Room Booked Successfully, CustomerID: {}")
    conn.commit()
    conn.close()

    #update table
    table()
    #reset entries
    # reset()

    try:
        #create bill for new customer
        conn=sqlite3.connect('booking.db')
        c=conn.cursor()
        c.execute("""CREATE TABLE bill(
            cid int,
            particular text,
            rate int,
            qty int,
            price int
        )""")
        conn.commit()
        conn.close()
    except:
        pass

    #get room number and number of days from customers table
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number,days from customers where oid=:cid",{'cid':cid[0][0]})
    room=c.fetchall()
    conn.commit()
    conn.close()

    #get price and room type from room table
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Price,Room_Type from room where Room_Number=:cid",{'cid':room[0][0]})
    price=c.fetchall()
    conn.commit()
    conn.close()
    days=room[0][1]
    rtype=price[0][1]
    prc=price[0][0]
    
    #inserting values to bill for room
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("INSERT INTO bill VALUES (:cid, :particular, :rate, :qty, :prc)",
    {
        'cid':cid[0][0],
        'particular':rtype,
        'rate':prc,
        'qty':days,
        'prc':prc*days
    })
    conn.commit()
    conn.close()

# #verification for customer update
# def verifyforupdate():
#     #getting all occupied rooms and adding to a list
#     conn=sqlite3.connect('booking.db')
#     c=conn.cursor()
#     c.execute("SELECT Room_Number from room WHERE Room_Status=:oc",{'oc':"Occupied"})
#     list1=c.fetchall()
#     y=[]
#     for i in list1:
#         y.append(i[0])
#     conn.commit()
#     conn.close()

#     #getting values to verify
#     a=fn.get()
#     b=ln.get()
#     c=gen.get()
#     d=dob.get()
#     e=mob.get()
#     f=eml.get()
#     g=add.get()
#     h=nat.get()
#     i=cod.get()
#     j=rno.get()

#     #verification
#     if a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i=="" or j=="":
#         messagebox.showerror("Booking","One or More Fields Empty!")
#     elif len(d)!=4:
#         messagebox.showerror("Booking","Invalid Date")
#     elif len(e)!=10:
#         messagebox.showerror("Booking","Invalid Phone Number")
#     elif "@" and ".com" not in f:
#         messagebox.showerror("Booking","Invalid Email")
#     elif j!="T1" and j!="T2" and j!="T3" and j!="C1" and j!="C2" and j!="R1" and j!="R2" and j!="R3" and j!="R4":
#         messagebox.showerror("Booking","Invalid Room Number")
#     elif d[0].isalpha() or d[1].isalpha() or d[2].isalpha() or d[3].isalpha():
#         messagebox.showerror("Booking","Invalid Date")
#     elif e[0].isalpha() or e[1].isalpha() or e[2].isalpha() or e[3].isalpha() or e[4].isalpha() or e[5].isalpha() or e[6].isalpha() or e[7].isalpha() or e[8].isalpha() or e[9].isalpha():
#         messagebox.showerror("Booking","Invalid Phone Number")
#     elif i[0].isalpha() or i[len(i)-1].isalpha() or len(i)>2:
#         messagebox.showerror("Booking","Invalid Number of Days")
#     else:
#         #occupied room verification 
#         if j in y:
#             conn=sqlite3.connect('booking.db')
#             c=conn.cursor()
#             c.execute("SELECT Room_Number from customers where mob=:phn",{'phn':e})
#             rn=c.fetchall()
#             conn.commit()
#             conn.close()
#             if j==rn[0][0]:
#                 update()
#             else:
#                 messagebox.showerror("Booking","Room Full")
#         else:
#             update()

# #update function           
# def update():
#     a=availableroom.get()
#     days=checkout.get()
    
#     conn=sqlite3.connect('booking.db')
#     c=conn.cursor()
#     c.execute("""UPDATE customers SET
#         fname=:a,
#         lname=:b,
#         gender=:d,
#         dob=:e,
#         mob=:f,
#         email=:g,
#         address=:h,
#         nationality=:i,
#         days=:k,
#         Room_Number=:l
#         WHERE oid=:cid""",{
#             'a':fn.get(),
#             'b':ln.get(),
#             'd':gen.get(),
#             'e':dob.get(),
#             'f':mob.get(),
#             'g':eml.get(),
#             'h':add.get(),
#             'i':nat.get(),
#             'k':cod.get(),
#             'l':rno.get(),
#             'cid':cid.get()
#         })
#     conn.commit()
#     conn.close()
#     reset()
#     table()

#     conn=sqlite3.connect('booking.db')
#     c=conn.cursor()
#     c.execute("SELECT Price, Room_Type from room WHERE Room_Number=:number",{'number':a})
#     price=c.fetchall()
#     conn.commit()
#     conn.close()
#     rtype=price[0][1]
#     prc=price[0][0]
#     summ=int(days)*int(prc)
#     print(summ)

#     conn=sqlite3.connect('booking.db')
#     c=conn.cursor()
#     c.execute("""UPDATE bill SET
#     particular=:newroom,
#     rate=:price,
#     qty=:days,
#     price=:money WHERE cid=:cid""",{'newroom':rtype,'price':prc,'days':days,'money':summ,'cid':cid.get()})
#     conn.commit()
#     conn.close()

#     messagebox.showinfo("Update","Data Updated Successfully")

#verification for submitting
def verifyforsubmit():
    conn=sqlite3.connect('booking.db')
    c=conn.cursor()
    c.execute("SELECT Room_Number from room WHERE Room_Status=:oc",{'oc':"Occupied"})
    list1=c.fetchall()
    y=[]
    for i in list1:
        y.append(i[0])
    conn.commit()
    conn.close()
    
    a=id.get()
    b=contact.get()
    c=checkin.get()
    d=checkout.get()
    e=meal.get()
    f=room_type.get()
    g=nofdays.get()
    h=availableroom.get()
    i=tax.get()
    j=total.get()
    if a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" :
        messagebox.showerror("Booking","One or More Fields Empty!")
    elif len(c)!=4 or len(d)!=4:
        messagebox.showerror("Booking","Invalid Date")
    elif len(b)!=10:
        messagebox.showerror("Booking","Invalid Phone Number")
    # elif "@" and ".com" not in f:
    #     messagebox.showerror("Booking","Invalid Email")
    # elif j!="T1" and j!="T2" and j!="T3" and j!="C1" and j!="C2" and j!="R1" and j!="R2" and j!="R3" and j!="R4":
    #     messagebox.showerror("Booking","Invalid Room Number")
    # elif j in y:
    #     messagebox.showerror("Booking","Room Full")
    elif d[0].isalpha() or d[1].isalpha() or d[2].isalpha() or d[3].isalpha():
        messagebox.showerror("Booking","Invalid Date")
    elif d[0].isalpha() or c[1].isalpha() or c[2].isalpha() or c[3].isalpha():
        messagebox.showerror("Booking","Invalid Date")
    elif g[0].isalpha() or g[len(i)-1].isalpha() or len(i)>2:
        messagebox.showerror("Booking","Invalid Number of Days")
    elif b[0].isalpha() or b[1].isalpha() or b[2].isalpha() or b[3].isalpha() or b[4].isalpha() or b[5].isalpha() or b[6].isalpha() or b[7].isalpha() or b[8].isalpha() or b[9].isalpha():
        messagebox.showerror("Booking","Invalid Phone Number")
    else:
        submit()



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
frame=Frame(root,bg="white")
frame.place(x=550,y=350,width=750,height=300)
scroll_x=Scrollbar(frame,orient=HORIZONTAL)
scroll_y=Scrollbar(frame,orient=VERTICAL)
room_table=ttk.Treeview(frame,column=("ref","zan","ali","pak","zun","mas","vii","hiv"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=room_table.xview)
scroll_y.config(command=room_table.yview)

room_table.heading("ref",text="CUSTOMER ID")
room_table.heading("zan",text="CHECK IN")
room_table.heading("ali",text="CHECK OUT")
room_table.heading("pak",text="ROOM TYPE")
room_table.heading("zun",text="ROOM NO.")
room_table.heading("mas",text="MEAL")
room_table.heading("vii",text="NO OF DAYS")
room_table.heading("hiv",text=" MOBILE")
room_table["show"]="headings"
room_table.pack(fill=BOTH,expand=1)
# fetch()


cid =ttk.Entry(root,textvariable=contact, font=("Arial", 12))
cid.place(x=250, y=140)
contct =ttk.Entry(root,textvariable=cust_id, font=("Arial",12))
contct.place(x=250, y=185)
checkin=ttk.Entry(root,textvariable=check_in, font=("Arial", 12))
checkin.place(x=250, y=230)
checkout=ttk.Entry(root,textvariable=check_out, font=("Arial", 12))
checkout.place(x=250, y=280)
meal=ttk.Combobox(root,textvariable=meal, state="readonly",font=("Arial", 12),width=18)
meal["value"]=("Breakfast","Lunch","Dinner")
meal.current(0)
meal.place(x=250, y=575)
search_=StringVar()
search =ttk.Entry(root,textvariable=search_,font=("Arial", 9))
search.place(x=820, y=305)
room_type =ttk.Combobox(root, font=("Arial", 12),width=18,state='readonly')
room_type['value']=("Luxury","High Luxury")
room_type.current(0)
room_type.place(x=250, y=330)
search_var=StringVar()
search =ttk.Combobox(root,textvariable=search_var, font=("Arial", 9),width=18,state='readonly')
search['value']=("cus_id")
search.current(0)
search.place(x=650, y=305)
nofdays=ttk.Entry(root, textvariable=nofdays,font=("Arial", 12))
nofdays.place(x=250, y=380)
tax=ttk.Entry(root, textvariable=tax,font=("Arial", 12))
tax.place(x=250, y=480)
total=ttk.Entry(root, textvariable=bill,font=("Arial", 12))
total.place(x=250, y=530)
availableroom =ttk.Combobox(root,textvariable=room_no, font=("Arial", 12),width=18,state="readonly")
availableroom["value"]=("101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120")
availableroom.current(0)
availableroom.place(x=250, y=430)
details=Label(root,text="CUSTOMER NUMBER:",font=('Consolas',13,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=90,y=140)
id=Label(root,text="CUSTOMER ID",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=130,y=180)
custmor=Label(root,text="CHECK IN DATE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=110,y=230)
room=Label(root,text="CHECK OUT DATE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=105,y=280)
tax1=Label(root,text="PAID TAX",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=150,y=480)
total=Label(root,text="TOTAL AMOUNT",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=120,y=530)
meallbl=Label(root,text="MEAL",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=170,y=575)
        
gender=Label(root,text="ROOM TYPE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=145,y=330)
email=Label(root,text="NO OF DAYS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=135,y=380)
national=Label(root,text="AVAILABLE ROOMS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=92,y=430)
bkdash=Label(root,text="BOOKING DASHBOARD",font=('Consolas',30,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=530,y=50)
save =Button(root, text="ADD",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black',command=verifyforsubmit).place(x=220, y=620,width=100)
search =Button(root, text="SEARCH",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1000, y=300,width=80)
delete =Button(root, text="DELETE",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=355, y=620,width=100)
bil=Button(root, text="BILL",command=day_check,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=95, y=621,width=100)

showall =Button(root, text="REFRESH LIST",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1100, y=300,width=115)
fetch_data =Button(root, text="FETCH DATA",font=("Consolas", 11, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=450, y=140,width=100)
email=Button(root, text="Email Details",command=email_check,font=("Consolas", 10, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="#FFA726",activeforeground='#FFA726').place(x=520, y=305,width=110)

root.mainloop()