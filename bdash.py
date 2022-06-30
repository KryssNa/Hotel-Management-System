

import datetime 
import sqlite3
import smtplib as s
from tkinter import *
import random
from tkinter import ttk
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
    CUSTOMER NAME : ZAIN ALI
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


id =ttk.Entry(root,textvariable=contact, font=("Arial", 12))
id.place(x=250, y=140)
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
save =Button(root, text="ADD",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=220, y=620,width=100)
search =Button(root, text="SEARCH",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1000, y=300,width=80)
delete =Button(root, text="DELETE",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=355, y=620,width=100)
bil=Button(root, text="BILL",command=day_check,font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=95, y=621,width=100)

showall =Button(root, text="REFRESH LIST",font=("Consolas", 13, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=1100, y=300,width=115)
fetch_data =Button(root, text="FETCH DATA",font=("Consolas", 11, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="black",activeforeground='black').place(x=450, y=140,width=100)
email=Button(root, text="Email Details",command=email_check,font=("Consolas", 10, "bold"), fg="black", bg="#FFA726", borderwidth=0,border=0,cursor="hand2",activebackground="#FFA726",activeforeground='#FFA726').place(x=520, y=305,width=110)

root.mainloop()