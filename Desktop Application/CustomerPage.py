import tkinter as tk
from tkinter import *
import tkinter.ttk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql


def add():
    firstname = c_firstname.get()
    lastname = c_lastname.get()
    passwrd = c_password.get()
    confirm_passwrd = c_confirm_passwrd.get()
    email = c_email.get()
    address = c_address.get("1.0", END)
    telephone = c_telephone.get()
    age = c_age.get()
    money = c_money.get()
    username = c_username.get()

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

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        cust_list()

        c_customer_id.delete(0, "end")
        c_firstname.delete(0, "end")
        c_lastname.delete(0, "end")
        c_password.delete(0, "end")
        c_confirm_passwrd.delete(0, "end")
        c_email.delete(0, "end")
        c_address.delete('1.0', END)
        c_telephone.delete(0, "end")
        c_money.delete(0, "end")
        c_age.delete(0, "end")
        c_username.delete(0, "end")

        con.close()


def update():
    customer_id = c_customer_id.get()
    firstname = c_firstname.get()
    lastname = c_lastname.get()
    passwrd = c_password.get()
    confirm_passwrd = c_confirm_passwrd.get()
    email = c_email.get()
    address = c_address.get("1.0", END)
    telephone = c_telephone.get()
    age = c_age.get()
    money = c_money.get()
    username = c_username.get()

    if(customer_id == "" or firstname == "" or lastname == "" or passwrd == "" or email == "" or address == ""
            or telephone == "" or age == "" or money == "" or username == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call updatePerson('" + customer_id + "','" + firstname + "','" + lastname + "','" + passwrd
                       + "','" + email + "','" + address + "','" + telephone + "'," + age + ","
                       + money + ",'" + username + "','" + "' '" + "','customer')")

        Messagebox.showinfo("Update Status", "Updated Succesfully")
        con.commit()
        cust_list()

        c_email.config(state="normal")

        c_customer_id.delete(0, "end")
        c_firstname.delete(0, "end")
        c_lastname.delete(0, "end")
        c_password.delete(0, "end")
        c_confirm_passwrd.delete(0, "end")
        c_email.delete(0, "end")
        c_address.delete('1.0', END)
        c_telephone.delete(0, "end")
        c_money.delete(0, "end")
        c_age.delete(0, "end")
        c_username.delete(0, "end")

        con.close()


def delete():
    customer_id = c_customer_id.get()
    if(customer_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call deletePerson(" + customer_id + ")")

        c_customer_id.delete(0, "end")
        c_firstname.delete(0, "end")
        c_lastname.delete(0, "end")
        c_password.delete(0, "end")
        c_confirm_passwrd.delete(0, "end")
        c_email.delete(0, "end")
        c_address.delete('1.0', END)
        c_telephone.delete(0, "end")
        c_money.delete(0, "end")
        c_age.delete(0, "end")
        c_username.delete(0, "end")

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
            cust[1], cust[2], cust[3], cust[4], cust[5], cust[6], cust[9], cust[10], cust[12]))

    con.close()


