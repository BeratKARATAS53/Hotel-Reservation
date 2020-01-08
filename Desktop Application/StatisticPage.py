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

statRoot = tk.Tk()
statRoot.geometry("871x498+189+104")
statRoot.minsize(120, 1)
statRoot.maxsize(1370, 749)
statRoot.resizable(1, 1)
statRoot.title("Table Statistics Page")
statRoot.configure(background='#EBEDEF')


def mainPage():
    import HotelPage


def reservationPage():
    import ReservationPage


def customerPage():
    import CustomerPage


def rows_list():
    records1 = numberofRows_list.get_children()
    for element1 in records1:
        numberofRows_list.delete(element1)

    records2 = totalsize_list.get_children()
    for element2 in records2:
        totalsize_list.delete(element2)

    con = mysql.connect(host="localhost", user="admin",
                        password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()

    cursor.execute(
        "SELECT count(table_name) FROM information_schema.tables WHERE table_schema ='hotel_reservation'")
    countTable = cursor.fetchall()

    cursor.execute(
        "SELECT table_name, table_rows FROM information_schema.tables WHERE table_schema = 'hotel_reservation' ORDER BY table_rows ASC")
    numberofRows = cursor.fetchall()

    cursor.execute("SELECT table_schema AS `Database`, table_name AS `Table`, round(((data_length + index_length) / 1024), 2) `Size in KB` FROM information_schema.TABLES WHERE table_schema ='hotel_reservation' ORDER BY (data_length + index_length) ASC")
    tablesize = cursor.fetchall()

    s_countTable.insert(0, countTable)

    for rows in numberofRows:
        numberofRows_list.insert('', 0, text=rows[0], value=rows[1])

    for size in tablesize:
        totalsize_list.insert('', 0, text=size[1], value=size[2])

    con.close()


'''SIDE BAR'''
hotel = Button(statRoot, text="HOTEL", font=(
    "calibri", 10), bg="#FEF9E7", command=mainPage)
hotel.place(relx=0.023, rely=0.08, height=24, width=147)

customer = Button(statRoot, text="CUSTOMER", font=(
    "calibri", 10), bg="#FEF9E7", command=customerPage)
customer.place(relx=0.023, rely=0.161, height=24, width=147)

reservation = Button(statRoot, text="RESERVATION", font=(
    "calibri", 10), bg="#FEF9E7", command=reservationPage)
reservation.place(relx=0.023, rely=0.241, height=24, width=147)

statistics = Button(statRoot, text="TABLE STATISTICS", font=(
    "calibri", 10), bg="#F1C40F")
statistics.place(relx=0.023, rely=0.321, height=24, width=147)

TSeparator1 = ttk.Separator(statRoot)
TSeparator1.place(relx=0.207, rely=0.04, relheight=0.602)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(statRoot)
TSeparator2.place(relx=0.218, rely=0.1, relwidth=0.723)

TSeparator3_1 = ttk.Separator(statRoot)
TSeparator3_1.place(relx=0.402, rely=0.12, relheight=0.522)
TSeparator3_1.configure(orient="vertical")

TSeparator3_2 = ttk.Separator(statRoot)
TSeparator3_2.place(relx=0.689, rely=0.12, relheight=0.522)
TSeparator3_2.configure(orient="vertical")

'''INPUT TEXTS'''
statisticLabel = Label(
    statRoot, text="Statistics of All Tables & Views ", font=("calibri", 9))
statisticLabel.place(relx=0.475, rely=0.06, height=21, width=175)

countTable = Label(
    statRoot, text="Count of Tables & Views", font=("calibri", 9))
countTable.place(relx=0.22, rely=0.161, height=21, width=155)

s_countTable = Entry(statRoot)
s_countTable.place(relx=0.287, rely=0.201, height=20, relwidth=0.051)

'''LIST OUTPUT'''
numberofRows = Label(
    statRoot, text="Number of Rows in Each Table & Views", font=("calibri", 9))
numberofRows.place(relx=0.425, rely=0.141, height=21, width=218)

numberofRows_list = ttk.Treeview(statRoot, height=10, columns=2)
numberofRows_list.grid(row=4, column=0)

numberofRows_list.configure(columns="Col1")
numberofRows_list.heading("#0", text='Table Name', anchor=N)
numberofRows_list.column("#0", width='125')
numberofRows_list.heading("Col1", text='Table Rows', anchor=N)
numberofRows_list.column("Col1", width='100')

numberofRows_list.place(relx=0.425, rely=0.201,
                        relheight=0.416, relwidth=0.257)

totalsizeLabel = Label(
    statRoot, text="Total Size of All Tables & Views", font=("calibri", 9))
totalsizeLabel.place(relx=0.725, rely=0.141, height=21, width=175)

totalsize_list = ttk.Treeview(statRoot, height=10, columns=2)
totalsize_list.grid(row=4, column=0)

totalsize_list.configure(columns="Col1")
totalsize_list.heading("#0", text='Table Name', anchor=N)
totalsize_list.column("#0", width='125')
totalsize_list.heading("Col1", text='Table Size (KB)', anchor=N)
totalsize_list.column("Col1", width='100')

totalsize_list.place(relx=0.7, rely=0.201, relheight=0.416, relwidth=0.25)

rows_list()

tk.mainloop()
