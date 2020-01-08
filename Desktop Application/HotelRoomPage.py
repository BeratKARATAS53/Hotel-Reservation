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
hotelRoomRoot.configure(background='#EBEDEF')
hotelRoomRoot.title("Hotel Room Page")

def organizationPage():
    import OrganizationPage

def employeePage():
    import EmployeeManagerPage

def extraServicePage():
    import ExtraServicePage

def get_rooms():
    hotel_id = e_hotel_id.get()
    
    records = room_list.get_children()
    for element in records:
        room_list.delete(element)

    con = mysql.connect(host="localhost", user="root",
                        password="12345", database="hotel_reservation")
    cursor = con.cursor()

    cursor.execute("select * from room where hotel_id='" + hotel_id + " order by id asc'")
    rooms = cursor.fetchall()

    for room in rooms:
        room_list.insert('', 0, text=room[0], value=(
            room[1], room[2], room[3], room[4], room[5]))

    con.close()

def get():
    e_hotel_id.delete(0, "end")
    e_price.delete(0, "end")
    e_capacity.delete("1.0", END)
    e_room_number.delete("1.0", END)
   

    room_id  = e_room_id.get()
    if(room_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from room where id = " + room_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_room_id.delete(0, "end")

        else:
            cursor.execute(
                "select * from room where id = " + room_id + "")
            rooms = cursor.fetchall()

            for room in rooms:
                #print(room[1],room[2],room[3],room[4],room[5],room[6])
                e_room_info.insert(INSERT, room[1])
                e_price.insert(0, room[2])
                e_status.insert(0, room[4])
                e_capacity.insert("1.0", room[5])
                e_room_number.insert("1.0", room[3])
                e_hotel_id.insert(0, room[6])

            Messagebox.showinfo("Fetch Status", "Fetch Succesfully")

        con.close()
 

def add():
    hotel_id = e_hotel_id.get()
    room_id = e_room_id.get()
    room_info = e_room_info.get()
    price = e_price.get()
    capacity = e_capacity.get("1.0", END)
    status = e_status.get()
    room_number = e_room_number.get("1.0", END)
    room_type = e_room_type.get()

    if(hotel_id == "" or room_info == "" or price == "" or capacity == ""
             or room_number == "" or room_type == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("select name from hotel where id= '" + hotel_id + "'")
        hotel_name = cursor.fetchall()
        #call addroom(:room_info, :room_price, :room_number, :status, :capacity, :feature, :hotel_name, :room_type)*/
        cursor.execute("Call addRoom('" + room_info + "'," + price + "," +
                       room_number + ",'" + status + "'," + capacity + "," +"' '"+ ",'"+ hotel_name[0][0] + "','"+ room_type + "')")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        get_rooms()
        
        e_hotel_id.delete(0, "end")
        e_room_id.delete(0, "end")
        e_room_info.delete(0, "end")
        e_price.delete(0, "end")
        e_capacity.delete("1.0", END)
        e_status.delete(0, "end")
        e_room_number.delete("1.0", END)
        room_type.delete(0, "end")

        con.close()

def update():
    hotel_id = e_hotel_id.get()
    room_id = e_room_id.get()
    room_info = e_room_info.get()
    price = e_price.get()
    capacity = e_capacity.get("1.0", END)
    status = e_status.get()
    room_number = e_room_number.get("1.0", END)
    room_type = e_room_type.get()

    if(hotel_id == "" or room_id == "" or room_info == "" or price == "" or capacity == "" or status == ""
                    or room_number == "" or room_type == ""):
        Messagebox.showinfo("Update Status", "All Fields Are Required!")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from room where id = " + room_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            room_id.delete(0, "end")

        else:
            cursor.execute("Call updateroom('" + room_id + "','" + room_info + "'," + price +
                           ",'" + status + "'," + capacity + "," + "' '" + ",'" + room_type + "')")

            Messagebox.showinfo("Update Status", "Updated Succesfully")
            con.commit()
            get_rooms()

            e_hotel_id.delete(0, "end")
            e_room_id.delete(0, "end")
            e_room_info.delete(0, "end")
            e_price.delete(0, "end")
            e_capacity.delete("1.0", END)
            e_status.delete(0, "end")
            e_room_number.delete("1.0", END)
            room_type.delete(0, "end")

        con.close()

def delete():
    room_id = e_room_id.get()
    if(room_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute(
            "select exists (select * from room where id = " + room_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo(
                "Fetch Status", "Fetch Failed! Record Not Found")
            e_room_id.delete(0, "end")

        else:
            cursor.execute("Call deleteroom(" + room_id + ")")

            e_room_id.delete(0, "end")
            e_room_info.delete(0, "end")
            e_price.delete(0, "end")
            e_capacity.delete("1.0", END)
            e_room_number.delete("1.0", END)
        

            Messagebox.showinfo("Delete Status", "Delete Succesfully")
            con.commit()
            get_rooms()
        con.close()

'''SIDE BAR'''
employee = Button(hotelRoomRoot, text="EMPLOYEES", font=(
    "bold", 10), bg="#FEF9E7", command=employeePage)
employee.place(relx=0.028, rely=0.091, height=24, width=127)

room = Button(hotelRoomRoot, text="ROOMS", font=(
    "bold", 10), bg="#F1C40F")
room.place(relx=0.028, rely=0.163, height=24, width=127)

extra_services = Button(hotelRoomRoot, text="EXTRA SERVICES", font=(
    "bold", 10), bg="#FEF9E7", command= extraServicePage)
extra_services.place(relx=0.028, rely=0.236, height=24, width=127)

organizations = Button(hotelRoomRoot, text="ORGANIZATIONS", font=(
    "bold", 10), bg="#FEF9E7", command= organizationPage)
organizations.place(relx=0.028, rely=0.308, height=24, width=127)

TSeparator1 = ttk.Separator(hotelRoomRoot)
TSeparator1.place(relx=0.179, rely=0.032, relheight=0.82)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(hotelRoomRoot)
TSeparator2.place(relx=0.188, rely=0.284, relwidth=0.635)

'''INPUT TEXTS'''
room_id = Label(hotelRoomRoot, text="ID: ", font=("bold", 9))
room_id.place(relx=0.199, rely=0.063, height=21, width=23)

e_room_id = Entry(hotelRoomRoot)
e_room_id.place(relx=0.228, rely=0.063, height=20, relwidth=0.034)

room_info = Label(hotelRoomRoot, text="Room Info: ", font=("bold", 9))
room_info.place(relx=0.275, rely=0.063, height=21, width=68)

e_room_info = Entry(hotelRoomRoot)
e_room_info.place(relx=0.348, rely=0.063, relheight=0.08, relwidth=0.330)

price = Label(hotelRoomRoot, text="Price: ", font=("bold", 9))
price.place(relx=0.690, rely=0.063, height=21, width=38)

e_price = Entry(hotelRoomRoot)
e_price.place(relx=0.740, rely=0.063, height=20, relwidth=0.120)


capacity = Label(hotelRoomRoot, text="Capacity: ", font=("bold", 9))
capacity.place(relx=0.410, rely=0.158, height=21, width=58)

e_capacity = Text(hotelRoomRoot)
e_capacity.place(relx=0.475, rely=0.158, height=20, relwidth=0.040)

room_number = Label(hotelRoomRoot, text="Room Number: ", font=("bold", 9))
room_number.place(relx=0.525, rely=0.158, height=21, width=91)

e_room_number  = Text(hotelRoomRoot)
e_room_number.place(relx=0.625, rely=0.158,height=20, relwidth=0.075)

hotel_id = Label(hotelRoomRoot, text="Hotel ID: ", font=("bold", 9))
hotel_id.place(relx=0.199, rely=0.221, height=21, width=50)

e_hotel_id = Entry(hotelRoomRoot)
e_hotel_id.place(relx=0.260, rely=0.221, height=20, relwidth=0.034)

'''COMBOBOX'''

status = Label(hotelRoomRoot, text="Status: ", font=("bold", 9))
status.place(relx=0.199, rely=0.158, height=21, width=44)

box_value = StringVar()
e_status = ttk.Combobox(
    hotelRoomRoot, textvariable=box_value, state='readonly')
e_status.place(relx=0.260, rely=0.158, relheight=0.033, relwidth=0.142)

e_status['values'] = ('available', 'not available')
e_status.current(0)

room_type = Label(hotelRoomRoot, text="Room Type: ", font=("bold", 9))
room_type.place(relx=0.705, rely=0.158, height=21, width=72)

box_value = StringVar()
e_room_type = ttk.Combobox(
    hotelRoomRoot, textvariable=box_value, state='readonly')
e_room_type.place(relx=0.780, rely=0.158, relheight=0.033, relwidth=0.082)

e_room_type['values'] = ('Special', 'Standart')
e_room_type.current(0)


'''OPERATION BUTTONS'''
add = Button(hotelRoomRoot, text="Add", font=(
    "italic", 10), bg="#7DCEA0", command = add)
add.place(relx=0.337, rely=0.221, height=24, width=97)

update = Button(hotelRoomRoot, text="Update", font=(
    "italic", 10), bg="#5DADE2", command = update)
update.place(relx=0.437, rely=0.221, height=24, width=99)

delete = Button(hotelRoomRoot, text="Delete", font=(
    "italic", 10), bg="#F1948A", command = delete)
delete.place(relx=0.536, rely=0.221, height=24, width=97)

get = Button(hotelRoomRoot, text="Get Room", font=(
    "italic", 10), bg="#BB8FCE", command = get)
get.place(relx=0.635, rely=0.221, height=24, width=97)

get = Button(hotelRoomRoot, text="Show Rooms", font=(
    "italic", 10), bg="#F8C471", command = get_rooms)
get.place(relx=0.733, rely=0.221, height=24, width=97)

'''LIST OUTPUT'''
rooms = Label(hotelRoomRoot, text="Room Table", font=("Comic Sans MC", 9))
rooms.place(relx=0.480, rely=0.29, height=31, width=66)

room_list = ttk.Treeview(hotelRoomRoot, height=10, columns=5)
room_list.grid(row=4, column=0)

room_list.configure(columns="Col1 Col2 Col3 Col4 Col5")
room_list.heading("#0", text='ID', anchor=N)
room_list.column("#0", width='40', stretch=NO)
room_list.heading("Col1", text='Room Info', anchor=N)
room_list.column("Col1", width='350')
room_list.heading("Col2", text='Room Price', anchor=N)
room_list.column("Col2", width='5')
room_list.heading("Col3", text='Room Number', anchor=N)
room_list.column("Col3", width='90', stretch=NO)
room_list.heading("Col4", text='Status', anchor=N)
room_list.column("Col4", width='5')
room_list.heading("Col5", text='Capacity', anchor=N)
room_list.column("Col5", width='5')

room_list.place(relx=0.189, rely=0.340, relheight=0.38, relwidth=0.800)

tk.mainloop()