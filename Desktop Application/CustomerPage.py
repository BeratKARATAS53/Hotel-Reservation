try:
    import tkinter as tk
    from tkinter import *
    import tkinter.messagebox as Messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import *
    import Tkinter.messagebox as Messagebox

try:
    import tkinter.ttk as ttk
except ImportError:
    import ttk

import mysql.connector as mysql


custRoot = tk.Tk()
custRoot.geometry("885x620+237+110")
custRoot.minsize(120, 1)
custRoot.maxsize(1370, 749)
custRoot.resizable(1, 1)
custRoot.configure(background='#EBEDEF')
custRoot.title("Customer Page")


def hotelPage():
    import HotelPage


def reservationPage():
    import ReservationPage


def statisticPage():
    import StatisticPage


def add():
    firstname = e_firstname.get()
    lastname = e_lastname.get()
    passwrd = e_password.get()
    confirm_passwrd = e_confirm_passwrd.get()
    email = e_email.get()
    address = e_address.get("1.0", END)
    telephone = e_telephone.get()
    age = e_age.get()
    money = e_money.get()
    username = e_username.get()

    if(firstname == "" or lastname == "" or passwrd == "" or email == "" or address == ""
            or telephone == "" or age == "" or username == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    elif(passwrd != confirm_passwrd):
        Messagebox.showinfo("Password Status", "Password Mismatch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addPerson('" + firstname + "','" + lastname + "','" + passwrd
                       + "','" + email + "','" + address + "','" + telephone + "'," + age + ","
                       + money + ",'" + username + "','" + "' '" + "','customer')")
        con.commit()
        con.close()
        
        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        cust_list()

        e_customer_id.delete(0, "end")
        e_firstname.delete(0, "end")
        e_lastname.delete(0, "end")
        e_password.delete(0, "end")
        e_confirm_passwrd.delete(0, "end")
        e_email.delete(0, "end")
        e_address.delete('1.0', END)
        e_telephone.delete(0, "end")
        e_money.delete(0, "end")
        e_age.delete(0, "end")
        e_username.delete(0, "end")



def update():
    customer_id = e_customer_id.get()
    firstname = e_firstname.get()
    lastname = e_lastname.get()
    passwrd = e_password.get()
    confirm_passwrd = e_confirm_passwrd.get()
    email = e_email.get()
    address = e_address.get("1.0", END)
    telephone = e_telephone.get()
    age = e_age.get()
    money = e_money.get()
    username = e_username.get()

    if(customer_id == "" or firstname == "" or lastname == "" or passwrd == "" or email == "" or address == ""
            or telephone == "" or age == "" or money == "" or username == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("select exists (select * from customer_all_info where id = " + customer_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
            e_customer_id.delete(0, "end")

        else:
            cursor.execute("Call updatePerson('" + customer_id + "','" + firstname + "','" + lastname + "','" + passwrd
                        + "','" + email + "','" + address + "','" + telephone + "'," + age + ","
                        + money + ",'" + username + "','" + "' '" + "','customer')")

            Messagebox.showinfo("Update Status", "Updated Succesfully")
            con.commit()
            cust_list()

            e_email.config(state="normal")

            e_customer_id.delete(0, "end")
            e_firstname.delete(0, "end")
            e_lastname.delete(0, "end")
            e_password.delete(0, "end")
            e_confirm_passwrd.delete(0, "end")
            e_email.delete(0, "end")
            e_address.delete('1.0', END)
            e_telephone.delete(0, "end")
            e_money.delete(0, "end")
            e_age.delete(0, "end")
            e_username.delete(0, "end")

            con.close()


def delete():
    customer_id = e_customer_id.get()
    if(customer_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("select exists (select * from customer_all_info where id = " + customer_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
            e_customer_id.delete(0, "end")
            
        else:
            cursor.execute("Call deletePerson(" + customer_id + ")")

            e_customer_id.delete(0, "end")
            e_firstname.delete(0, "end")
            e_lastname.delete(0, "end")
            e_password.delete(0, "end")
            e_confirm_passwrd.delete(0, "end")
            e_email.delete(0, "end")
            e_address.delete('1.0', END)
            e_telephone.delete(0, "end")
            e_money.delete(0, "end")
            e_age.delete(0, "end")
            e_username.delete(0, "end")

            Messagebox.showinfo("Delete Status", "Delete Succesfully")
            con.commit()
            cust_list()

        con.close()


def cust_list():
    records = customer_list.get_children()
    for element in records:
        customer_list.delete(element)

    con = mysql.connect(host="localhost", user="admin",
                        password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("select * from customer_all_info order by id asc")
    customer = cursor.fetchall()

    for cust in customer:
        customer_list.insert('', 0, text=cust[0], value=(
            cust[1], cust[2], cust[4], cust[6], cust[5], cust[9], cust[10], cust[12]))

    con.close()


def get():
    e_email.config(state="normal")

    e_firstname.delete(0, "end")
    e_lastname.delete(0, "end")
    e_password.delete(0, "end")
    e_confirm_passwrd.delete(0, "end")
    e_email.delete(0, "end")
    e_address.delete('1.0', END)
    e_telephone.delete(0, "end")
    e_money.delete(0, "end")
    e_age.delete(0, "end")
    e_username.delete(0, "end")

    customer_id = e_customer_id.get()
    if(customer_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("select exists (select * from customer_all_info where id = " + customer_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
            e_customer_id.delete(0, "end")

        else:
            cursor.execute(
                "select * from customer_all_info where id = " + customer_id + "")
            customer = cursor.fetchall()

            for cust in customer:
                e_firstname.insert(0, cust[1])
                e_lastname.insert(0, cust[2])
                e_password.insert(0, cust[3])
                e_confirm_passwrd.insert(0, cust[3])
                e_email.insert(0, cust[4])
                e_telephone.insert(0, cust[5])
                e_address.insert(INSERT, cust[6])
                e_username.insert(0, cust[9])
                e_age.insert(0, cust[10])
                e_money.insert(0, cust[12])

                e_email.config(state="disabled")

            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")

            con.close()


'''SIDE BAR'''
hotel = Button(custRoot, text="HOTEL", font=(
    "calibri", 10), bg="#FEF9E7", command=hotelPage)
hotel.place(relx=0.023, rely=0.067, height=24, width=127)

customer = Button(custRoot, text="CUSTOMER", font=(
    "calibri", 10), bg="#F1C40F")
customer.place(relx=0.023, rely=0.129, height=24, width=127)

reservation = Button(custRoot, text="RESERVATION", font=(
    "calibri", 10), bg="#FEF9E7", command=reservationPage)
reservation.place(relx=0.023, rely=0.194, height=24, width=127)

statistics = Button(custRoot, text="TABLE STATISTICS", font=(
    "calibri", 10), bg="#FEF9E7", command=statisticPage)
statistics.place(relx=0.023, rely=0.260, height=24, width=127)

TSeparator1 = ttk.Separator(custRoot)
TSeparator1.place(relx=0.194, rely=0.032, relheight=0.919)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(custRoot)
TSeparator2.place(relx=0.217, rely=0.435, relwidth=0.743)

'''INPUT TEXTS'''
customer_id = Label(custRoot, text="ID: ", font=("calibri", 9))
customer_id.place(relx=0.251, rely=0.065, height=21, width=24)

e_customer_id = Entry(custRoot)
e_customer_id.place(relx=0.286, rely=0.065, height=20, relwidth=0.039)

firstname = Label(custRoot, text="First Name: ", font=("calibri", 9))
firstname.place(relx=0.331, rely=0.065, height=21, width=69)

e_firstname = Entry(custRoot)
e_firstname.place(relx=0.423, rely=0.065, height=20, relwidth=0.199)

lastname = Label(custRoot, text="Last Name: ", font=("calibri", 9))
lastname.place(relx=0.629, rely=0.065, height=21, width=68)

e_lastname = Entry(custRoot)
e_lastname.place(relx=0.709, rely=0.065, height=20, relwidth=0.233)

passwrd = Label(custRoot, text="Password: ", font=("calibri", 9))
passwrd.place(relx=0.251, rely=0.21, height=19, width=60)

e_password = Entry(custRoot)
e_password.place(relx=0.697, rely=0.21, height=20, relwidth=0.245)

confirm_passwrd = Label(custRoot, text="Confirm Password: ", font=("calibri", 9))
confirm_passwrd.place(relx=0.571, rely=0.21, height=21, width=109)

e_confirm_passwrd = Entry(custRoot)
e_confirm_passwrd.place(relx=0.331, rely=0.21, height=20, relwidth=0.233)

email = Label(custRoot, text="Email: ", font=("calibri", 9))
email.place(relx=0.251, rely=0.113, height=21, width=41)

e_email = Entry(custRoot)
e_email.place(relx=0.331, rely=0.113, height=20, relwidth=0.279)

telephone = Label(custRoot, text="Phone: ", font=("calibri", 9))
telephone.place(relx=0.617, rely=0.113, height=21, width=46)

e_telephone = Entry(custRoot)
e_telephone.place(relx=0.686, rely=0.113, height=20, relwidth=0.256)

address = Label(custRoot, text="Address: ", font=("calibri", 9))
address.place(relx=0.251, rely=0.258, height=21, width=54)

e_address = Text(custRoot)
e_address.place(relx=0.331, rely=0.258, relheight=0.087, relwidth=0.61)

username = Label(custRoot, text="Username: ", font=("calibri", 9))
username.place(relx=0.251, rely=0.161, height=21, width=65)

e_username = Entry(custRoot)
e_username.place(relx=0.331, rely=0.161, height=20, relwidth=0.336)

age = Label(custRoot, text="Age: ", font=("calibri", 9))
age.place(relx=0.674, rely=0.161, height=21, width=33)

e_age = Entry(custRoot)
e_age.place(relx=0.72, rely=0.161, height=20, relwidth=0.039)

money = Label(custRoot, text="Money: ", font=("calibri", 9))
money.place(relx=0.777, rely=0.161, height=21, width=49)

e_money = Entry(custRoot)
e_money.place(relx=0.846, rely=0.161, height=20, relwidth=0.096)

'''OPERATION BUTTONS'''
add = Button(custRoot, text="Add", font=(
    "calibri", 10), bg="#7DCEA0", command=add)
add.place(relx=0.297, rely=0.371, height=24, width=97)

update = Button(custRoot, text="Update", font=(
    "calibri", 10), bg="#5DADE2", command=update)
update.place(relx=0.423, rely=0.371, height=24, width=99)

delete = Button(custRoot, text="Delete", font=(
    "calibri", 10), bg="#F1948A", command=delete)
delete.place(relx=0.549, rely=0.371, height=24, width=97)

get = Button(custRoot, text="Get Customer", font=(
    "calibri", 10), bg="#BB8FCE", command=get)
get.place(relx=0.674, rely=0.371, height=24, width=97)

refresh = Button(custRoot, text="Refresh Page", font=(
    "calibri", 10), bg="#b3ecff", command=cust_list)
refresh.place(relx=0.8, rely=0.371, height=24, width=96)

'''LIST OUTPUT'''
customer = Label(custRoot, text="Customer Table", font=("Comic Sans MC", 9))
customer.place(relx=0.537, rely=0.452, height=21, width=89)

customer_list = ttk.Treeview(custRoot, height=10, columns=5)
customer_list.grid(row=4, column=0)

customer_list.configure(columns="Col1 Col2 Col4 Col5 Col6 Col7 Col8 Col9")
customer_list.heading("#0", text='ID', anchor=N)
customer_list.column("#0", width='35', stretch=NO)
customer_list.heading("Col1", text='First Name', anchor=N)
customer_list.column("Col1", width='50')
customer_list.heading("Col2", text='Last Name', anchor=N)
customer_list.column("Col2", width='50')
customer_list.heading("Col4", text='Email', anchor=N)
customer_list.column("Col4", width='100')
customer_list.heading("Col5", text='Address', anchor=N)
customer_list.column("Col5", width='100')
customer_list.heading("Col6", text='Telephone', anchor=N)
customer_list.column("Col6", width='100', stretch=NO)
customer_list.heading("Col7", text='Username', anchor=N)
customer_list.column("Col7", width='100', stretch=NO)
customer_list.heading("Col8", text='Age', anchor=N)
customer_list.column("Col8", width='35', stretch=NO)
customer_list.heading("Col9", text='Money (₺)', anchor=N)
customer_list.column("Col9", width='65', stretch=NO)

customer_list.place(relx=0.217, rely=0.5, relheight=0.389, relwidth=0.721)
cust_list()

tk.mainloop()