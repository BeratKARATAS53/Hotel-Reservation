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


hotelRoot = tk.Tk()
hotelRoot.geometry("1007x634+99+96")
hotelRoot.minsize(120, 1)
hotelRoot.maxsize(1370, 749)
hotelRoot.resizable(1, 1)
hotelRoot.title("Main Page")
hotelRoot.configure(background='#EBEDEF')


def customerPage():
    import CustomerPage


def reservationPage():
    import ReservationPage


def statisticPage():
    import StatisticPage


def otherOperations():
    import EmployeeManagerPage


def add():
    hotel_id = e_hotel_id.get()
    name = e_name.get()
    telephone = e_telephone.get()
    address = e_address.get("1.0", END)
    info = e_info.get("1.0", END)
    stars = e_stars.get()
    hotel_type = e_hotel_type.get()

    if(name == "" or telephone == "" or address == "" or info == "" or hotel_type == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addHotel('" + name + "','" + address + "','" +
                       telephone + "','" + info + "'," + stars + ",'" + hotel_type + "')")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        get_hotels()

        e_name.delete(0, "end")
        e_telephone.delete(0, "end")
        e_address.delete('1.0', END)
        e_info.delete('1.0', END)
        e_hotel_type.delete(0, "end")
        e_stars.delete(0, "end")

        con.close()


def update():
    hotel_id = e_hotel_id.get()
    name = e_name.get()
    telephone = e_telephone.get()
    address = e_address.get("1.0", END)
    info = e_info.get("1.0", END)
    stars = e_stars.get()
    hotel_type = e_hotel_type.get()

    if(hotel_id == "" or name == "" or telephone == "" or address == "" or info == "" or hotel_type == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from hotel where id = " + hotel_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_hotel_id.delete(0, "end")

        else:
            cursor.execute("Call updateHotel('" + hotel_id + "','" + name + "','" + address +
                           "','" + telephone + "','" + info + "'," + stars + ",'" + hotel_type + "')")

            Messagebox.showinfo("Update Status", "Updated Succesfully")
            con.commit()
            get_hotels()

            e_hotel_id.delete(0, "end")
            e_name.delete(0, "end")
            e_telephone.delete(0, "end")
            e_address.delete('1.0', END)
            e_info.delete('1.0', END)
            e_hotel_type.delete(0, "end")
            e_stars.delete(0, "end")

        con.close()


def delete():
    hotel_id = e_hotel_id.get()
    if(hotel_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from hotel where id = " + hotel_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_hotel_id.delete(0, "end")

        else:
            cursor.execute("Call deleteHotel(" + hotel_id + ")")

            e_name.delete(0, "end")
            e_telephone.delete(0, "end")
            e_address.delete('1.0', END)
            e_info.delete('1.0', END)
            e_hotel_type.delete(0, "end")
            e_stars.delete(0, "end")

            Messagebox.showinfo("Delete Status", "Delete Succesfully")
            con.commit()
            get_hotels()

        con.close()


def get_hotels():
    records = hotel_list.get_children()
    for element in records:
        hotel_list.delete(element)

    con = mysql.connect(host="localhost", user="admin",
                        password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("select * from hotel_balance order by id asc")
    hotels = cursor.fetchall()

    for hotel in hotels:
        hotel_list.insert('', 0, text=hotel[0], value=(
            hotel[1], hotel[2], hotel[3], hotel[4], hotel[5], hotel[6], hotel[8]))

    con.close()


def get():
    e_name.delete(0, "end")
    e_telephone.delete(0, "end")
    e_address.delete('1.0', END)
    e_info.delete('1.0', END)
    e_hotel_type.delete(0, "end")
    e_stars.delete(0, "end")

    hotel_id = e_hotel_id.get()
    if(hotel_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from hotel where id = " + hotel_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_hotel_id.delete(0, "end")

        else:
            cursor.execute(
                "select * from hotel_balance where id = " + hotel_id + "")
            hotels = cursor.fetchall()

            for hotel in hotels:
                e_name.insert(0, hotel[1])
                e_address.insert(INSERT, hotel[2])
                e_telephone.insert(0, hotel[3])
                e_info.insert(INSERT, hotel[4])
                e_stars.insert(0, hotel[5])
                e_hotel_type.insert(INSERT, hotel[6])

            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")

        con.close()


def otherOperationsFunc():

    e_name.delete(0, "end")
    e_telephone.delete(0, "end")
    e_address.delete('1.0', END)
    e_info.delete('1.0', END)
    e_hotel_type.delete(0, "end")
    e_stars.delete(0, "end")

    hotel_id = e_hotel_id.get()
    if(hotel_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from hotel where id = " + hotel_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_hotel_id.delete(0, "end")

        else:
            cursor.execute(
                "select * from hotel_balance where id = " + hotel_id + "")
            hotels = cursor.fetchall()

            for hotel in hotels:
                e_name.insert(0, hotel[1])
                e_address.insert(INSERT, hotel[2])
                e_telephone.insert(0, hotel[3])
                e_info.insert(INSERT, hotel[4])
                e_stars.insert(0, hotel[5])
                e_hotel_type.insert(INSERT, hotel[6])

            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")

            otherOperations()
        con.close()


'''SIDE BAR'''
hotel = Button(hotelRoot, text="HOTEL", font=(
    "calibri", 10), bg="#F1C40F")
hotel.place(relx=0.02, rely=0.063, height=24, width=147)

customer = Button(hotelRoot, text="CUSTOMER", font=(
    "calibri", 10), bg="#FEF9E7", command=customerPage)
customer.place(relx=0.02, rely=0.126, height=24, width=147)

reservation = Button(hotelRoot, text="RESERVATION", font=(
    "calibri", 10), bg="#FEF9E7", command=reservationPage)
reservation.place(relx=0.02, rely=0.189, height=24, width=147)

statistics = Button(hotelRoot, text="TABLE STATISTICS", font=(
    "calibri", 10), bg="#FEF9E7", command=statisticPage)
statistics.place(relx=0.02, rely=0.249, height=24, width=147)

TSeparator1 = ttk.Separator(hotelRoot)
TSeparator1.place(relx=0.179, rely=0.032, relheight=0.82)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(hotelRoot)
TSeparator2.place(relx=0.189, rely=0.379, relwidth=0.775)

'''INPUT TEXTS'''
hotel_id = Label(hotelRoot, text="ID: ", font=("calibri", 9))
hotel_id.place(relx=0.199, rely=0.063, height=21, width=23)

e_hotel_id = Entry(hotelRoot)
e_hotel_id.place(relx=0.228, rely=0.063, height=20, relwidth=0.034)

name = Label(hotelRoot, text="Name: ", font=("calibri", 9))
name.place(relx=0.268, rely=0.063, height=21, width=76)

e_name = Entry(hotelRoot)
e_name.place(relx=0.348, rely=0.063, height=20, relwidth=0.292)

telephone = Label(hotelRoot, text="Phone: ", font=("calibri", 9))
telephone.place(relx=0.645, rely=0.063, height=21, width=67)

e_telephone = Entry(hotelRoot)
e_telephone.place(relx=0.715, rely=0.063, height=20, relwidth=0.133)

address = Label(hotelRoot, text="Hotel Address: ", font=("calibri", 9))
address.place(relx=0.199, rely=0.11, height=21, width=86)

e_address = Text(hotelRoot)
e_address.place(relx=0.288, rely=0.11, relheight=0.164, relwidth=0.163)

info = Label(hotelRoot, text="Hotel Information: ", font=("calibri", 9))
info.place(relx=0.457, rely=0.11, height=21, width=107)

e_info = Text(hotelRoot)
e_info.place(relx=0.566, rely=0.11, relheight=0.164, relwidth=0.193)

'''COMBOBOX'''
hotel_type = Label(hotelRoot, text="Hotel Type: ", font=("calibri", 9))
hotel_type.place(relx=0.765, rely=0.11, height=21, width=69)

box_value = StringVar()
e_hotel_type = ttk.Combobox(
    hotelRoot, textvariable=box_value, state='readonly')
e_hotel_type.place(relx=0.834, rely=0.11, relheight=0.033, relwidth=0.082)

e_hotel_type['values'] = ('Normal', 'Termal', 'Bungalow')
e_hotel_type.current(0)

'''SPINBOX'''
stars = Label(hotelRoot, text="Stars: ", font=("calibri", 9))
stars.place(relx=0.844, rely=0.063, height=21, width=37)

var = StringVar(hotelRoot)
var.set("5")
e_stars = Spinbox(hotelRoot, from_=1, to=10, textvariable=var)
e_stars.place(relx=0.884, rely=0.063, relheight=0.03, relwidth=0.035)


'''OPERATION BUTTONS'''
add = Button(hotelRoot, text="Add", font=(
    "calibri", 10), bg="#7DCEA0", command=add)
add.place(relx=0.318, rely=0.3, height=24, width=97)

update = Button(hotelRoot, text="Update", font=(
    "calibri", 10), bg="#5DADE2", command=update)
update.place(relx=0.427, rely=0.3, height=24, width=99)

delete = Button(hotelRoot, text="Delete", font=(
    "calibri", 10), bg="#F1948A", command=delete)
delete.place(relx=0.536, rely=0.3, height=24, width=97)

get = Button(hotelRoot, text="Get hotel", font=(
    "calibri", 10), bg="#BB8FCE", command=get)
get.place(relx=0.645, rely=0.3, height=24, width=97)

operation = Button(hotelRoot, text="Other Operations", font=(
    "calibri", 10), bg="#b3ecff", command=otherOperationsFunc)
operation.place(relx=0.755, rely=0.3, height=24, width=127)

'''LIST OUTPUT'''
hotels = Label(hotelRoot, text="Hotel Table", font=("Comic Sans MC", 9))
hotels.place(relx=0.536, rely=0.41, height=31, width=66)

hotel_list = ttk.Treeview(hotelRoot, height=10, columns=5)
hotel_list.grid(row=4, column=0)

hotel_list.configure(columns="Col1 Col2 Col4 Col5 Col6 Col7 Col8")
hotel_list.heading("#0", text='ID', anchor=N)
hotel_list.column("#0", width='40', stretch=NO)
hotel_list.heading("Col1", text='Name', anchor=N)
hotel_list.column("Col1", width='50')
hotel_list.heading("Col2", text='Address', anchor=N)
hotel_list.column("Col2", width='100')
hotel_list.heading("Col4", text='Telephone', anchor=N)
hotel_list.column("Col4", width='100', stretch=NO)
hotel_list.heading("Col5", text='Hotel Info', anchor=N)
hotel_list.column("Col5", width='100')
hotel_list.heading("Col6", text='Stars', anchor=N)
hotel_list.column("Col6", width='50', stretch=NO)
hotel_list.heading("Col7", text='Hotel Type', anchor=N)
hotel_list.column("Col7", width='75', stretch=NO)
hotel_list.heading("Col8", text='Balance (₺)', anchor=N)
hotel_list.column("Col8", width='50', stretch=NO)

hotel_list.place(relx=0.189, rely=0.457, relheight=0.38, relwidth=0.776)
get_hotels()

tk.mainloop()
