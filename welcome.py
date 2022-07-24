#import important module
from tkinter import *
from PIL import Image,ImageTk

#creating window
root=Tk()
root.title("Hotel Management System")#window title
root.geometry("1550x850")

#background image
image3=Image.open("image/Mainpage.jpg")
resized_image = image3.resize((1550,785))
photo1=ImageTk.PhotoImage(resized_image)
imglabel=Label(root,image=photo1)
imglabel.pack()

#destroy current window and import login
def login_page():
    root.destroy()
    import login

#destroy current window and import signup
def signup_page():
    root.destroy()
    import reg

#login button function
loginbtn=Button(root,text="LOGIN",font="comicsansms,9,bold",bg="white",width=10,background="#FFA726",activebackground="#FFA726",command=login_page)
loginbtn.place(x=1350,y=650)

#signin button function
signbtn=Button(root,text="SIGN UP",font="comicsansms,39,bold",bg="white",width=10,background="#FFA726",activebackground="#FFA726",command=signup_page)
signbtn.place(x=1350,y=720)

root.mainloop()