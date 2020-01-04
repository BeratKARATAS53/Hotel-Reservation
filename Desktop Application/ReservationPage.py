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
from datetime import datetime

reservRoot = tk.Tk()
reservRoot.geometry("845x587+204+81")
reservRoot.minsize(120, 1)
reservRoot.maxsize(1370, 749)
reservRoot.resizable(1, 1)
reservRoot.title("Reservation Page")


def customerPage():
    import CustomerPage


def hotelPage():
    import HotelPage


def statisticPage():
    import StatisticPage


def add():
    reserv_id = e_reserv_id.get()
    start_date = e_start_date.get()
    finish_date = e_finish_date.get()
    room_number = e_room_number.get()
    customee_id = e_customee_id.get()

    if(start_date == "" or finish_date == "" or room_number == "" or customee_id == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addReservation('" + start_date + "','" +
                       finish_date + "'," + customee_id + ",'" + room_number + "')")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        reserv_list()
        con.close()


def update():
    reserv_id = e_reserv_id.get()
    start_date = e_start_date.get()
    finish_date = e_finish_date.get()
    room_number = e_room_number.get()
    customee_id = e_customee_id.get()

    if(reserv_id == "" or start_date == "" or finish_date == "" or room_number == "" or customee_id == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from reservation where id = " + reserv_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_reserv_id.delete(0, "end")

        else:
            cursor.execute("Call updateReservation('" + reserv_id + "','" + start_date + "','" +
                           finish_date + "'," + customee_id + ",'" + room_number + "')")

            Messagebox.showinfo("Update Status", "Updated Succesfully")
            con.commit()
            reserv_list()

        con.close()


def delete():
    reserv_id = e_reserv_id.get()
    if(reserv_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from reservation where id = " + reserv_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_reserv_id.delete(0, "end")

        else:
            cursor.execute("Call deleteReservation(" + reserv_id + ")")

            e_reserv_id.insert(0, "")
            e_start_date.insert(0, "")
            e_finish_date.insert(0, "")
            e_room_number.insert(0, "")
            e_customee_id.insert(0, "")

            Messagebox.showinfo("Delete Status", "Delete Succesfully")
            con.commit()
            reserv_list()
        con.close()


def reserv_list():
    records = reservation_list.get_children()
    for element in records:
        reservation_list.delete(element)

    con = mysql.connect(host="localhost", user="admin",
                        password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("select * from reservation")
    reservation = cursor.fetchall()

    for reserv in reservation:
        reservation_list.insert('', 0, text=reserv[0], value=(
            reserv[1], reserv[2], reserv[3], reserv[4]))

    con.close()


def serv_list():
    records = service_list.get_children()
    for element in records:
        service_list.delete(element)

    con = mysql.connect(host="localhost", user="admin",
                        password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()

    """ Eğer Oda Özel Değil ise Yemek Servislerini Göstermemesi Gerek 
    boolean = cursor.execute(
        "select substring_index(substring_index(room_number,'-',-2),'-',1) from room where id=9")
    boolean = cursor.fetchall()
    food
    if(boolean == 1):
        cursor.execute(
            "select * from extraservice where hotel_id = substring_index('1-0-100', '-', 1) order by id desc")
        food = cursor.fetchall()
    """
    cursor.execute(
        "select * from extraservice where hotel_id = substring_index('1-0-100', '-', 1) order by id desc")
    service = cursor.fetchall()

    for serv in service:
        service_list.insert('', 0, text=serv[0], value=(serv[1], serv[2]))

    con.close()


def get():
    e_start_date.delete(0, "end")
    e_finish_date.delete(0, "end")
    e_room_number.delete(0, "end")
    e_customee_id.delete(0, "end")

    reserv_id = e_reserv_id.get()

    if(reserv_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from reservation where id = " + reserv_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_reserv_id.delete(0, "end")

        else:
            cursor.execute(
                "select * from reservation where id = " + reserv_id + "")
            reservation = cursor.fetchall()

            cursor.execute(
                "select r.room_number from room_reservation rr, room r where rr.room_id=r.id and rr.reservation_id = " + reserv_id + "")
            room_no = cursor.fetchall()

            for reserve in reservation:
                e_start_date.insert(0, reserve[1])
                e_finish_date.insert(0, reserve[2])
                e_customee_id.insert(0, reserve[4])
                e_room_number.insert(0, room_no)

            e_reserv_id.insert(0, "")
            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")
        con.close()


'''SIDE BAR'''
hotel = Button(reservRoot, text="HOTEL", font=(
    "bold", 10), bg="#d9d9d9", command=hotelPage)
hotel.place(relx=0.024, rely=0.068, height=24, width=127)

customer = Button(reservRoot, text="CUSTOMER", font=(
    "bold", 10), bg="#d9d9d9", command=customerPage)
customer.place(relx=0.024, rely=0.136, height=24, width=127)

reservation = Button(reservRoot, text="RESERVATION", font=(
    "bold", 10), bg="#80ff00")
reservation.place(relx=0.024, rely=0.204, height=24, width=127)

statistics = Button(reservRoot, text="TABLE STATISTICS", font=(
    "bold", 10), bg="#d9d9d9", command=statisticPage)
statistics.place(relx=0.024, rely=0.274, height=24, width=127)

TSeparator1 = ttk.Separator(reservRoot)
TSeparator1.place(relx=0.201, rely=0.034, relheight=0.92)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(reservRoot)
TSeparator2.place(relx=0.213, rely=0.375, relwidth=0.71)

'''INPUT TEXTS'''
reserv_id = Label(reservRoot, text="ID: ", font=("bold", 9))
reserv_id.place(relx=0.225, rely=0.068, height=21, width=23)

e_reserv_id = Entry(reservRoot)
e_reserv_id.place(relx=0.26, rely=0.068, height=20, relwidth=0.04)

start_date = Label(reservRoot, text="Start Date: ", font=("bold", 9))
start_date.place(relx=0.308, rely=0.068, height=21, width=63)

e_start_date = Entry(reservRoot)
e_start_date.place(relx=0.391, rely=0.068, height=20, relwidth=0.099)

finish_date = Label(reservRoot, text="Finish Date: ", font=("bold", 9))
finish_date.place(relx=0.497, rely=0.068, height=21, width=70)

e_finish_date = Entry(reservRoot)
e_finish_date.place(relx=0.58, rely=0.068, height=20, relwidth=0.099)

room_number = Label(reservRoot, text="Room No: ", font=("bold", 9))
room_number.place(relx=0.686, rely=0.068, height=21, width=63)

e_room_number = Entry(reservRoot)
e_room_number.place(relx=0.769, rely=0.068, height=20, relwidth=0.064)

customee_id = Label(reservRoot, text="Customer ID: ", font=("bold", 9))
customee_id.place(relx=0.698, rely=0.119, height=21, width=78)

e_customee_id = Entry(reservRoot)
e_customee_id.place(relx=0.793, rely=0.119, height=20, relwidth=0.04)

'''OPERATION BUTTONS'''
add = Button(reservRoot, text="Add", font=(
    "italic", 10), bg="#d9d9d9", command=add)
add.place(relx=0.331, rely=0.307, height=24, width=97)

update = Button(reservRoot, text="Update", font=(
    "italic", 10), bg="#d9d9d9", command=update)
update.place(relx=0.473, rely=0.307, height=24, width=99)

delete = Button(reservRoot, text="Delete", font=(
    "italic", 10), bg="#d9d9d9", command=delete)
delete.place(relx=0.615, rely=0.307, height=24, width=97)

get = Button(reservRoot, text="Get Reservation", font=(
    "italic", 10), bg="#d9d9d9", command=get)
get.place(relx=0.757, rely=0.307, height=24, width=97)

'''LIST OUTPUT'''
extra_services = Label(reservRoot, text="Extra Services: ", font=("bold", 9))
extra_services.place(relx=0.225, rely=0.117, height=21, width=83)

service_list = ttk.Treeview(reservRoot, height=10, columns=5)
service_list.grid(row=4, column=0, columnspan=2)

service_list.configure(columns="Col1 Col2")
service_list.heading("#0", text='ID', anchor=N)
service_list.column("#0", width='50', stretch=NO)
service_list.heading("Col1", text='Service', anchor=N)
service_list.column("Col1", width='120')
service_list.heading("Col2", text='Price (₺)', anchor=N)
service_list.column("Col2", width='120')

service_list.place(relx=0.331, rely=0.117, relheight=0.162, relwidth=0.304)
serv_list()

reservation = Label(reservRoot, text="Reservation Table", font=("bold", 9))
reservation.place(relx=0.544, rely=0.392, height=21, width=98)

reservation_list = ttk.Treeview(reservRoot, height=10, columns=5)
reservation_list.grid(row=4, column=0, columnspan=2)

reservation_list.configure(columns="Col1 Col2 Col3 Col4")
reservation_list.heading("#0", text='ID', anchor=N)
reservation_list.column("#0", width='50', stretch=NO)
reservation_list.heading("Col1", text='Start Date', anchor=N)
reservation_list.column("Col1", width='120')
reservation_list.heading("Col2", text='Finish Date', anchor=N)
reservation_list.column("Col2", width='120')
reservation_list.heading("Col3", text='Price (₺)', anchor=N)
reservation_list.column("Col3", width='50')
reservation_list.heading("Col4", text='Customer ID', anchor=N)
reservation_list.column("Col4", width='80', stretch=NO)

reservation_list.place(relx=0.225, rely=0.426, relheight=0.513, relwidth=0.699)
reserv_list()

tk.mainloop()
