
# from tkinter import *
# from PIL import Image,ImageTk


# root=Tk()
# root.title("Hotel Management System")
# root.geometry("1440x1024")

# image3=Image.open("wel.png")
# resized_image = image3.resize((1440,1024))
# photo1=ImageTk.PhotoImage(resized_image)
# imglabel=Label(root,image=photo1)
# imglabel.pack()


# htlname=Label(root,text="MOUNTAIN VIEW",font="comicsansms,39,bold",bg="white")
# htlname.place(x=15,y=20)

# htlname=Label(root,text="Welcome to our Hotel",font="comicsansms,9,bold",bg="white")
# htlname.place(x=85,y=400)

# # htlname=Label(root,text="MOUNTAIN VIEW",font="comicsansms,39,bold",bg="white")
# # htlname.place(x=15,y=20)


# root.mainloop()


# print("kryss")
# print("\\ kryss")
# print("krysssss")
# print("kryssmm")
# print("krysskk")

import os
from sqlite3 import Row

menu_category = ["Tea & Coffee","Drinks","Fast Food","Nepali dishes","Starters","Main Course","Dessert"]

menu_category_dict = {"Tea & Coffee":"Tea & Coffee.txt","Drinks":"Drinks.txt",
                "Fast Food":"3 Fast Food.txt","Punjabi dishes":"4 Punjabi dishes.txt",
                "Starters":"5 Starters.txt","Main Course":"6 Main Course.txt",
                "Sweet Dishes":"7 Sweet Dishes.txt"}

order_dict = {}
for i in menu_category:
    order_dict[i] = {}
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#====================Backend Functions===================

menu_file_list = os.listdir("Menu")
for file in menu_file_list:
    f = open("Menu\\" + file ,"r")
    category=" "
    while True:
        line = f.readline()
        if(line==""):
            # menu_tabel.insert('',END,values=["","",""])
            break
        # elif (line=="\n"):
        #     continue
        # elif(line[0]=='#'):
        #     category = line[1:-1]
        #     print(category)
        #     name = "\t\t"+line[1:-1]
        #     print(name)
        #     price = ""
        elif(line[0]=='*'):
            name = Row[1]
            print(name)
            price = ""
        else:
            name = line[:line.rfind(" ")]
            print(name)
            price = line[line.rfind(" ")+1:-3]
            print(price)Z