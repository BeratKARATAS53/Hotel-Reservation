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

staffRoot = tk.Tk()
staffRoot.geometry("1007x634+99+96")
staffRoot.minsize(120, 1)
staffRoot.maxsize(1370, 749)
staffRoot.resizable(1, 1)
staffRoot.title("Hotel Employees Page")


def organizationPage():
    import OrganizationPage


def extraServicePage():
    import ExtraServicePage


def roomPage():
    import HotelRoomPage


'''SIDE BAR'''
employee = Button(staffRoot, text="EMPLOYEES", font=(
    "calibri", 10), bg="#80ff00")
employee.place(relx=0.028, rely=0.091, height=24, width=127)

room = Button(staffRoot, text="ROOMS", font=(
    "calibri", 10), bg="#d9d9d9", command=roomPage)
room.place(relx=0.028, rely=0.163, height=24, width=127)

extra_services = Button(staffRoot, text="EXTRA SERVICES", font=(
    "calibri", 10), bg="#d9d9d9", command=extraServicePage)
extra_services.place(relx=0.028, rely=0.236, height=24, width=127)

organizations = Button(staffRoot, text="ORGANIZATIONS", font=(
    "calibri", 10), bg="#d9d9d9", command=organizationPage)
organizations.place(relx=0.028, rely=0.308, height=24, width=127)

TSeparator1 = ttk.Separator(staffRoot)
TSeparator1.place(relx=0.179, rely=0.032, relheight=0.82)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(staffRoot)
TSeparator2.place(relx=0.188, rely=0.354, relwidth=0.780)

'''INPUT TEXTS'''
emp_id = Label(staffRoot, text="ID: ", font=("calibri", 9))
emp_id.place(relx=0.201, rely=0.065, height=21, width=24)

e_emp_id = Entry(staffRoot)
e_emp_id.place(relx=0.236, rely=0.065, height=20, relwidth=0.039)

firstname = Label(staffRoot, text="First Name: ", font=("calibri", 9))
firstname.place(relx=0.285, rely=0.065, height=21, width=69)

e_firstname = Entry(staffRoot)
e_firstname.place(relx=0.360, rely=0.065, height=20, relwidth=0.150)

lastname = Label(staffRoot, text="Last Name: ", font=("calibri", 9))
lastname.place(relx=0.520, rely=0.065, height=21, width=68)

e_lastname = Entry(staffRoot)
e_lastname.place(relx=0.600, rely=0.065, height=20, relwidth=0.150)

telephone = Label(staffRoot, text="Phone: ", font=("calibri", 9))
telephone.place(relx=0.760, rely=0.065, height=21, width=46)

e_telephone = Entry(staffRoot)
e_telephone.place(relx=0.810, rely=0.065, height=20, relwidth=0.130)

email = Label(staffRoot, text="Email: ", font=("calibri", 9))
email.place(relx=0.201, rely=0.113, height=21, width=41)

e_email = Entry(staffRoot)
e_email.place(relx=0.256, rely=0.113, height=20, relwidth=0.254)

passwrd = Label(staffRoot, text="Password: ", font=("calibri", 9))
passwrd.place(relx=0.520, rely=0.113, height=19, width=60)

e_password = Entry(staffRoot)
e_password.place(relx=0.585, rely=0.113, height=20, relwidth=0.110)

confirm_passwrd = Label(staffRoot, text="Confirm Password: ", font=("calibri", 9))
confirm_passwrd.place(relx=0.700, rely=0.113, height=21, width=109)

e_confirm_passwrd = Entry(staffRoot)
e_confirm_passwrd.place(relx=0.810, rely=0.113, height=20, relwidth=0.130)

address = Label(staffRoot, text="Address: ", font=("calibri", 9))
address.place(relx=0.201, rely=0.160, height=21, width=54)

e_address = Text(staffRoot)
e_address.place(relx=0.256, rely=0.160, relheight=0.100, relwidth=0.35)

salary = Label(staffRoot, text=" Salary: ", font=("calibri", 9))
salary.place(relx=0.610, rely=0.161, height=21, width=40)

e_salary = Entry(staffRoot)
e_salary.place(relx=0.660, rely=0.161, height=20, relwidth=0.049)

'''COMBOBOX'''
emp_type = Label(staffRoot, text="Employee Type: ", font=("calibri", 9))
emp_type.place(relx=0.720, rely=0.158, height=21, width=90)

box_value = StringVar()
e_emp_type = ttk.Combobox(
    staffRoot, textvariable=box_value, state='readonly')
e_emp_type.place(relx=0.810, rely=0.158, relheight=0.033, relwidth=0.130)

e_emp_type['values'] = ('Normal', 'Termal', 'Bungalow')
e_emp_type.current(0)

'''OPERATION BUTTONS'''
add = Button(staffRoot, text="Add", font=(
    "calibri", 10), bg="#d9d9d9")
add.place(relx=0.337, rely=0.291, height=24, width=97)

update = Button(staffRoot, text="Update", font=(
    "calibri", 10), bg="#d9d9d9")
update.place(relx=0.437, rely=0.291, height=24, width=99)

delete = Button(staffRoot, text="Delete", font=(
    "calibri", 10), bg="#d9d9d9")
delete.place(relx=0.536, rely=0.291, height=24, width=97)

get = Button(staffRoot, text="Get Employee", font=(
    "calibri", 10), bg="#d9d9d9")
get.place(relx=0.635, rely=0.291, height=24, width=97)

'''LIST OUTPUT'''
manager = Label(staffRoot, text="Manager Table", font=("Comic Sans MC", 9))
manager.place(relx=0.480, rely=0.36, height=31, width=90)

manager_list = ttk.Treeview(staffRoot, height=10, columns=5)
manager_list.grid(row=4, column=0)

manager_list.place(relx=0.189, rely=0.415, relheight=0.18, relwidth=0.700)

emp = Label(staffRoot, text="Employee Table", font=("Comic Sans MC", 9))
emp.place(relx=0.480, rely=0.60, height=31, width=90)

emp_list = ttk.Treeview(staffRoot, height=10, columns=5)
emp_list.grid(row=4, column=0)

emp_list.place(relx=0.189, rely=0.66, relheight=0.18, relwidth=0.700)
tk.mainloop()
