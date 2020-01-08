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

ServiceRoot = tk.Tk()
ServiceRoot.geometry("1007x634+99+96")
ServiceRoot.minsize(120, 1)
ServiceRoot.maxsize(1370, 749)
ServiceRoot.resizable(1, 1)
ServiceRoot.title("Room Extra Service Page")
ServiceRoot.configure(background='#EBEDEF')


def organizationPage():
    import OrganizationPage


def roomPage():
    import HotelRoomPage


def employeePage():
    import EmployeeManagerPage

def addExtra():
    service = e_service.get()
    extPrice = e_extPrice.get()
    extPoint = e_extPoint.get()
    hotel_id = e_ex_hotel_id.get()

    if(service == "" or extPrice == "" or extPoint == "" or hotel_id == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addExtraservice('" + service + "','" + extPrice + "','" + 
                        extPoint + "','" + hotel_id + "', @service_id)")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        ext_list()

        e_service.delete(0, "end")
        e_extPrice.delete(0, "end")
        e_extPoint.delete(0, 1)
        e_ex_hotel_id.delete(0, "end")

        con.close()


def addFood():
    foodService = e_food_service.get()
    foodPrice = e_foodPrice.get()
    foodPoint = e_foodPoint.get()
    foodDetail = e_foodDetail.get()
    f_hotel_id = e_fd_hotel_id.get()

    if(foodService == "" or foodPrice == "" or foodPoint == "" or foodDetail == "" or f_hotel_id == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addFoodservice('" + foodService + "','" + foodPrice + "','" + 
                        foodPoint + "','" + foodDetail + "','" + f_hotel_id + "')")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        food_list()

        e_food_service.delete(0, "end")
        e_foodPrice.delete(0, "end")
        e_foodPoint.delete(0, 1)
        e_foodDetail.delete(0, "end")
        e_fd_hotel_id.delete(0, "end")

        con.close()


def updateExtra():
    ex_id = e_ex_id.get()
    service = e_service.get()
    extPrice = e_extPrice.get()
    extPoint = e_extPoint.get()
    hotel_id = e_ex_hotel_id.get()

    if(ex_id == "" or service == "" or extPrice == "" or extPoint == "" or hotel_id == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call addUpdaeextraservice('" + ex_id + "','" + service + "','" + extPrice + "','" + 
                        extPoint + "','" + hotel_id + "', @service_id)")

        Messagebox.showinfo("Update Status", "Updated Succesfully")
        con.commit()
        ext_list()

        e_ex_id.delete(0, "end")
        e_service.delete(0, "end")
        e_extPrice.delete(0, "end")
        e_extPoint.delete(0, 1)
        e_ex_hotel_id.delete(0, "end")

        con.close()


def updateFood():
    food = e_food.get()
    foodService = e_food_service.get()
    foodPrice = e_foodPrice.get()
    foodPoint = e_foodPoint.get()
    foodDetail = e_foodDetail.get()
    f_hotel_id = e_fd_hotel_id.get()

    if(food == "" or foodService == "" or foodPrice == "" or foodPoint == "" or foodDetail == "" or f_hotel_id == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("Call updateFoodservice('" + food + "','" + foodService + "','" + foodPrice + "','" + 
                        foodPoint + "','" + foodDetail + "','" + f_hotel_id + "')")

        Messagebox.showinfo("Update Status", "Updated Succesfully")
        con.commit()
        food_list()

        e_food.delete(0, "end")
        e_food_service.delete(0, "end")
        e_foodPrice.delete(0, "end")
        e_foodPoint.delete(0, 1)
        e_foodDetail.delete(0, "end")
        e_fd_hotel_id.delete(0, "end")

        con.close()


def deleteExtra():
    ex_id = e_ex_id.get()

    if(ex_id == ""):
        Messagebox.showinfo("Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()

        cursor.execute(
            "select exists (select * from extraservice where id = " + ex_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            ex_id.delete(0, "end")

        else:
            cursor.execute("Call deleteextraservice(" + ex_id + ")")

            e_ex_id.delete(0, "end")
            e_service.delete(0, "end")
            e_extPrice.delete(0, "end")
            e_extPoint.delete(0, 1)
            e_ex_hotel_id.delete(0, "end")

            Messagebox.showinfo("Delete Status", "Deleted Succesfully")
            con.commit()
            ext_list()
            food_list()

            con.close()


def deleteFood():
    food = e_food.get()

    if(food == ""):
        Messagebox.showinfo("Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()

        cursor.execute(
            "select exists (select * from foodservice where id = " + food + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            food.delete(0, "end")
        
        else:
            cursor.execute("Call deletefoodservice(" + food + ")")

            e_food.delete(0, "end")
            e_food_service.delete(0, "end")
            e_foodPrice.delete(0, "end")
            e_foodPoint.delete(0, 1)
            e_foodDetail.delete(0, "end")
            e_fd_hotel_id.delete(0, "end")

            Messagebox.showinfo("Delete Status", "Deleted Succesfully")
            con.commit()
            food_list()
            ext_list()

            con.close()


def getExtra():
    e_service.delete(0, "end")
    e_extPrice.delete(0, "end")
    e_extPoint.delete(0, 1)
    e_ex_hotel_id.delete(0, "end")

    ex_id = e_ex_id.get()
    if(ex_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from extraservice where id = " + ex_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_ex_id.delete(0, "end")

        else:
            cursor.execute(
                "select * from extraservice where id = " + ex_id + "")
            extras = cursor.fetchall()

            for extra in extras:
                e_service.insert(0, extra[1])
                e_extPrice.insert(0, extra[2])
                e_extPoint.insert(0, extra[3])
                e_ex_hotel_id.insert(0, extra[4])

            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")
            con.close()


def getFood():
    e_food_service.delete(0, "end")
    e_foodPrice.delete(0, "end")
    e_foodPoint.delete(0, 1)
    e_foodDetail.delete(0, "end")
    e_fd_hotel_id.delete(0, "end")

    food = e_food.get()
    if(food == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from foodservice where id = " + food + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_food.delete(0, "end")

        else:
            cursor.execute(
                "select * from extraservice e, foodservice f where e.id = f.service_id and f.id = " + food + "")
            foods = cursor.fetchall()

            for food in foods:
                e_food_service.insert(0, food[1])
                e_foodPrice.insert(0, food[2])
                e_foodPoint.insert(0, food[3])
                e_foodDetail.insert(0, food[6])
                e_fd_hotel_id.insert(0, food[4])

            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")
            con.close()


def ext_list():
    records = ext_serv_list.get_children()
    for element in records:
        ext_serv_list.delete(element)

    con = mysql.connect(host="localhost", user="admin",
                        password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("Select * From extraservice Order By id Asc ")
    extra_services = cursor.fetchall()

    for extra in extra_services:
        ext_serv_list.insert('', 0, text=extra[0], value=(
            extra[1], extra[2], extra[3]))

    con.close()

def food_list():
    records = food_serv_list.get_children()
    for element in records:
        food_serv_list.delete(element)

    con = mysql.connect(host="localhost", user="admin",
                        password="Berat.190797", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("Select * From extraservice e, foodservice f Where e.id=f.service_id Order By e.id Asc")
    food_services = cursor.fetchall()

    for food in food_services:
        food_serv_list.insert('', 0, text=food[5], value=(
            food[1], food[6], food[2], food[3]))

    con.close()

def update():
    emp_id = e_emp_id.get()
    firstname = e_firstname.get()
    lastname = e_lastname.get()
    passwrd = e_password.get()
    confirm_passwrd = e_confirm_passwrd.get()
    email = e_email.get()
    address = e_address.get("1.0", END)
    telephone = e_telephone.get()
    salary = e_salary.get()
    employee_type = e_emp_type.get()


    if(emp_id == "" or firstname == "" or lastname == "" or passwrd == "" or email == "" or address == ""
            or telephone == ""  or salary == "" ):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="admin",
                            password="Berat.190797", database="hotel_reservation")
        cursor = con.cursor()
        if ( employee_type == "manager"):
            cursor.execute("select exists (select * from manager_all_info where id = " + manager_id + ")")
        else:
            cursor.execute("select exists (select * from employee_all_info where id = " + employee_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
            e_emp_id.delete(0, "end")

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
            e_salary.delete(0, "end")


        con.close()

'''SIDE BAR'''
employee = Button(ServiceRoot, text="EMPLOYEES", font=(
    "calibri", 10), bg="#FEF9E7",  command=employeePage)
employee.place(relx=0.028, rely=0.091, height=24, width=127)

room = Button(ServiceRoot, text="ROOMS", font=(
    "calibri", 10), bg="#FEF9E7", command=roomPage)
room.place(relx=0.028, rely=0.163, height=24, width=127)

extra_services = Button(ServiceRoot, text="EXTRA SERVICES", font=(
    "calibri", 10), bg="#F1C40F")
extra_services.place(relx=0.028, rely=0.236, height=24, width=127)

organizations = Button(ServiceRoot, text="ORGANIZATIONS", font=(
    "calibri", 10), bg="#FEF9E7", command=organizationPage)
organizations.place(relx=0.028, rely=0.308, height=24, width=127)

TSeparator1 = ttk.Separator(ServiceRoot)
TSeparator1.place(relx=0.179, rely=0.032, relheight=0.82)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(ServiceRoot)
TSeparator2.place(relx=0.188, rely=0.320, relwidth=0.800)

TSeparator3 = ttk.Separator(ServiceRoot)
TSeparator3.place(relx=0.585, rely=0.032, relheight=0.82)
TSeparator3.configure(orient="vertical")

'''INPUT TEXTS FOR EXTRA'''

ex = Label(ServiceRoot, text="Extra Service", font=("calibri", 10))
ex.place(relx=0.350, rely=0.031, height=20, width=90)

ex_id = Label(ServiceRoot, text="ID: ", font=("calibri", 9))
ex_id.place(relx=0.199, rely=0.091, height=20, width=23)

e_ex_id = Entry(ServiceRoot)
e_ex_id.place(relx=0.228, rely=0.091, height=20, relwidth=0.034)

ex_hotel_id = Label(ServiceRoot, text="Hotel ID: ", font=("calibri", 9))
ex_hotel_id.place(relx=0.199, rely=0.14, height=20, width=55)

e_ex_hotel_id = Entry(ServiceRoot)
e_ex_hotel_id.place(relx=0.258, rely=0.14, height=20, relwidth=0.032)

service = Label(ServiceRoot, text="Service: ", font=("calibri", 9))
service.place(relx=0.270, rely=0.091, height=20, width=50)

e_service = Entry(ServiceRoot)
e_service.place(relx=0.320, rely=0.091, height=20, relwidth=0.240)

extPrice = Label(ServiceRoot, text="Service Price : ", font=("calibri", 9))
extPrice.place(relx=0.290, rely=0.14, height=20, width=90)

e_extPrice = Entry(ServiceRoot)
e_extPrice.place(relx=0.375, rely=0.14, height=20, relwidth=0.085)

'''SPINBOX'''
extPoint = Label(ServiceRoot, text="Service Point : ", font=("calibri", 9))
extPoint.place(relx=0.440, rely=0.14, height=20, width=90)

var = StringVar(ServiceRoot)
var.set("1")
e_extPoint = Spinbox(ServiceRoot, from_=1, to=5, textvariable=var)
e_extPoint.place(relx=0.525, rely=0.14, height=20, relwidth=0.035)

'''INPUT TEXTS FOR FOOD'''

ex = Label(ServiceRoot, text="Food Service", font=("calibri", 10))
ex.place(relx=0.760, rely=0.031, height=21, width=90)

food = Label(ServiceRoot, text="ID: ", font=("calibri", 9))
food.place(relx=0.610, rely=0.091, height=21, width=23)

e_food = Entry(ServiceRoot)
e_food.place(relx=0.635, rely=0.091, height=20, relwidth=0.034)

fd_hotel_id = Label(ServiceRoot, text="Hotel ID: ", font=("calibri", 9))
fd_hotel_id.place(relx=0.610, rely=0.14, height=20, width=55)

e_fd_hotel_id = Entry(ServiceRoot)
e_fd_hotel_id.place(relx=0.665, rely=0.14, height=20, relwidth=0.032)

food_service = Label(ServiceRoot, text="Service: ", font=("calibri", 9))
food_service.place(relx=0.680, rely=0.091, height=20, width=50)

e_food_service = Entry(ServiceRoot)
e_food_service.place(relx=0.730, rely=0.091, height=20, relwidth=0.240)

foodPrice = Label(ServiceRoot, text="Service Price : ", font=("calibri", 9))
foodPrice.place(relx=0.695, rely=0.14, height=20, width=90)

e_foodPrice = Entry(ServiceRoot)
e_foodPrice.place(relx=0.790, rely=0.14, height=20, relwidth=0.085)

foodDetail = Label(ServiceRoot, text="Food Detail : ", font=("calibri", 9))
foodDetail.place(relx=0.675, rely=0.19, height=20, width=90)

e_foodDetail = Entry(ServiceRoot)
e_foodDetail.place(relx=0.770, rely=0.19, height=20, relwidth=0.200)

'''SPINBOX'''
foodPoint = Label(ServiceRoot, text="Service Point : ", font=("calibri", 9))
foodPoint.place(relx=0.850, rely=0.14, height=20, width=90)

var = StringVar(ServiceRoot)
var.set("1")
e_foodPoint = Spinbox(ServiceRoot, from_=1, to=5, textvariable=var)
e_foodPoint.place(relx=0.935, rely=0.14, height=20, relwidth=0.035)

'''OPERATION BUTTONS FOR EXTRA'''
ext_add = Button(ServiceRoot, text="Add", font=(
    "calibri", 10), bg="#7DCEA0", command=addExtra)
ext_add.place(relx=0.228, rely=0.250, height=24, width=80)

ext_update = Button(ServiceRoot, text="Update", font=(
    "calibri", 10), bg="#5DADE2", command=updateExtra)
ext_update.place(relx=0.310, rely=0.250, height=24, width=80)

ext_delete = Button(ServiceRoot, text="Delete", font=(
    "calibri", 10), bg="#F1948A", command=deleteExtra)
ext_delete.place(relx=0.391, rely=0.250, height=24, width=80)

ext_get = Button(ServiceRoot, text="Get Extra", font=(
    "calibri", 10), bg="#BB8FCE", command=getExtra)
ext_get.place(relx=0.474, rely=0.250, height=24, width=85)

'''OPERATION BUTTONS FOR FOOD'''
food_add = Button(ServiceRoot, text="Add", font=(
    "calibri", 10), bg="#7DCEA0", command=addFood)
food_add.place(relx=0.635, rely=0.250, height=24, width=80)

food_update = Button(ServiceRoot, text="Update", font=(
    "calibri", 10), bg="#5DADE2", command=updateFood)
food_update.place(relx=0.717, rely=0.250, height=24, width=80)

food_delete = Button(ServiceRoot, text="Delete", font=(
    "calibri", 10), bg="#F1948A", command=deleteFood)
food_delete.place(relx=0.798, rely=0.250, height=24, width=80)

food_get = Button(ServiceRoot, text="Get Food", font=(
    "calibri", 10), bg="#BB8FCE", command=getFood)
food_get.place(relx=0.880, rely=0.250, height=24, width=85)

'''LIST OUTPUT FOR EXTRA'''
ext_serv = Label(ServiceRoot, text="Extra Service Table",
                 font=("calibri", 9))
ext_serv.place(relx=0.280, rely=0.33, height=31, width=140)

ext_serv_list = ttk.Treeview(ServiceRoot, height=10, columns=5)
ext_serv_list.grid(row=4, column=0)

ext_serv_list.configure(columns="Col1 Col2 Col3")
ext_serv_list.heading("#0", text='ID', anchor=N)
ext_serv_list.column("#0", width='40', stretch=NO)
ext_serv_list.heading("Col1", text='Service Name', anchor=N)
ext_serv_list.column("Col1", width='100')
ext_serv_list.heading("Col2", text='Price', anchor=N)
ext_serv_list.column("Col2", width='60', stretch=NO)
ext_serv_list.heading("Col3", text='Point', anchor=N)
ext_serv_list.column("Col3", width='40', stretch=NO)

ext_serv_list.place(relx=0.189, rely=0.380, relheight=0.38, relwidth=0.38)

ext_list()

'''LIST OUTPUT FOR FOOD'''
food_serv = Label(ServiceRoot, text="Food Service Table",
                  font=("calibri", 9))
food_serv.place(relx=0.710, rely=0.33, height=31, width=140)

food_serv_list = ttk.Treeview(ServiceRoot, height=10, columns=5)
food_serv_list.grid(row=4, column=0)

food_serv_list.configure(columns="Col1 Col2 Col3 Col4")
food_serv_list.heading("#0", text='ID', anchor=N)
food_serv_list.column("#0", width='40', stretch=NO)
food_serv_list.heading("Col1", text='Service Name', anchor=N)
food_serv_list.column("Col1", width='100')
food_serv_list.heading("Col2", text='Food Detail', anchor=N)
food_serv_list.column("Col2", width='100')
food_serv_list.heading("Col3", text='Price', anchor=N)
food_serv_list.column("Col3", width='60', stretch=NO)
food_serv_list.heading("Col4", text='Point', anchor=N)
food_serv_list.column("Col4", width='40', stretch=NO)

food_serv_list.place(relx=0.610, rely=0.380, relheight=0.38, relwidth=0.38)

food_list()

tk.mainloop()
