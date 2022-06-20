
from tkinter import*
from PIL import Image,ImageTk






win=Tk()
win.title("HotelManagementSystem")
win.geometry('1550x800+0+0')
    #  first image
img1=Image.open("hottu.jpg")
img1=img1.resize((1550,800),Image.ANTIALIAS)
win.photoimg1= ImageTk.PhotoImage(img1)

lblimg=Label(win,image=win.photoimg1,bd=4,)
lblimg.place(x=0,y=0,width=1550,height=140)

img2=Image.open("logo.jpg")
img2=img2.resize((230,140),Image.ANTIALIAS)
win.photoimg2= ImageTk.PhotoImage(img2)

lblimg=Label(win,image=win.photoimg2,bd=4,)
lblimg.place(x=0,y=0,width=230,height=140)

# title

lbl_title=Label(text="MOTEY THE ROYAL HOTEL",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4)
lbl_title.place(x=0,y=140,width=1550,height=50)
# ======main frame==========
main_frame=Frame(bd=4)
main_frame.place(x=0,y=190,width=1550,height=620)
# ======menu==========
lbl_title=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4)
lbl_title.place(x=0,y=0,width=230)

# ======btn frame==========
btn_frame=Frame(main_frame,bd=4,bg="pink")
btn_frame.place(x=0,y=50,width=230,height=500)

login_btn=Button(btn_frame,text="LOG IN",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
login_btn.grid(row=0,column=0,pady=1)


cust_btn=Button(btn_frame,text="CUSTOMER",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
cust_btn.grid(row=1,column=0,pady=1)

room_btn=Button(btn_frame,text="ROOM",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
room_btn.grid(row=2,column=0,pady=1)

details_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
details_btn.grid(row=3,column=0,pady=1)


report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
report_btn.grid(row=4,column=0,pady=1)

logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
logout_btn.grid(row=5,column=0,pady=1)

# ==========RIGHT SIDE IMAGE=====
img3=Image.open("67.png")
img3=img3.resize((1310,590),Image.ANTIALIAS)
win.photoimg3= ImageTk.PhotoImage(img3)

lblimg=Label(win,image=win.photoimg3,bd=4)
lblimg.place(x=240,y=200,width=1300,height=600)


# ======room image=============

img5=Image.open("room.jpg")
img5=img5.resize((230,210),Image.ANTIALIAS)
win.photoimg5= ImageTk.PhotoImage(img5)

lblimg=Label(win,image=win.photoimg5,bd=4)
lblimg.place(x=0,y=650,width=230,height=210)













win.mainloop()

