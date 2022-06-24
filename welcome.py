
from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.title("Hotel Management System")
root.geometry("1440x1024")

image3=Image.open("wel.png")
resized_image = image3.resize((1440,1024))
photo1=ImageTk.PhotoImage(resized_image)
imglabel=Label(root,image=photo1)
imglabel.pack()


htlname=Label(root,text="MOUNTAIN VIEW",font="comicsansms,39,bold",bg="white")
htlname.place(x=15,y=20)

htlname=Label(root,text="Welcome to our Hotel",font="comicsansms,9,bold",bg="white")
htlname.place(x=85,y=400)

# htlname=Label(root,text="MOUNTAIN VIEW",font="comicsansms,39,bold",bg="white")
# htlname.place(x=15,y=20)


root.mainloop()