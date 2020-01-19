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
reservRoot.geometry("772x536+261+104")
reservRoot.minsize(120, 1)
reservRoot.maxsize(1370, 749)
reservRoot.resizable(1, 1)
reservRoot.title("Reservation Page")
reservRoot.configure(background='#EBEDEF')


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
    total_price = e_price.get()

    if(start_date == "" or finish_date == "" or room_number == "" or customee_id == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Select r.status From room r Where r.room_number = '" + room_number + "'")
        room_status = cursor.fetchall()

        if(room_status[0][0] == 'not available'):
            Messagebox.showinfo("Fetch Status", "Room Not Available For Booking")
        else:
            cursor.execute("Call addReservation('" + start_date + "','" +
                        finish_date + "'," + customee_id + ",'" + room_number + "',"+ total_price + ")")

            Messagebox.showinfo("Insert Status", "Inserted Succesfully")
            con.commit()
            reserv_list()

            e_reserv_id.delete(0, "end")
            e_start_date.delete(0, "end")
            e_finish_date.delete(0, "end")
            e_room_number.delete(0, "end")
            e_customee_id.delete(0, "end")
            e_price.delete(0, "end")
                
            con.close()


def update():
    reserv_id = e_reserv_id.get()
    start_date = e_start_date.get()
    finish_date = e_finish_date.get()
    room_number = e_room_number.get()
    customee_id = e_customee_id.get()
    total_price = e_price.get()

    if(reserv_id == "" or start_date == "" or finish_date == "" or room_number == "" or customee_id == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call deleteReservation(" + reserv_id + ")")
        con.commit()
        cursor.execute("Call addReservation('" + start_date + "','" +
                       finish_date + "'," + customee_id + ",'" + room_number + "',"+ total_price + ")")

        Messagebox.showinfo("Update Status", "Updated Succesfully")
        con.commit()
        reserv_list()

        e_reserv_id.delete(0, "end")
        e_start_date.delete(0, "end")
        e_finish_date.delete(0, "end")
        e_room_number.delete(0, "end")
        e_customee_id.delete(0, "end")
        e_price.config(state="normal")
        e_price.delete(0, "end")

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
            e_price.config(state="normal")
            e_price.delete(0, "end")

            Messagebox.showinfo("Delete Status", "Deleted Succesfully")
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


def get():
    e_start_date.delete(0, "end")
    e_finish_date.delete(0, "end")
    e_room_number.delete(0, "end")
    e_customee_id.delete(0, "end")

    e_price.config(state="normal")
    e_price.delete(0, "end")

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
                e_price.insert(0, reserve[3])
                e_customee_id.insert(0, reserve[4])
                e_room_number.insert(0, room_no)

            e_price.config(state="disabled")

            e_reserv_id.insert(0, "")
            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")
            con.close()


def serv_list():
    records = service_list.get_children()
    for element in records:
        service_list.delete(element)
    e_price.config(state="normal")
    e_price.delete(0, "end")

    start_date = e_start_date.get()
    finish_date = e_finish_date.get()
    room_number = e_room_number.get()
    
    if(start_date == "" or finish_date == "" or room_number == ""):
        Messagebox.showinfo(
            "Fetch Status", "Start Date, Finish Date, and Room Number is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("(select day('" + finish_date +"') - day('" + start_date + "'))")
        difference_date = cursor.fetchall()
        diff = difference_date[0][0]
        if(diff == 0):
            diff = 1

        cursor.execute("select room_price from room where room_number = '" + room_number + "'")
        price = cursor.fetchall()
        e_price.insert(0, float(price[0][0])*diff)
        e_price.config(state="disabled")

        cursor.execute("select substring_index(substring_index('" + room_number + "','-',-2),'-',1)")
        boolean = cursor.fetchall()
        if(boolean[0][0] == 0):
            cursor.execute(
                "select * from extraservice where hotel_id = substring_index('" + room_number + "', '-', 1) and id not in (select f.service_id from foodservice f)")
            notFood = cursor.fetchall()
            for noo in notFood:
                service_list.insert('', 0, text=noo[0], value=(noo[1], noo[2]))
        
        cursor.execute(
            "select * from extraservice where hotel_id = substring_index('" + room_number + "', '-', 1) order by id desc")
        service = cursor.fetchall()
        for serv in service:
            service_list.insert('', 0, text=serv[0], value=(serv[1], serv[2]))
            
        con.close()


def addService():
    start_date = e_start_date.get()
    finish_date = e_finish_date.get()
    service_id = e_service_id.get()
    room_number = e_room_number.get()
    if(start_date == "" or finish_date == "" or service_id == ""):
        Messagebox.showinfo("Insert Status", "Start Date, Finish Date, and Service ID Must Be Entered!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()

        cursor.execute(
            "select exists (select * from extraservice where id = " + service_id + " and hotel_id = substring_index('" + room_number + "', '-', 1))")
        boolean = cursor.fetchall()
        
        if(boolean[0][0] == 0):
            Messagebox.showinfo("Fetch Status", "Fetch Failed! Service Not Found")
            e_service_id.delete(0, "end")
        else:
            cursor.execute("select id from room where room_number = '" + room_number + "'")
            room_id = cursor.fetchall()

            cursor.execute("select service_price from extraservice where id = '" + service_id + "'")
            service_price = cursor.fetchall()
            
            cursor.execute("select exists (select * from room_extraservice where room_id = '" + str(room_id[0][0]) + "' and service_id = '" + str(service_id) + "')")
            existsRoomExtra = cursor.fetchall()

            if(existsRoomExtra[0][0] == 1):
                Messagebox.showinfo("Insert Status", "Service Already Added!")
            else:
                cursor.execute("Call addroom_extraservice('" + str(room_id[0][0]) + "','" + str(service_id) + "')")

                Messagebox.showinfo("Insert Status", "Service Inserted Succesfully")
                
                e_price.config(state="normal")
                room_price = float(e_price.get()) + service_price[0][0]
                e_price.delete(0, "end")
                e_price.insert(0, room_price)
                e_price.config(state="disabled")

                con.commit()
                con.close()

def deleteService():
    start_date = e_start_date.get()
    finish_date = e_finish_date.get()
    service_id = e_service_id.get()
    room_number = e_room_number.get()
    if(start_date == "" or finish_date == "" or service_id == ""):
        Messagebox.showinfo("Delete Status", "Start Date, Finish Date, and Service ID Must Be Entered!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("select id from room where room_number = '" + room_number + "'")
        room_id = cursor.fetchall()
        cursor.execute("select service_price from extraservice where id = '" + service_id + "'")
        service_price = cursor.fetchall()
        
        cursor.execute("select exists (select * from room_extraservice where room_id = '" + str(room_id[0][0]) + 
                        "' and service_id = '" + str(service_id) + "')")
        existsRoomExtra = cursor.fetchall()

        if(existsRoomExtra[0][0] == 0):
            Messagebox.showinfo("Delete Status", "You Cannot Delete a Service That is Not!")
        else:
            cursor.execute("Call deleteroom_extraservice('" + str(room_id[0][0]) + "','" + str(service_id) + "')")

            Messagebox.showinfo("Delete Status", "Service Deleted Succesfully")

            e_price.config(state="normal")
            room_price = float(e_price.get()) - service_price[0][0]
            e_price.delete(0, "end")
            e_price.insert(0, room_price)
            e_price.config(state="disabled")

            con.commit()
            con.close()

'''SIDE BAR'''
hotel = Button(reservRoot, text="HOTEL", font=(
    "calibri", 10), bg="#FEF9E7", command=hotelPage)
hotel.place(relx=0.026, rely=0.075, height=24, width=127)

customer = Button(reservRoot, text="CUSTOMER", font=(
    "calibri", 10), bg="#FEF9E7", command=customerPage)
customer.place(relx=0.026, rely=0.149, height=24, width=127)

reservation = Button(reservRoot, text="RESERVATION", font=(
    "calibri", 10), bg="#F1C40F")
reservation.place(relx=0.026, rely=0.224, height=24, width=127)

statistics = Button(reservRoot, text="TABLE STATISTICS", font=(
    "calibri", 10), bg="#FEF9E7", command=statisticPage)
statistics.place(relx=0.026, rely=0.299, height=24, width=127)

TSeparator1 = ttk.Separator(reservRoot)
TSeparator1.place(relx=0.22, rely=0.056, relheight=0.858)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(reservRoot)
TSeparator2.place(relx=0.233, rely=0.485, relwidth=0.699)

TSeparator3_1 = ttk.Separator(reservRoot)
TSeparator3_1.place(relx=0.233, rely=0.392, relwidth=0.453)

TSeparator3_2 = ttk.Separator(reservRoot)
TSeparator3_2.place(relx=0.233, rely=0.131, relwidth=0.453)

TSeparator3_3 = ttk.Separator(reservRoot)
TSeparator3_3.place(relx=0.687, rely=0.131, relheight=0.261)
TSeparator3_3.configure(orient="vertical")

TSeparator3_4 = ttk.Separator(reservRoot)
TSeparator3_4.place(relx=0.233, rely=0.131, relheight=0.261)
TSeparator3_4.configure(orient="vertical")

'''INPUT TEXTS'''
reserv_id = Label(reservRoot, text="ID: ", font=("calibri", 9))
reserv_id.place(relx=0.246, rely=0.075, height=21, width=23)

e_reserv_id = Entry(reservRoot)
e_reserv_id.place(relx=0.285, rely=0.075,height=20, relwidth=0.044)

start_date = Label(reservRoot, text="Start Date: ", font=("calibri", 9))
start_date.place(relx=0.337, rely=0.075, height=21, width=63)

e_start_date = Entry(reservRoot)
e_start_date.place(relx=0.427, rely=0.075, height=20, relwidth=0.109)

finish_date = Label(reservRoot, text="Finish Date: ", font=("calibri", 9))
finish_date.place(relx=0.544, rely=0.075, height=21, width=70)

e_finish_date = Entry(reservRoot)
e_finish_date.place(relx=0.648, rely=0.075, height=20, relwidth=0.109)

room_number = Label(reservRoot, text="Room No: ", font=("calibri", 9))
room_number.place(relx=0.712, rely=0.131, height=21, width=63)

e_room_number = Entry(reservRoot)
e_room_number.place(relx=0.803, rely=0.131, height=20, relwidth=0.07)

customee_id = Label(reservRoot, text="Customer ID: ", font=("calibri", 9))
customee_id.place(relx=0.712, rely=0.187, height=21, width=78)

e_customee_id = Entry(reservRoot)
e_customee_id.place(relx=0.842, rely=0.187, height=20, relwidth=0.031)

price = Label(reservRoot, text="Room Price (₺): ", font=("calibri", 9))
price.place(relx=0.717, rely=0.243, height=21, width=80)

e_price = Entry(reservRoot)
e_price.place(relx=0.825, rely=0.243,height=20, relwidth=0.05)

service_id = Label(reservRoot, text="Service ID: ", font=("calibri", 9))
service_id.place(relx=0.246, rely=0.336, height=21, width=62)

e_service_id = Entry(reservRoot)
e_service_id.place(relx=0.337, rely=0.336, height=20, relwidth=0.031)

'''OPERATION BUTTONS'''
add = Button(reservRoot, text="Add", font=(
    "calibri", 10), bg="#7DCEA0", command=add)
add.place(relx=0.324, rely=0.429, height=24, width=97)

update = Button(reservRoot, text="Update", font=(
    "calibri", 10), bg="#5DADE2", command=update)
update.place(relx=0.466, rely=0.429, height=24, width=99)

delete = Button(reservRoot, text="Delete", font=(
    "calibri", 10), bg="#F1948A", command=delete)
delete.place(relx=0.609, rely=0.429, height=24, width=97)

get = Button(reservRoot, text="Get Reservation", font=(
    "calibri", 10), bg="#BB8FCE", command=get)
get.place(relx=0.751, rely=0.429, height=24, width=97)

'''SERVICE OPERATION BUTTONS'''
addService = Button(reservRoot, text="Add Service", font=(
    "calibri", 10), bg="#caffb3", command=addService)
addService.place(relx=0.389, rely=0.336, height=24, width=84)

deleteService = Button(reservRoot, text="Delete Service", font=(
    "calibri", 10), bg="#ffaeae", command=deleteService)
deleteService.place(relx=0.518, rely=0.336, height=24, width=84)

getService = Button(reservRoot, text="Get Services", font=(
    "calibri", 10), bg="#b3ecff", command=serv_list)
getService.place(relx=0.777, rely=0.075, height=24, width=74)

'''LIST OUTPUT'''

extra_services = Label(reservRoot, text="Extra Services: ", font=("calibri", 9))
extra_services.place(relx=0.246, rely=0.149, height=21, width=83)

service_list = ttk.Treeview(reservRoot, height=10, columns=5)
service_list.grid(row=4, column=0, columnspan=2)

service_list.configure(columns="Col1 Col2")
service_list.heading("#0", text='ID', anchor=N)
service_list.column("#0", width='50', stretch=NO)
service_list.heading("Col1", text='Service', anchor=N)
service_list.column("Col1", width='100')
service_list.heading("Col2", text='Price (₺)', anchor=N)
service_list.column("Col2", width='75')

service_list.place(relx=0.363, rely=0.149, relheight=0.181, relwidth=0.306)

reservation = Label(reservRoot, text="Reservation Table", font=("calibri", 9))
reservation.place(relx=0.518, rely=0.504, height=21, width=98)

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

reservation_list.place(relx=0.259, rely=0.56, relheight=0.274
                , relwidth=0.667)
reserv_list()

tk.mainloop()