def get():
    c_firstname.delete(0, "end")
    c_lastname.delete(0, "end")
    c_password.delete(0, "end")
    c_confirm_passwrd.delete(0, "end")
    c_email.delete(0, "end")
    c_address.delete('1.0', END)
    c_telephone.delete(0, "end")
    c_money.delete(0, "end")
    c_age.delete(0, "end")
    c_username.delete(0, "end")

    customer_id = c_customer_id.get()
    if(customer_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select * from customer_all_info where id = " + customer_id + "")
        customer = cursor.fetchall()

        for cust in customer:
            c_firstname.insert(0, cust[1])
            c_lastname.insert(0, cust[2])
            c_password.insert(0, cust[3])
            c_confirm_passwrd.insert(0, cust[3])
            c_email.insert(0, cust[4])
            c_telephone.insert(0, cust[5])
            c_address.insert(INSERT, cust[6])
            c_username.insert(0, cust[9])
            c_age.insert(0, cust[10])
            c_money.insert(0, cust[12])

            c_email.config(state="disabled")

        Messagebox.showinfo("Fetch Status", "Fetch Succesfully")

        con.close()


root = tk.Tk()
root.geometry("875x620+237+110")
root.title("Main Page")

'''SIDE BAR'''
hotel = Button(root, text="HOTEL", font=(
    "bold", 10), bg="#d9d9d9")
hotel.place(relx=0.023, rely=0.067, height=24, width=127)

customer = Button(root, text="CUSTOMER", font=(
    "bold", 10), bg="#80ff00")
customer.place(relx=0.023, rely=0.129, height=24, width=127)

reservation = Button(root, text="RESERVATION", font=(
    "bold", 10), bg="#d9d9d9")
reservation.place(relx=0.023, rely=0.194, height=24, width=127)

TSeparator1 = tkinter.ttk.Separator()
TSeparator1.place(relx=0.194, rely=0.032, relheight=0.919)
TSeparator1.configure(orient="vertical")

TSeparator2 = tkinter.ttk.Separator()
TSeparator2.place(relx=0.217, rely=0.435, relwidth=0.743)

'''INPUT TEXTS'''
customer_id = Label(root, text="ID: ", font=("bold", 9))
customer_id.place(relx=0.251, rely=0.065, height=21, width=24)

c_customer_id = Entry()
c_customer_id.place(relx=0.286, rely=0.065, height=20, relwidth=0.039)

firstname = Label(root, text="First Name: ", font=("bold", 9))
firstname.place(relx=0.331, rely=0.065, height=21, width=69)

c_firstname = Entry()
c_firstname.place(relx=0.423, rely=0.065, height=20, relwidth=0.199)

lastname = Label(root, text="Last Name: ", font=("bold", 9))
lastname.place(relx=0.629, rely=0.065, height=21, width=68)

c_lastname = Entry()
c_lastname.place(relx=0.709, rely=0.065, height=20, relwidth=0.233)

passwrd = Label(root, text="Password: ", font=("bold", 9))
passwrd.place(relx=0.251, rely=0.21, height=19, width=60)

c_password = Entry()
c_password.place(relx=0.697, rely=0.21, height=20, relwidth=0.245)

confirm_passwrd = Label(root, text="Confirm Password: ", font=("bold", 9))
confirm_passwrd.place(relx=0.571, rely=0.21, height=21, width=109)

c_confirm_passwrd = Entry()
c_confirm_passwrd.place(relx=0.331, rely=0.21, height=20, relwidth=0.233)

email = Label(root, text="Email: ", font=("bold", 9))
email.place(relx=0.251, rely=0.113, height=21, width=41)

c_email = Entry()
c_email.place(relx=0.331, rely=0.113, height=20, relwidth=0.279)

telephone = Label(root, text="Phone: ", font=("bold", 9))
telephone.place(relx=0.617, rely=0.113, height=21, width=46)

c_telephone = Entry()
c_telephone.place(relx=0.686, rely=0.113, height=20, relwidth=0.256)

address = Label(root, text="Address: ", font=("bold", 9))
address.place(relx=0.251, rely=0.258, height=21, width=54)

c_address = Text()
c_address.place(relx=0.331, rely=0.258, relheight=0.087, relwidth=0.61)

username = Label(root, text="Username: ", font=("bold", 9))
username.place(relx=0.251, rely=0.161, height=21, width=65)

c_username = Entry()
c_username.place(relx=0.331, rely=0.161, height=20, relwidth=0.336)

age = Label(root, text="Age: ", font=("bold", 9))
age.place(relx=0.674, rely=0.161, height=21, width=33)

c_age = Entry()
c_age.place(relx=0.72, rely=0.161, height=20, relwidth=0.039)

money = Label(root, text="Money: ", font=("bold", 9))
money.place(relx=0.777, rely=0.161, height=21, width=49)

c_money = Entry()
c_money.place(relx=0.846, rely=0.161, height=20, relwidth=0.096)

'''OPERATION BUTTONS'''
add = Button(root, text="Add", font=(
    "italic", 10), bg="#d9d9d9", command=add)
add.place(relx=0.297, rely=0.371, height=24, width=97)

update = Button(root, text="Update", font=(
    "italic", 10), bg="#d9d9d9", command=update)
update.place(relx=0.423, rely=0.371, height=24, width=99)

delete = Button(root, text="Delete", font=(
    "italic", 10), bg="#d9d9d9", command=delete)
delete.place(relx=0.549, rely=0.371, height=24, width=97)

get = Button(root, text="Get Customer", font=(
    "italic", 10), bg="#d9d9d9", command=get)
get.place(relx=0.674, rely=0.371, height=24, width=97)

rent = Button(root, text="Rent Operations", font=(
    "italic", 10), bg="#d9d9d9")
rent.place(relx=0.8, rely=0.371, height=24, width=96)

'''LIST OUTPUT'''
customer = Label(root, text="Customer Table", font=("Comic Sans MC", 9))
customer.place(relx=0.537, rely=0.452, height=21, width=89)

customer_list = tkinter.ttk.Treeview(height=10, columns=5)
customer_list.grid(row=4, column=0)

customer_list.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6 Col7 Col8 Col9")
customer_list.heading("#0", text='ID', anchor=N)
customer_list.column("#0", width='15')
customer_list.heading("Col1", text='First Name', anchor=N)
customer_list.column("Col1", width='50')
customer_list.heading("Col2", text='Last Name', anchor=N)
customer_list.column("Col2", width='50')
customer_list.heading("Col3", text='Password', anchor=N)
customer_list.column("Col3", width='70')
customer_list.heading("Col4", text='Email', anchor=N)
customer_list.column("Col4", width='100')
customer_list.heading("Col5", text='Address', anchor=N)
customer_list.column("Col5", width='100')
customer_list.heading("Col6", text='Telephone', anchor=N)
customer_list.column("Col6", width='100')
customer_list.heading("Col7", text='Username', anchor=N)
customer_list.column("Col7", width='100')
customer_list.heading("Col8", text='Age', anchor=N)
customer_list.column("Col8", width='20')
customer_list.heading("Col9", text='Money', anchor=N)
customer_list.column("Col9", width='50')

customer_list.place(relx=0.217, rely=0.5, relheight=0.389, relwidth=0.721)
cust_list()

tk.mainloop()
