import tkinter as tk
from tkinter import *
import tkinter.ttk
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

from datetime import datetime


def add():
    reserv_id = r_reserv_id.get()
    start_date = r_start_date.get()
    finish_date = r_finish_date.get()
    room_number = r_room_number.get()
    customer_id = r_customer_id.get()

    if(start_date == "" or finish_date == "" or room_number == "" or customer_id == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addReservation('" + start_date + "','" +
                       finish_date + "'," + customer_id + ",'" + room_number + "')")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        reserv_list()
        con.close()


def update():
    reserv_id = r_reserv_id.get()
    start_date = r_start_date.get()
    finish_date = r_finish_date.get()
    room_number = r_room_number.get()
    customer_id = r_customer_id.get()

    if(reserv_id == "" or start_date == "" or finish_date == "" or room_number == "" or customer_id == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call updateReservation('" + reserv_id + "','" + start_date + "','" +
                       finish_date + "'," + customer_id + ",'" + room_number + "')")

        Messagebox.showinfo("Update Status", "Updated Succesfully")
        con.commit()
        reserv_list()

        con.close()


def delete():
    reserv_id = r_reserv_id.get()
    if(reserv_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call deleteReservation(" + reserv_id + ")")

        r_reserv_id.insert(0, "")
        r_start_date.insert(0, "")
        r_finish_date.insert(0, "")
        r_room_number.insert(0, "")
        r_customer_id.insert(0, "")

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

    '''
    cursor.execute("select * from extraservice")
    extraservices = cursor.fetchall()

    for extraservice in extraservices:
        insertService = str(
            extraservice[1]) + '   ' + str(extraservice[2]) + '   ' + str(extraservice[3])
        extra_service_list.insert(extra_service_list.size()+1, insertService)
    '''
    con.close()


def get():
    reserv_id = r_reserv_id.get()

    if(reserv_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select * from reservation where id = " + reserv_id + "")
        reservation = cursor.fetchall()

        for reserve in reservation:
            r_start_date.insert(0, reserve[1])
            r_finish_date.insert(0, reserve[2])
            r_customer_id.insert(0, reserve[4])

        r_reserv_id.insert(0, "")
        Messagebox.showinfo("Fetch Status", "Fetch Succesfully")
        con.close()


root = tk.Tk()
root.geometry("1008x674")
root.title("Main Page")

'''SIDE BAR'''
hotel = Button(root, text="HOTEL", font=(
    "bold", 10), bg="#d9d9d9")
hotel.place(relx=0.024, rely=0.068, height=24, width=127)

customer = Button(root, text="CUSTOMER", font=(
    "bold", 10), bg="#80e5ff")
customer.place(relx=0.024, rely=0.136, height=24, width=127)

reservation = Button(root, text="RESERVATION", font=(
    "bold", 10), bg="#d9d9d9")
reservation.place(relx=0.024, rely=0.204, height=24, width=127)

TSeparator1 = tkinter.ttk.Separator()
TSeparator1.place(relx=0.201, rely=0.034, relheight=0.92)
TSeparator1.configure(orient="vertical")

TSeparator2 = tkinter.ttk.Separator()
TSeparator2.place(relx=0.213, rely=0.375, relwidth=0.71)

'''INPUT TEXTS'''
reserv_id = Label(root, text="ID: ", font=("bold", 9))
reserv_id.place(relx=0.225, rely=0.068, height=21, width=23)

r_reserv_id = Entry()
r_reserv_id.place(relx=0.26, rely=0.068, height=20, relwidth=0.064)

start_date = Label(root, text="Start Date: ", font=("bold", 9))
start_date.place(relx=0.331, rely=0.068, height=21, width=63)

r_start_date = Entry()
r_start_date.place(relx=0.414, rely=0.068, height=20, relwidth=0.099)

finish_date = Label(root, text="Finish Date: ", font=("bold", 9))
finish_date.place(relx=0.509, rely=0.068, height=21, width=70)

r_finish_date = Entry()
r_finish_date.place(relx=0.592, rely=0.068, height=20, relwidth=0.099)

room_number = Label(root, text="Room Number: ", font=("bold", 9))
room_number.place(relx=0.698, rely=0.068, height=21, width=63)

r_room_number = Entry()
r_room_number.place(relx=0.781, rely=0.068, height=20, relwidth=0.052)

customer_id = Label(root, text="Customer ID: ", font=("bold", 9))
customer_id.place(relx=0.698, rely=0.119, height=21, width=78)

r_customer_id = Entry()
r_customer_id.place(relx=0.793, rely=0.119, height=20, relwidth=0.04)

'''OPERATION BUTTONS'''
add = Button(root, text="Add", font=(
    "italic", 10), bg="#d9d9d9", command=add)
add.place(relx=0.331, rely=0.307, height=24, width=97)

update = Button(root, text="Update", font=(
    "italic", 10), bg="#d9d9d9", command=update)
update.place(relx=0.473, rely=0.307, height=24, width=99)

delete = Button(root, text="Delete", font=(
    "italic", 10), bg="#d9d9d9", command=delete)
delete.place(relx=0.615, rely=0.307, height=24, width=97)

get = Button(root, text="Get Reservation", font=(
    "italic", 10), bg="#d9d9d9", command=get)
get.place(relx=0.757, rely=0.307, height=24, width=97)

'''LIST OUTPUT'''
extra_services = Label(root, text="Extra Services: ", font=("bold", 9))
room_number.place(relx=0.225, rely=0.119, height=21, width=83)

reservation = Label(root, text="Reservation Table", font=("bold", 9))
reservation.place(relx=0.544, rely=0.392, height=21, width=98)

reservation_list = tkinter.ttk.Treeview(height=10, columns=5)
reservation_list.grid(row=4, column=0, columnspan=2)

reservation_list.configure(columns="Col1 Col2 Col3 Col4")
reservation_list.heading("#0", text='ID', anchor=W)
reservation_list.column("#0", width='20')
reservation_list.heading("Col1", text='Start Date', anchor=W)
reservation_list.column("Col1", width='120')
reservation_list.heading("Col2", text='Finish Date', anchor=W)
reservation_list.column("Col2", width='120')
reservation_list.heading("Col3", text='Price', anchor=W)
reservation_list.column("Col3", width='100')
reservation_list.heading("Col4", text='Customer ID', anchor=W)
reservation_list.column("Col4", width='100')

tkinter.ttk.Button(text="Delete Record").grid(row=5, column=0)
tkinter.ttk.Button(text="Edit Record").grid(row=5, column=1)

reservation_list.place(relx=0.225, rely=0.426, relheight=0.513, relwidth=0.699)
reserv_list()

tk.mainloop()
