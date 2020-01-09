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


orgRoot = tk.Tk()
orgRoot.geometry("725x552+248+111")
orgRoot.minsize(120, 1)
orgRoot.maxsize(1370, 749)
orgRoot.resizable(1, 1)
orgRoot.configure(background='#EBEDEF')
orgRoot.title("Hotel Organization Page")


def add():
    name = e_name.get()
    price = e_price.get()
    info = e_info.get("1.0", END)

    if(name == "" or price == "" or info == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addOrganization('" + name +
                       "'," + info + ",'" + price + "')")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        org_list()

        e_name.delete(0, "end")
        e_info.delete('1.0', END)
        e_price.delete(0, "end")

        con.close()


def update():
    org_id = e_org_id.get()
    name = e_name.get()
    price = e_price.get()
    info = e_info.get("1.0", END)

    if(org_id == "" or name == "" or price == "" or info == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from organization where id = " + org_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_org_id.delete(0, "end")

        else:
            cursor.execute("Call updateOrganization('" + org_id +
                           "','" + name + "','" + price + "','" + info + "')")

            Messagebox.showinfo("Update Status", "Updated Succesfully")
            con.commit()
            org_list()

        e_name.delete(0, "end")
        e_info.delete('1.0', END)
        e_price.delete(0, "end")

        con.close()


def delete():
    org_id = e_org_id.get()
    if(org_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from organization where id = " + org_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_org_id.delete(0, "end")

        else:
            cursor.execute("Call deleteOrganization(" + org_id + ")")

            e_org_id.delete(0, "end")
            e_name.delete(0, "end")
            e_info.delete('1.0', END)
            e_price.delete(0, "end")

            Messagebox.showinfo("Delete Status", "Delete Succesfully")
            con.commit()
            org_list()

        con.close()


def org_list():
    records = organization_list.get_children()
    for element in records:
        organization_list.delete(element)

    con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("select * from organization order by id asc")
    organization = cursor.fetchall()

    for org in organization:
        organization_list.insert(
            '', 0, text=org[0], value=(org[1], org[2], org[3]))

    con.close()


def get():
    e_name.delete(0, "end")
    e_price.delete(0, "end")
    e_info.delete('1.0', END)

    org_id = e_org_id.get()
    if(org_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from organization where id = " + org_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_org_id.delete(0, "end")

        else:
            cursor.execute(
                "select * from organization where id = " + org_id + "")
            customer = cursor.fetchall()

            for cust in customer:
                e_name.insert(0, cust[1])
                e_info.insert(INSERT, cust[2])
                e_price.insert(0, cust[3])

            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")

        con.close()


'''SIDE BAR'''
employee = Button(orgRoot, text="EMPLOYEES", font=(
    "calibri", 10), bg="#FEF9E7")
employee.place(relx=0.028, rely=0.091, height=24, width=127)

room = Button(orgRoot, text="ROOMS", font=(
    "calibri", 10), bg="#FEF9E7")
room.place(relx=0.028, rely=0.163, height=24, width=127)

extra_services = Button(orgRoot, text="EXTRA SERVICES", font=(
    "calibri", 10), bg="#FEF9E7")
extra_services.place(relx=0.028, rely=0.236, height=24, width=127)

organizations = Button(orgRoot, text="ORGANIZATIONS", font=(
    "calibri", 10), bg="#F1C40F")
organizations.place(relx=0.028, rely=0.308, height=24, width=127)

TSeparator1 = ttk.Separator(orgRoot)
TSeparator1.place(relx=0.234, rely=0.036, relheight=0.761)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(orgRoot)
TSeparator2.place(relx=0.262, rely=0.326, relwidth=0.607)

'''INPUT TEXTS'''
org_id = Label(orgRoot, text="ID: ", font=("calibri", 9))
org_id.place(relx=0.276, rely=0.091, height=21, width=23)

e_org_id = Entry(orgRoot)
e_org_id.place(relx=0.317, rely=0.091, height=20, relwidth=0.033)

name = Label(orgRoot, text="Name: ", font=("calibri", 9))
name.place(relx=0.359, rely=0.091, height=21, width=44)

e_name = Entry(orgRoot)
e_name.place(relx=0.428, rely=0.091, height=20, relwidth=0.309)

price = Label(orgRoot, text="Price: ", font=("calibri", 9))
price.place(relx=0.735, rely=0.091, height=21, width=38)

e_price = Entry(orgRoot)
e_price.place(relx=0.786, rely=0.091, height=20, relwidth=0.061)

info = Label(orgRoot, text="Information: ", font=("calibri", 9))
info.place(relx=0.276, rely=0.145, height=21, width=75)

e_info = Text(orgRoot, font=("calibri", 9))
e_info.place(relx=0.386, rely=0.145, relheight=0.08, relwidth=0.461)

'''OPERATION BUTTONS'''
add = Button(orgRoot, text="Add", font=(
    "calibri", 10), bg="#7DCEA0", command=add)
add.place(relx=0.303, rely=0.254, height=24, width=97)

update = Button(orgRoot, text="Update", font=(
    "calibri", 10), bg="#5DADE2", command=update)
update.place(relx=0.441, rely=0.254, height=24, width=99)

delete = Button(orgRoot, text="Delete", font=(
    "calibri", 10), bg="#F1948A", command=delete)
delete.place(relx=0.579, rely=0.254, height=24, width=97)

get = Button(orgRoot, text="Get Organization", font=(
    "calibri", 10), bg="#BB8FCE", command=get)
get.place(relx=0.717, rely=0.254, height=24, width=100)

'''LIST OUTPUT'''
organization = Label(orgRoot, text="Customer Table", font=("calibri", 9))
organization.place(relx=0.483, rely=0.344, height=21, width=105)

organization_list = ttk.Treeview(orgRoot, height=10, columns=5)
organization_list.grid(row=4, column=0)

organization_list.configure(columns="Col1 Col2 Col3")
organization_list.heading("#0", text='ID', anchor=N)
organization_list.column("#0", width='50', stretch=NO)
organization_list.heading("Col1", text='Name', anchor=N)
organization_list.column("Col1", minwidth='60', width='80', stretch=NO)
organization_list.heading("Col2", text='Information', anchor=N)
organization_list.column("Col2", minwidth='150', width='200', stretch=YES)
organization_list.heading("Col3", text='Price (₺)', anchor=N)
organization_list.column("Col3", width='50', stretch=NO)

organization_list.place(relx=0.276, rely=0.38, relheight=0.375, relwidth=0.588)
org_list()

tk.mainloop()
