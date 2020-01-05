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


def organizationPage():
    import OrganizationPage


def roomPage():
    import HotelRoomPage


def employeePage():
    import EmployeeManagerPage


'''SIDE BAR'''
employee = Button(ServiceRoot, text="EMPLOYEES", font=(
    "bold", 10), bg="#d9d9d9",  command=employeePage)
employee.place(relx=0.028, rely=0.091, height=24, width=127)

room = Button(ServiceRoot, text="ROOMS", font=(
    "bold", 10), bg="#d9d9d9", command=roomPage)
room.place(relx=0.028, rely=0.163, height=24, width=127)

extra_services = Button(ServiceRoot, text="EXTRA SERVICES", font=(
    "bold", 10), bg="#80ff00")
extra_services.place(relx=0.028, rely=0.236, height=24, width=127)

organizations = Button(ServiceRoot, text="ORGANIZATIONS", font=(
    "bold", 10), bg="#d9d9d9", command=organizationPage)
organizations.place(relx=0.028, rely=0.308, height=24, width=127)

TSeparator1 = ttk.Separator(ServiceRoot)
TSeparator1.place(relx=0.179, rely=0.032, relheight=0.82)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(ServiceRoot)
TSeparator2.place(relx=0.188, rely=0.320, relwidth=0.800)

TSeparator3 = ttk.Separator(ServiceRoot)
TSeparator3.place(relx=0.585, rely=0.032, relheight=0.82)
TSeparator3.configure(orient="vertical")

'''INPUT TEXTS'''

ex = Label(ServiceRoot, text="Extra Service", font=("bold", 10))
ex.place(relx=0.350, rely=0.031, height=20, width=90)

ex_id = Label(ServiceRoot, text="ID: ", font=("bold", 9))
ex_id.place(relx=0.199, rely=0.091, height=20, width=23)

e_ex_id = Entry(ServiceRoot)
e_ex_id.place(relx=0.228, rely=0.091, height=20, relwidth=0.034)

service_id = Label(ServiceRoot, text="Service: ", font=("bold", 9))
service_id.place(relx=0.270, rely=0.091, height=20, width=50)

e_service_id = Entry(ServiceRoot)
e_service_id.place(relx=0.320, rely=0.091, height=20, relwidth=0.240)

extPrice_id = Label(ServiceRoot, text="Service Price : ", font=("bold", 9))
extPrice_id.place(relx=0.270, rely=0.14, height=20, width=90)

e_extPrice_id = Entry(ServiceRoot)
e_extPrice_id.place(relx=0.355, rely=0.14, height=20, relwidth=0.085)

extPoint_id = Label(ServiceRoot, text="Service Point : ", font=("bold", 9))
extPoint_id.place(relx=0.440, rely=0.14, height=20, width=90)

e_extPoint_id = Entry(ServiceRoot)
e_extPoint_id.place(relx=0.525, rely=0.14, height=20, relwidth=0.035)

'''INPUT TEXTS'''

ex = Label(ServiceRoot, text="Food Service", font=("bold", 10))
ex.place(relx=0.760, rely=0.031, height=21, width=90)

food_id = Label(ServiceRoot, text="ID: ", font=("bold", 9))
food_id.place(relx=0.610, rely=0.091, height=21, width=23)

e_food_id = Entry(ServiceRoot)
e_food_id.place(relx=0.635, rely=0.091, height=20, relwidth=0.034)

food_service_id = Label(ServiceRoot, text="Service: ", font=("bold", 9))
food_service_id.place(relx=0.680, rely=0.091, height=20, width=50)

e_food_service_id = Entry(ServiceRoot)
e_food_service_id.place(relx=0.730, rely=0.091, height=20, relwidth=0.240)

foodPrice_id = Label(ServiceRoot, text="Service Price : ", font=("bold", 9))
foodPrice_id.place(relx=0.675, rely=0.14, height=20, width=90)

e_foodPrice_id = Entry(ServiceRoot)
e_foodPrice_id.place(relx=0.770, rely=0.14, height=20, relwidth=0.085)

foodPoint_id = Label(ServiceRoot, text="Service Point : ", font=("bold", 9))
foodPoint_id.place(relx=0.850, rely=0.14, height=20, width=90)

e_foodPoint_id = Entry(ServiceRoot)
e_foodPoint_id.place(relx=0.935, rely=0.14, height=20, relwidth=0.035)

foodDetail_id = Label(ServiceRoot, text="Food Detail : ", font=("bold", 9))
foodDetail_id.place(relx=0.675, rely=0.19, height=20, width=90)

e_foodDetail_id = Entry(ServiceRoot)
e_foodDetail_id.place(relx=0.770, rely=0.19, height=20, relwidth=0.200)

'''OPERATION BUTTONS'''
ext_add = Button(ServiceRoot, text="Add", font=(
    "italic", 10), bg="#d9d9d9")
ext_add.place(relx=0.228, rely=0.250, height=24, width=80)

ext_update = Button(ServiceRoot, text="Update", font=(
    "italic", 10), bg="#d9d9d9")
ext_update.place(relx=0.310, rely=0.250, height=24, width=80)

ext_delete = Button(ServiceRoot, text="Delete", font=(
    "italic", 10), bg="#d9d9d9")
ext_delete.place(relx=0.391, rely=0.250, height=24, width=80)

ext_get = Button(ServiceRoot, text="Get Extra", font=(
    "italic", 10), bg="#d9d9d9")
ext_get.place(relx=0.474, rely=0.250, height=24, width=85)

'''OPERATION BUTTONS'''
food_add = Button(ServiceRoot, text="Add", font=(
    "italic", 10), bg="#d9d9d9")
food_add.place(relx=0.635, rely=0.250, height=24, width=80)

food_update = Button(ServiceRoot, text="Update", font=(
    "italic", 10), bg="#d9d9d9")
food_update.place(relx=0.717, rely=0.250, height=24, width=80)

food_delete = Button(ServiceRoot, text="Delete", font=(
    "italic", 10), bg="#d9d9d9")
food_delete.place(relx=0.798, rely=0.250, height=24, width=80)

food_get = Button(ServiceRoot, text="Get Extra", font=(
    "italic", 10), bg="#d9d9d9")
food_get.place(relx=0.880, rely=0.250, height=24, width=85)

'''LIST OUTPUT'''
ext_serv = Label(ServiceRoot, text="Extra Service Table",
                 font=("Comic Sans MC", 9))
ext_serv.place(relx=0.280, rely=0.33, height=31, width=140)

ext_serv_list = ttk.Treeview(ServiceRoot, height=10, columns=5)
ext_serv_list.grid(row=4, column=0)

ext_serv_list.place(relx=0.189, rely=0.380, relheight=0.38, relwidth=0.370)


'''LIST OUTPUT'''
food_serv = Label(ServiceRoot, text="Food Service Table",
                  font=("Comic Sans MC", 9))
food_serv.place(relx=0.610, rely=0.33, height=31, width=140)

food_serv_list = ttk.Treeview(ServiceRoot, height=10, columns=5)
food_serv_list.grid(row=4, column=0)

food_serv_list.place(relx=0.610, rely=0.380, relheight=0.38, relwidth=0.370)

tk.mainloop()
