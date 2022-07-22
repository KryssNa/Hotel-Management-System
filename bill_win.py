
from logging import root
import sqlite3
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
import tkinter as tk
from PIL import ImageTk,Image

conn=sqlite3.connect('customer.db')
c=conn.cursor()
try:
    conn=sqlite3.connect("customer.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE bill(
        
        contact integer PRIMARY KEY,
        cust_name text,
        item text,
        rate integer,
        qty integer,
        price integer
        
        )""")
    conn.commit()
    conn.close()
    print("Table created successfully")
except:
    pass



def details():   
    menu_category = ["Tea & Coffee","Drinks","Fast Food","Nepali dishes","Starters","Main Course","Dessert"]

    menu_category_dict = {"Tea & Coffee":"Tea & Coffee.txt","Drinks":"Drinks.txt",
                    "Fast Food":"3 Fast Food.txt","Punjabi dishes":"4 Punjabi dishes.txt",
                    "Starters":"5 Starters.txt","Main Course":"6 Main Course.txt",
                    "Sweet Dishes":"7 Sweet Dishes.txt"}
    
    order_dict = {}
    for i in menu_category:
        order_dict[i] = {}

#====================Backend Functions===========================#      
        
##function to add item to menu
    def menu_window():
        root=Toplevel()
        root.geometry("300x200")
        root.config(background="#39065D")
        root.title("Menu")
        
        try:
            conn=sqlite3.connect("menu.db")
            c=conn.cursor()
            c.execute(""" CREATE TABLE menulist (
                
                item text,
                category text,
                rate 
                )""")
            conn.commit()
            conn.close()
            print("table created successfully")
        except:
            pass
        
        def add_item():
            try:
                conn=sqlite3.connect("menu.db")
                c=conn.cursor()
                c.execute("INSERT INTO menulist VALUES(:item,:category,:rate)",{
                    "item":entry_item.get(),
                    "category":cmenu.get(),
                    "rate":entry_rate.get()
                    })      
                conn.commit()
                load_menu()
                conn.close()
                msg=tmsg.showinfo("Success","Added successfully")
            except Exception as es:
                tmsg.showerror("Error", f"error due to:{str(es)}")
                
            
        ##combobox for category
        mCategory = StringVar()
        cmenu = ttk.Combobox(root,textvariable=mCategory)
        cmenu.set(value="Drinks")
        cmenu['value']=(menu_category)
        cmenu.place(x=98)

        
        ##entry and label for item
        label_item=Label(root,text="Item name",background="#39065D",fg="white",font=("Montserrat",9,"bold"))
        label_item.place(x=27,y=50)
        
        item=StringVar()
        entry_item=Entry(root,width=20,textvariable=item)
        entry_item.place(x=100,y=50)
        
        ##label and entry for rate
        label_rate=Label(root,text="Rate",background="#39065D",fg="white",font=("Montserrat",9,"bold"))
        label_rate.place(x=52,y=110)
        
        rate=StringVar()
        entry_rate=Entry(root,width=20,textvariable=rate)
        entry_rate.place(x=100,y=110)
        
        #button to add item 
        Button(root,text="Add",width=15,command=add_item,font=("Montserrat",9,"bold"),bg="#FFA726",fg="black",activebackground="#FFA726").place(x=100,y=170)
        root.mainloop()

    def mainpage():
        root7.destroy()
        import main
    
    def load_menu():
        conn=sqlite3.connect("menu.db")
        c=conn.cursor()
        c.execute("SELECT * FROM menulist")
        rows=c.fetchall()    

        if len(rows)!=2:
            menu_tabel.delete(*menu_tabel.get_children())
        for row in rows:
                menu_tabel.insert("",tk.END, values=row)        
        conn.close()
        conn.close()
        
        
    def load_order():
        order_tabel.delete(*order_tabel.get_children())
        for category in order_dict.keys():
            if order_dict[category]:
                for lis in order_dict[category].values():
                    order_tabel.insert('',END,values=lis)
        update_total_price()

    def add_button_operation():
        name = itemName.get()
        rate = itemRate.get()
        category = itemCategory.get()
        quantity = itemQuantity.get()

        if name in order_dict[category].keys():
            tmsg.showinfo("Error", "Item already exist in your order")
            return
        if not quantity.isdigit():
            tmsg.showinfo("Error", "Please Enter Valid Quantity")
            return
        lis = [name,rate,quantity,str(int(rate)*int(quantity)),category]
        order_dict[category][name] = lis
        load_order()
        
    def load_item_from_menu(event):
        cursor_row = menu_tabel.focus()
        contents = menu_tabel.item(cursor_row)
        row = contents["values"]
        itemName.set(row[0])
        itemRate.set(row[2])
        itemCategory.set(row[1])
        itemQuantity.set("1")

    def load_item_from_order():
        cursor_row = order_tabel.focus()
        contents = order_tabel.item(cursor_row)
        row = contents["values"]

        itemName.set(row[0])
        itemRate.set(row[1])
        itemQuantity.set(row[2])
        itemCategory.set(row[4])

    def show_button_operation():
        category = menuCategory.get()
        if category not in menu_category:
            tmsg.showinfo("Error", "Please select valid Choice")
        else:
            menu_tabel.delete(*menu_tabel.get_children())
            f = open("Menu\\" + menu_category_dict[category] , "r")
            while True:
                line = f.readline()
                if(line==""):
                    break
                if (line[0]=='#' or line=="\n"):
                    continue
                if(line[0]=='*'):
                    name = "\t"+line[:-1]
                    menu_tabel.insert('',END,values=[name,"",""])
                else:
                    name = line[:line.rfind(" ")]
                    price = line[line.rfind(" ")+1:-3]
                    menu_tabel.insert('',END,values=[name,price,category])

    def clear_button_operation():
        itemName.set("")
        itemRate.set("")
        itemQuantity.set("")
        itemCategory.set("")

    def cancel_button_operation():
        names = []
        for i in menu_category:
            names.extend(list(order_dict[i].keys()))
        if len(names)==0:
            tmsg.showinfo("Error", "Your order list is Empty")
            return
        ans = tmsg.askquestion("Cancel Order", "Are You Sure to Cancel Order?")
        if ans=="no":
            return
        order_tabel.delete(*order_tabel.get_children())
        for i in menu_category:
            order_dict[i] = {}
        clear_button_operation()
        update_total_price()

    def update_quantity():
        name = itemName.get()
        rate = itemRate.get()
        category = itemCategory.get()
        quantity = itemQuantity.get()

        if category=="":
            return
        if name not in order_dict[category].keys():
            tmsg.showinfo("Error", "Item is not in your order list")
            return
        if order_dict[category][name][2]==quantity:
            tmsg.showinfo("Error", "No changes in Quantity")
            return
        order_dict[category][name][2] = quantity
        order_dict[category][name][3] = str(int(rate)*int(quantity))
        load_order()

    def remove_button_operation():
        name = itemName.get()
        category = itemCategory.get()

        if category=="":
            return
        if name not in order_dict[category].keys():
            tmsg.showinfo("Error", "Item is not in your order list")
            return
        del order_dict[category][name]
        load_order()

    def update_total_price():
        price = 0
        for i in menu_category:
            for j in order_dict[i].keys():
                price += int(order_dict[i][j][3])
        if price == 0:
            totalPrice.set("")
        else:
            totalPrice.set("Rs. "+str(price)+"  /-")

    ##bill function
    def bill_button_operation():
        customer_name = customerName.get()
        customer_contact = customerContact.get()
        names = []
        for i in menu_category:
            names.extend(list(order_dict[i].keys()))
        if len(names)==0:
            tmsg.showinfo("Error", "Your order list is Empty")
            return
        if customer_name=="" or customer_contact=="":
            tmsg.showinfo("Error", "Customer Details Required")
            return
        if not customerContact.get().isdigit():
            tmsg.showinfo("Error", "Invalid Customer Contact")
            return   
        ans = tmsg.askquestion("Generate Bill", "Are You Sure to Generate Bill?")
        ans = "yes"
        if ans=="yes":
            bill = Toplevel(root7)
            bill.title("Bill")
            bill.geometry("820x450+300+100")
            bill_text_area = Text(bill, font=("Montserrat", 12))
            st = "\t\t\t HOTEL MANGEMENT SYSTEM\n\t\t\t Designed and Programmed by\n"
            st += "\t\t\t\tkryss na\n"
            st += "-"*61 + "BILL" + "-"*61 + "\nDate:- "

            #Date and time
            t = time.localtime(time.time())
            week_day_dict = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",
                                6:"Sunday"}
            st += f"{t.tm_mday} / {t.tm_mon} / {t.tm_year} ({week_day_dict[t.tm_wday]})"
            st += " "*10 + f"\t\t\t\t\t\tTime:- {t.tm_hour} : {t.tm_min} : {t.tm_sec}"

            #Customer Name & Contact
            st += f"\nCustomer Name:- {customer_name}\nCustomer Contact:- {customer_contact}\n"
            st += "-"*130 + "\n" + " "*4 + "DESCRIPTION\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n"
            st += "-"*130 + "\n"

            #List of Items
            for i in menu_category:
                for j in order_dict[i].keys():
                    lis = order_dict[i][j]
                    name = lis[0]
                    rate = lis[1]
                    quantity = lis[2]
                    price = lis[3]
                    st += name + "\t\t\t\t\t" + rate + "\t      " + quantity + "\t\t  " + price + "\n\n"
            st += "-"*130

            #Total Price
            st += f"\n\t\t\tTotal price : {totalPrice.get()}\n"
            st += "-"*130

            #display bill in new window
            bill_text_area.insert(1.0, st)

            #write into file
            folder = f"{t.tm_mday},{t.tm_mon},{t.tm_year}"
            if not os.path.exists(f"Bill Records\\{folder}"):
                os.makedirs(f"Bill Records\\{folder}")
            file = open(f"Bill Records\\{folder}\\{customer_name+customer_contact}.txt", "w")
            file.write(st)
            file.close()

            #Clear operaitons
            order_tabel.delete(*order_tabel.get_children())
            for i in menu_category:
                order_dict[i] = {}
            clear_button_operation()
            update_total_price()
            customerName.set("")
            customerContact.set("")

            bill_text_area.pack(expand=True, fill=BOTH)
            bill.focus_set()
            bill.protocol("WM_DELETE_WINDOW", close_window)

    
    
    def close_window():
        tmsg.showinfo("Thanks", "Thanks for using our service")
        root7.destroy()
        import login
    
    ##function to remove item  from  menu
    def remove_fromMenu():
        selected_item=menu_tabel.selection()[0]
        # print(selected_item)
        items=menu_tabel.item(selected_item)['values'][0]
        conn=sqlite3.connect('menu.db')
        c=conn.cursor()
        c.execute('DELETE FROM menulist WHERE item=?',(items,))
        conn.commit()
        conn.close()
        menu_tabel.delete(*menu_tabel.get_children())
        conn=sqlite3.connect('menu.db')
        c=conn.cursor()
        c.execute("SELECT * FROM menulist")
        data=c.fetchall()
        print(data)
        for i in data:
            menu_tabel.insert('',END,values=i)
       
        conn.commit()
        conn.close()


    
    #logout function
    def logout():
        y=tmsg.askyesno("LogOut","Are you sure you want to Log Out")
        if y==YES:
            root7.destroy()
            import login
        else:
            pass

    ##import customer dashboard
    def cust_dash():
        root7.destroy()
        import customer_dash

    ##import booking dashboard
    def book_dash():
        root7.destroy()
        import book_dash

    ##import billdash
    def bill_dash():
        tmsg.showinfo("Error","Already on Billing Dashboard")
        
    ##head to main window
    def main():
        root7.destroy()
        import main


    
    #==================Backend Code Ends===============

    root7=Tk()
    w, h = root7.winfo_screenwidth(), root7.winfo_screenheight()
    root7.geometry("%dx%d+0+0" % (w, h))
    root7.title("CUSTOMER BIILING SYSTEM")
    root7.configure(bg="#501F1F")

    ##image
    load=Image.open("trypp.png")
    load=load.resize((1535,800))
    render=ImageTk.PhotoImage(load)
    imgs=Label(root7,image=render)
    imgs.place(x=0,y=45)


    #================Title==============
    style_button = ttk.Style()
    style_button.configure("TButton",font = ("Montserrat",10,"bold"),
    background="#501F1F")

    title_frame = Frame(root7, bg="#501F1F", relief=GROOVE)
    title_frame.pack(side=TOP, fill="x")

    title_label = Label(root7, text="CUSTOMER  BILLING  DASHBOARD", 
                        font=("Montserrat SemiBold", 19, "bold"),bg = "#501F1F", fg="white")
    title_label.place(x=55,y=10)

    #main window button
    logout1=Button(root7,text="LOG OUT",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=logout).place(x=1450,y=6)
    custmor=Button(root7,text="CUSTOMERS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=cust_dash).place(x=1100,y=7)
    booking=Button(root7,text="Book Now",font=('Consolas',14,"bold"),bg="#A0522D",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=book_dash).place(x=820,y=6)
    con_btn=Button(root7,text="Contact & Help",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F").place(x=1250,y=6)
    foodIte=Button(root7,text="FOOD ITEMS",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=bill_dash).place(x=950,y=7)
    homebtn=Button(root7,text="Home ",font=('Consolas',14,"bold"),bg="#501F1F",border=0,fg="white",cursor="hand2",activebackground="#501F1F",activeforeground="#501F1F",command=main).place(x=700,y=6)

    
    #==============Customer=============
    customer_frame = LabelFrame(root7,text="Customer Details",font=("Montserrat", 14,),border=0,
                                bg="#501F1F",fg="white")
    customer_frame.place(x=0,y=95 ,width=680,height=100)

    customer_name_label = Label(customer_frame, text="Name", 
                        font=("Montserrat", 14),bg = "#501F1F", fg="white")
    customer_name_label.grid(row = 0, column = 0)

    customerName = StringVar()
    customerName.set("")
    customer_name_entry = Entry(customer_frame,width=20,font="Montserrat 12",
                                    textvariable=customerName)
    customer_name_entry.grid(row = 0, column=1,padx=30)

    customer_contact_label = Label(customer_frame, text="Contact", 
                        font=("Montserra", 15, "bold"),bg = "#501F1F", fg="white")
    customer_contact_label.grid(row = 0, column = 2)

    customerContact = StringVar()
    customerContact.set("")
    customer_contact_entry = Entry(customer_frame,width=20,font="Montserrat 12",bd=0,
                                    textvariable=customerContact)
    customer_contact_entry.grid(row = 0, column=3,padx=30)

    # fetch=Button(customer_frame,text="Fetch Data",font=("Montserrat",9,"bold"),bg="#FFA726",activebackground="#FFA726",
    #                         width=10)
    # fetch.grid(row=0,column=4)

    #===============Menu===============
    menu_frame = Frame(root7,bd=8, bg="#501F1F")
    menu_frame.place(x=0,y=160,height=560,width=680)

    menu_label = Label(menu_frame, text="Available Products", 
                        font=("Montserrat SemiBold", 15, "bold"),bg = "#501F1F", fg="white", pady=0)
    menu_label.pack(side=TOP,fill="x")

    menu_category_frame = Frame(menu_frame,bg="#501F1F",pady=10)
    menu_category_frame.pack(fill="x")

    combo_lable = Label(menu_category_frame,text="Menu List", 
                        font=("Montserrat", 12, "bold"),bg = "#501F1F", fg="white")
    combo_lable.grid(row=0,column=0,padx=10)

    menuCategory = StringVar()

    add_to_menu=Button(menu_category_frame,text="Add to Menu",font=("Montserrat",9,"bold"),width=10,bg="#FFA726",activebackground="#FFA726",command=menu_window)
    add_to_menu.grid(row=0,column=2,padx=30)
    remove_button =Button(menu_category_frame, text="Remove Item",font=("Montserrat",9,"bold"),width=10,bg="#FFA726",activebackground="#FFA726",command=remove_fromMenu)
    remove_button.grid(row=0,column=4,padx=40,pady=30)

    show_all_button =Button(menu_category_frame, text="Show All",font=("Montserrat",9,"bold"),bg="#FFA726",activebackground="#FFA726",
                            width=10,command=load_menu)
    show_all_button.grid(row=0,column=3)

    ############# Menu Tabel ##########################################
    menu_tabel_frame = Frame(menu_frame)
    menu_tabel_frame.pack(fill=BOTH,expand=1)

    scrollbar_menu_x = Scrollbar(menu_tabel_frame,orient=HORIZONTAL)
    scrollbar_menu_y = Scrollbar(menu_tabel_frame,orient=VERTICAL)

    style = ttk.Style()
    style.configure("Treeview.Heading",font=("Montserrat",10,))
    style.configure("Treeview",font=("Montserrat",8,),rowheight=25)

    menu_tabel = ttk.Treeview(menu_tabel_frame,style = "Treeview",
                columns =("name","category","price"),xscrollcommand=scrollbar_menu_x.set,
                yscrollcommand=scrollbar_menu_y.set)
    ##adding some bg color
    menu_tabel.tag_configure('oddrow', background="white")
    menu_tabel.tag_configure('evenrow', background="lightblue")
    
    menu_tabel.heading("name",text="Name")
    menu_tabel.heading("category",text="Category")
    menu_tabel.heading("price",text="price") 
    menu_tabel["displaycolumns"]=("name","category","price",)
    menu_tabel["show"] = "headings"
    menu_tabel.column("price",width=50,anchor='center')

    scrollbar_menu_x.pack(side=BOTTOM,fill=X)
    scrollbar_menu_y.pack(side=RIGHT,fill=Y)

    scrollbar_menu_x.configure(command=menu_tabel.xview)
    scrollbar_menu_y.configure(command=menu_tabel.yview)

    menu_tabel.pack(fill=BOTH,expand=1)  
    load_menu()
    menu_tabel.bind("<ButtonRelease-1>",load_item_from_menu)
    ###########################################################################################

    #===============Item Frame=============
    item_frame = Frame(root7, bg="#39065D")
    item_frame.place(x=680,y=170,height=230,width=680)

    item_title_label = Label(item_frame, text="Selected Product", 
                        font=("Montserrat Semibold", 15,),bg = "#39065D", fg="white")
    item_title_label.pack(side=TOP,fill="x")

    item_frame2 = Frame(item_frame, bg="#39065D")
    item_frame2.pack(fill=X)

    item_name_label = Label(item_frame2, text="Name",
                        font=("Montserrat", 12, "bold"),bg = "#39065D", fg="white")
    item_name_label.grid(row=0,column=0)

    itemCategory = StringVar()
    itemCategory.set("")

    itemName = StringVar()
    itemName.set("")
    item_name = Entry(item_frame2, font="arial 12",textvariable=itemName,state=DISABLED, width=25)
    item_name.grid(row=0,column=1,padx=10)

    item_rate_label = Label(item_frame2, text="Price", 
                        font=("arial", 12, "bold"),bg = "#39065D", fg="white")
    item_rate_label.grid(row=0,column=2,padx=40)

    itemRate = StringVar()
    itemRate.set("")
    item_rate = Entry(item_frame2, font="arial 12",textvariable=itemRate,state=DISABLED, width=10)
    item_rate.grid(row=0,column=3,padx=10)

    item_quantity_label = Label(item_frame2, text="Quantity", 
                        font=("Montserrat", 10, "bold"),bg = "#39065D", fg="white")
    item_quantity_label.grid(row=1,column=0,padx=30,pady=15)

    itemQuantity = StringVar()
    itemQuantity.set("")
    item_quantity = Entry(item_frame2, font="arial 12",textvariable=itemQuantity, width=10)
    item_quantity.grid(row=1,column=1)

    item_frame3 = Frame(item_frame, bg="#39065D")
    item_frame3.pack(fill=X)

    ##button to add item to menu
    add_button =Button(item_frame3, text="Add Item",bg="#FFA726",activebackground="#FFA726"
                        ,command=add_button_operation   )
    add_button.grid(row=0,column=0,padx=40,pady=30)
   
    remove_button =Button(item_frame3, text="Remove Item",bg="#FFA726",activebackground="#FFA726"
                        ,command=remove_button_operation  )
    remove_button.grid(row=0,column=1,padx=40,pady=30)

    update_button =Button(item_frame3, text="Update Quantity",bg="#FFA726",activebackground="#FFA726",
                        command=update_quantity)
    update_button.grid(row=0,column=2,padx=40,pady=30)

    clear_button =Button(item_frame3, text="Clear",bg="#FFA726",command=clear_button_operation,activebackground="#FFA726",
                            width=8)
    clear_button.grid(row=0,column=3,padx=40,pady=30)

    #==============Order Frame=====================
    order_frame = Frame(root7, bg="#39065D")
    order_frame.place(x=680,y=350,height=370,width=680)

    order_title_label = Label(order_frame, text="Your Products", 
                        font=("Montserrat", 15, "bold"),bg = "#39065D", fg="white")
    order_title_label.pack(side=TOP,fill="x")

    ############################## Order Tabel ###################################
    order_tabel_frame = Frame(order_frame)
    order_tabel_frame.place(x=0,y=40,height=260,width=680)

    scrollbar_order_x = Scrollbar(order_tabel_frame,orient=HORIZONTAL)
    scrollbar_order_y = Scrollbar(order_tabel_frame,orient=VERTICAL)

    order_tabel = ttk.Treeview(order_tabel_frame,
                columns =("name","rate","quantity","price","category"),xscrollcommand=scrollbar_order_x.set,
                yscrollcommand=scrollbar_order_y.set)
    order_tabel.tag_configure('oddrow', background="white")
    order_tabel.tag_configure('evenrow', background="lightblue")
    order_tabel.heading("name",text="Name")
    order_tabel.heading("rate",text="Rate")
    order_tabel.heading("quantity",text="Quantity")
    order_tabel.heading("price",text="Price")
    order_tabel["displaycolumns"]=("name", "rate","quantity","price")
    order_tabel["show"] = "headings"
    order_tabel.column("rate",width=100,anchor='center', stretch=NO)
    order_tabel.column("quantity",width=100,anchor='center', stretch=NO)
    order_tabel.column("price",width=100,anchor='center', stretch=NO)

    order_tabel.bind("<ButtonRelease-1>",load_item_from_order)

    scrollbar_order_x.pack(side=BOTTOM,fill=X)
    scrollbar_order_y.pack(side=RIGHT,fill=Y)

    scrollbar_order_x.configure(command=order_tabel.xview)
    scrollbar_order_y.configure(command=order_tabel.yview)

    order_tabel.pack(fill=BOTH,expand=1)

    ##label for total price
    total_price_label = Label(order_frame, text="Total Price", 
                        font=("Montserrat", 12, "bold"),bg = "#39065D", fg="white")
    total_price_label.pack(side=LEFT,anchor=SW,padx=20,pady=10)

    ##entry for total price
    totalPrice = StringVar()
    totalPrice.set("")
    total_price_entry = Entry(order_frame, font="arial 12",textvariable=totalPrice,state=DISABLED, 
                                width=10)
    total_price_entry.pack(side=LEFT,anchor=SW,padx=0,pady=10)

    ##bill button
    bill_button = Button(order_frame,font=("Montserrat",9,"bold"), command=bill_button_operation,text="Bill",width=10,bg="#FFA726",activebackground="#FFA726"
                        )
    bill_button.pack(side=LEFT,anchor=SW,padx=80,pady=10)

    ##cancel order button
    cancel_button =Button(order_frame, text="Cancel Order",font=("Montserrat",9,"bold"),command=cancel_button_operation,width=12,bg="#FFA726",fg="black",activebackground="#FFA726")
    cancel_button.pack(side=LEFT,anchor=SW,padx=20,pady=10)

    ##button to go back to mainpage
    # Button(root7,text="back",width=3,command=mainpage).place(x=0,y=2)

    root7.mainloop()
    
details()
