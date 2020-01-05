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

hotelRoomRoot = tk.Tk()
hotelRoomRoot.geometry("1007x634+99+96")
hotelRoomRoot.minsize(120, 1)
hotelRoomRoot.maxsize(1370, 749)
hotelRoomRoot.resizable(1, 1)
hotelRoomRoot.title("Hotel Room Page")


def organizationPage():
    import OrganizationPage


def employeePage():
    import EmployeeManagerPage


def extraServicePage():
    import ExtraServicePage


'''SIDE BAR'''
employee = Button(hotelRoomRoot, text="EMPLOYEES", font=(
    "bold", 10), bg="#d9d9d9", command=employeePage)
employee.place(relx=0.028, rely=0.091, height=24, width=127)

room = Button(hotelRoomRoot, text="ROOMS", font=(
    "bold", 10), bg="#80ff00")
room.place(relx=0.028, rely=0.163, height=24, width=127)

extra_services = Button(hotelRoomRoot, text="EXTRA SERVICES", font=(
    "bold", 10), bg="#d9d9d9", command=extraServicePage)
extra_services.place(relx=0.028, rely=0.236, height=24, width=127)

organizations = Button(hotelRoomRoot, text="ORGANIZATIONS", font=(
    "bold", 10), bg="#d9d9d9", command=organizationPage)
organizations.place(relx=0.028, rely=0.308, height=24, width=127)

TSeparator1 = ttk.Separator(hotelRoomRoot)
TSeparator1.place(relx=0.179, rely=0.032, relheight=0.82)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(hotelRoomRoot)
TSeparator2.place(relx=0.188, rely=0.284, relwidth=0.635)

'''INPUT TEXTS'''
hotel_id = Label(hotelRoomRoot, text="ID: ", font=("bold", 9))
hotel_id.place(relx=0.199, rely=0.063, height=21, width=23)

e_hotel_id = Entry(hotelRoomRoot)
e_hotel_id.place(relx=0.228, rely=0.063, height=20, relwidth=0.034)

room_info = Label(hotelRoomRoot, text="Room Info: ", font=("bold", 9))
room_info.place(relx=0.275, rely=0.063, height=21, width=68)

e_room_info = Entry(hotelRoomRoot)
e_room_info.place(relx=0.348, rely=0.063, relheight=0.08, relwidth=0.330)

price = Label(hotelRoomRoot, text="Price: ", font=("bold", 9))
price.place(relx=0.690, rely=0.063, height=21, width=38)

e_price = Entry(hotelRoomRoot)
e_price.place(relx=0.740, rely=0.063, height=20, relwidth=0.120)


capacity = Label(hotelRoomRoot, text="Capacity: ", font=("bold", 9))
capacity.place(relx=0.460, rely=0.158, height=21, width=58)

e_capacity = Text(hotelRoomRoot)
e_capacity.place(relx=0.520, rely=0.158, height=20, relwidth=0.044)

room_number = Label(hotelRoomRoot, text="Room Number: ", font=("bold", 9))
room_number.place(relx=0.570, rely=0.158, height=21, width=91)

e_room_number = Text(hotelRoomRoot)
e_room_number.place(relx=0.660, rely=0.158, height=20, relwidth=0.044)

'''COMBOBOX'''

status = Label(hotelRoomRoot, text="Status: ", font=("bold", 9))
status.place(relx=0.258, rely=0.158, height=21, width=44)

box_value = StringVar()
e_status = ttk.Combobox(
    hotelRoomRoot, textvariable=box_value, state='readonly')
e_status.place(relx=0.310, rely=0.158, relheight=0.033, relwidth=0.142)

e_status['values'] = ('Normal', 'Termal', 'Bungalow')
e_status.current(0)

room_type = Label(hotelRoomRoot, text="Room Type: ", font=("bold", 9))
room_type.place(relx=0.705, rely=0.158, height=21, width=72)

box_value = StringVar()
e_room_type = ttk.Combobox(
    hotelRoomRoot, textvariable=box_value, state='readonly')
e_room_type.place(relx=0.780, rely=0.158, relheight=0.033, relwidth=0.082)

e_room_type['values'] = ('Normal', 'Termal', 'Bungalow')
e_room_type.current(0)


'''OPERATION BUTTONS'''
add = Button(hotelRoomRoot, text="Add", font=(
    "italic", 10), bg="#d9d9d9")
add.place(relx=0.337, rely=0.221, height=24, width=97)

update = Button(hotelRoomRoot, text="Update", font=(
    "italic", 10), bg="#d9d9d9")
update.place(relx=0.437, rely=0.221, height=24, width=99)

delete = Button(hotelRoomRoot, text="Delete", font=(
    "italic", 10), bg="#d9d9d9")
delete.place(relx=0.536, rely=0.221, height=24, width=97)

get = Button(hotelRoomRoot, text="Get Room", font=(
    "italic", 10), bg="#d9d9d9")
get.place(relx=0.635, rely=0.221, height=24, width=97)

'''LIST OUTPUT'''
rooms = Label(hotelRoomRoot, text="Room Table", font=("Comic Sans MC", 9))
rooms.place(relx=0.480, rely=0.29, height=31, width=66)

room_list = ttk.Treeview(hotelRoomRoot, height=10, columns=5)
room_list.grid(row=4, column=0)

room_list.place(relx=0.189, rely=0.340, relheight=0.38, relwidth=0.600)

tk.mainloop()
