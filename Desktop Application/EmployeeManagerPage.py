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
staffRoot.configure(background='#EBEDEF')
staffRoot.title("Hotel Employees Page")

def organizationPage():
    import OrganizationPage

def extraServicePage():
    import ExtraServicePage

def roomPage():
    import HotelRoomPage

def add():
    firstname = e_firstname.get()
    lastname = e_lastname.get()
    telephone = e_telephone.get()
    email = e_email.get()
    passwrd = e_password.get()
    confirm_passwrd = e_confirm_passwrd.get()
    address = e_address.get("1.0", END)
    salary = e_salary.get()
    employee_type = e_emp_type.get()
    hotel_id = e_hotel_id.get()

    if(firstname == "" or lastname == "" or passwrd == "" or email == "" or address == ""
            or telephone == "" or salary == "" or employee_type == ""):
        Messagebox.showinfo("Insert Status", "All Fields Are Required!")
    elif(passwrd != confirm_passwrd):
        Messagebox.showinfo("Password Status", "Password Mismatch")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        cursor.execute("select name from hotel where id= '" + hotel_id + "'")
        hotel_name = cursor.fetchall()
        #print(hotel_name[0][0])
        #call addperson(:firstname, :lastname, :passwrd, :mail, :address, :phone, :age, :salary, :username, :hotel_name, :person_type)*/
        cursor.execute("Call addPerson('" + firstname + "','" + lastname + "','" + passwrd
                       + "','" + email + "','" + address + "','" + telephone + "'," + "0" + ","
                       + salary + "," + "' '" + ",'" + hotel_name[0][0] + "','"+ employee_type +"')")

        Messagebox.showinfo("Insert Status", "Inserted Succesfully")
        con.commit()
        if(employee_type == "manager"):
            man_list()
        else:
            emp_list()

        e_emp_id.delete(0, "end")
        e_firstname.delete(0, "end")
        e_lastname.delete(0, "end")
        e_password.delete(0, "end")
        e_confirm_passwrd.delete(0, "end")
        e_email.delete(0, "end")
        e_address.delete('1.0', END)
        e_telephone.delete(0, "end")
        e_salary.delete(0, "end")
        e_emp_type.delete(0, "end")

        con.close()

def get():
    e_firstname.delete(0, "end")
    e_lastname.delete(0, "end")
    e_password.delete(0, "end")
    e_confirm_passwrd.delete(0, "end")
    e_email.delete(0, "end")
    e_address.delete('1.0', END)
    e_telephone.delete(0, "end")
    e_salary.delete(0, "end")
 

    emp_id = e_emp_id.get()
    emp_type = e_emp_type.get()
    if(emp_id == ""):
        Messagebox.showinfo(
            "Fetch Status", "ID is compolsary for fetch")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        if(emp_type == "manager"):
            cursor.execute("select exists (select * from manager_all_info where id = " + emp_id + ")") 
            boolean = cursor.fetchall()
            if(boolean[0][0] == 0):
                Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
                e_emp_id.delete(0, "end")
            else:
                cursor.execute(
                    "select * from manager_all_info where id = " + emp_id + "")
                manager = cursor.fetchall()

                for man in manager:
                    e_firstname.insert(0, man[1])
                    e_lastname.insert(0, man[2])
                    e_password.insert(0, man[3])
                    e_email.insert(0, man[4])
                    e_telephone.insert(0, man[5])
                    e_address.insert(INSERT, man[6])
                    e_salary.insert(0, man[12])
                    e_hotel_id.insert(0, man[9])

                Messagebox.showinfo("Fetch Status", "Fetch Succesfully")
        else:
            cursor.execute("select exists (select * from employee_all_info where id = " + emp_id + ")") 
            boolean = cursor.fetchall()
            if(boolean[0][0] == 0):
                Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
                e_emp_id.delete(0, "end")
            else:
                cursor.execute(
                    "select * from employee_all_info where id = " + emp_id + "")
                employee = cursor.fetchall()

                for emp in employee:
                    e_firstname.insert(0, emp[1])
                    e_lastname.insert(0, emp[2])
                    e_password.insert(0, emp[3])
                    e_email.insert(0, emp[4])
                    e_telephone.insert(0, emp[5])
                    e_address.insert(INSERT, emp[6])
                    e_salary.insert(0, emp[12])
                    e_hotel_id.insert(0, emp[9])

                Messagebox.showinfo("Fetch Status", "Fetch Succesfully")

        con.close()
        
def man_list():
    records = manager_list.get_children()
    for element in records:
        manager_list.delete(element)

    con = mysql.connect(host="localhost", user="root",
                        password="12345", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("select * from manager_all_info order by id asc")
    manager = cursor.fetchall()

    for man in manager:
        manager_list.insert('', 0, text=man[0], value=(
            man[1], man[2], man[4], man[6], man[5], man[10]))

    con.close()

def emp_list():
    records = employee_list.get_children()
    for element in records:
        employee_list.delete(element)

    con = mysql.connect(host="localhost", user="root",
                        password="12345", database="hotel_reservation")
    cursor = con.cursor()
    cursor.execute("select * from employee_all_info order by id asc")
    employee = cursor.fetchall()

    for emp in employee:
        employee_list.insert('', 0, text=emp[0], value=(
            emp[1], emp[2], emp[4], emp[6], emp[5], emp[10]))

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
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        if ( employee_type == "manager"):
            cursor.execute("select exists (select * from manager_all_info where id = " + emp_id + ")")
        else:
            cursor.execute("select exists (select * from employee_all_info where id = " + emp_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
            e_emp_id.delete(0, "end")

        else:
            cursor.execute("Call updatePerson('" + emp_id + "','" + firstname + "','" + lastname + "','" + passwrd
                        + "','" + email + "','" + address + "','" + telephone + "'," + '0' + ","
                        + salary + "," + "' '" + "," + "' '" + ",'"+ employee_type +"')")

            Messagebox.showinfo("Update Status", "Updated Succesfully")
            con.commit()
            emp_list()
            man_list()

            e_email.config(state="normal")
        
            e_firstname.delete(0, "end")
            e_hotel_id.delete(0, "end")
            e_lastname.delete(0, "end")
            e_password.delete(0, "end")
            e_confirm_passwrd.delete(0, "end")
            e_email.delete(0, "end")
            e_address.delete('1.0', END)
            e_telephone.delete(0, "end")
            e_salary.delete(0, "end")

        con.close()

def delete():
    emp_id = e_emp_id.get()
    emp_type = e_emp_type.get()
    if(emp_id == ""):
        Messagebox.showinfo(
            "Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="12345", database="hotel_reservation")
        cursor = con.cursor()
        if ( emp_type == "manager"):
            cursor.execute("select exists (select * from manager_all_info where id = " + emp_id + ")")
        else:
            cursor.execute("select exists (select * from employee_all_info where id = " + emp_id + ")")
        boolean = cursor.fetchall()

        if(boolean[0][0] == 0):
            Messagebox.showinfo( "Fetch Status", "Fetch Failed! Record Not Found")
            e_emp_id.delete(0, "end")
            
        else:
            cursor.execute("Call deletePerson(" + emp_id + ")")

            e_firstname.delete(0, "end")
            e_hotel_id.delete(0, "end")
            e_lastname.delete(0, "end")
            e_password.delete(0, "end")
            e_confirm_passwrd.delete(0, "end")
            e_email.delete(0, "end")
            e_address.delete('1.0', END)
            e_telephone.delete(0, "end")
            e_salary.delete(0, "end")

            Messagebox.showinfo("Delete Status", "Delete Succesfully")
            con.commit()
            emp_list()
            man_list()

        con.close()

'''SIDE BAR'''
employee = Button(staffRoot, text="EMPLOYEES", font=(
    "bold", 10,"bold"), bg="#F1C40F")
employee.place(relx=0.028, rely=0.091, height=24, width=127)

room = Button(staffRoot, text="ROOMS", font=(
    "bold", 10), bg="#FEF9E7",command = roomPage)
room.place(relx=0.028, rely=0.163, height=24, width=127)

extra_services = Button(staffRoot, text="EXTRA SERVICES", font=(
    "bold", 10), bg="#FEF9E7",command = extraServicePage )
extra_services.place(relx=0.028, rely=0.236, height=24, width=127)

organizations = Button(staffRoot, text="ORGANIZATIONS", font=(
    "bold", 10), bg="#FEF9E7", command= organizationPage)
organizations.place(relx=0.028, rely=0.308, height=24, width=127)

TSeparator1 = ttk.Separator(staffRoot)
TSeparator1.place(relx=0.179, rely=0.032, relheight=0.82)
TSeparator1.configure(orient="vertical")

TSeparator2 = ttk.Separator(staffRoot)
TSeparator2.place(relx=0.188, rely=0.354, relwidth=0.780)

'''INPUT TEXTS'''
emp_id = Label(staffRoot, text="ID: ", font=("bold", 9))
emp_id.place(relx=0.201, rely=0.065, height=21, width=24)
emp_id.configure(background="#EBEDEF")

e_emp_id = Entry(staffRoot)
e_emp_id.place(relx=0.236, rely=0.065, height=20, relwidth=0.039)

firstname = Label(staffRoot, text="First Name: ", font=("bold", 9))
firstname.place(relx=0.285, rely=0.065, height=21, width=69)
firstname.configure(background="#EBEDEF")

e_firstname = Entry(staffRoot)
e_firstname.place(relx=0.360, rely=0.065, height=20, relwidth=0.150)

lastname = Label(staffRoot, text="Last Name: ", font=("bold", 9))
lastname.place(relx=0.520, rely=0.065, height=21, width=68)
lastname.configure(background="#EBEDEF")

e_lastname = Entry(staffRoot)
e_lastname.place(relx=0.600, rely=0.065, height=20, relwidth=0.150)

telephone = Label(staffRoot, text="Phone: ", font=("bold", 9))
telephone.place(relx=0.760, rely=0.065, height=21, width=46)
telephone.configure(background="#EBEDEF")

e_telephone = Entry(staffRoot)
e_telephone.place(relx=0.810, rely=0.065, height=20, relwidth=0.130)

email = Label(staffRoot, text="Email: ", font=("bold", 9))
email.place(relx=0.201, rely=0.113, height=21, width=41)
email.configure(background="#EBEDEF")

e_email = Entry(staffRoot)
e_email.place(relx=0.256, rely=0.113, height=20, relwidth=0.254)

passwrd = Label(staffRoot, text="Password: ", font=("bold", 9))
passwrd.place(relx=0.520, rely=0.113, height=19, width=60)
passwrd.configure(background="#EBEDEF")

e_password = Entry(staffRoot)
e_password.place(relx=0.585, rely=0.113, height=20, relwidth=0.110)

confirm_passwrd = Label(staffRoot, text="Confirm Password: ", font=("bold", 9))
confirm_passwrd.place(relx=0.700, rely=0.113, height=21, width=109)
confirm_passwrd.configure(background="#EBEDEF")

e_confirm_passwrd = Entry(staffRoot)
e_confirm_passwrd.place(relx=0.810, rely=0.113, height=20, relwidth=0.130)

address = Label(staffRoot, text="Address: ", font=("bold", 9))
address.place(relx=0.201, rely=0.160, height=21, width=54)
address.configure(background="#EBEDEF")

e_address = Text(staffRoot)
e_address.place(relx=0.256, rely=0.160, relheight=0.100, relwidth=0.35)

salary = Label(staffRoot, text=" Salary: ", font=("bold", 9))
salary.place(relx=0.610, rely=0.161, height=21, width=40)
salary.configure(background="#EBEDEF")

e_salary = Entry(staffRoot)
e_salary.place(relx=0.660, rely=0.161, height=20, relwidth=0.049)

hotel_id = Label(staffRoot, text="Hotel ID: ", font=("bold", 9))
hotel_id.place(relx=0.610, rely=0.209, height=21, width=60)

e_hotel_id= Entry(staffRoot)
e_hotel_id.place(relx=0.670, rely=0.209, height=21, relwidth=0.037)

'''COMBOBOX'''
emp_type = Label(staffRoot, text="Employee Type: ", font=("bold", 9))
emp_type.place(relx=0.720, rely=0.158, height=21, width=90)
emp_type.configure(background="#EBEDEF")

box_value = StringVar()
e_emp_type = ttk.Combobox(
    staffRoot, textvariable=box_value, state='readonly')
e_emp_type.place(relx=0.810, rely=0.158, relheight=0.033, relwidth=0.130)

e_emp_type['values'] = ('manager', 'employee')
e_emp_type.current(0)

'''OPERATION BUTTONS'''
add = Button(staffRoot, text="Add", font=(
    "italic", 10,"bold"),  bg="#7DCEA0", command = add)
add.place(relx=0.337, rely=0.291, height=24, width=97)

update = Button(staffRoot, text="Update", font=(
    "italic", 10,"bold"), bg="#5DADE2",command=update)
update.place(relx=0.435, rely=0.291, height=24, width=99)

delete = Button(staffRoot, text="Delete", font=(
    "italic", 10,"bold"), bg="#F1948A", command=delete)
delete.place(relx=0.536, rely=0.291, height=24, width=97)

get = Button(staffRoot, text="Get Staff", font=(
    "italic", 10,"bold"), bg="#BB8FCE", command=get)
get.place(relx=0.635, rely=0.291, height=24, width=97)

'''LIST OUTPUT'''
manager = Label(staffRoot, text="Manager Table", font=("Comic Sans MC", 9,"bold"))
manager.place(relx=0.480, rely=0.36, height=31, width=90)
manager.configure(background="#EBEDEF")

manager_list = ttk.Treeview(staffRoot, height=10, columns=5)
manager_list.grid(row=4, column=0)

manager_list.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6")
manager_list.heading("#0", text='ID', anchor=N)
manager_list.column("#0", width='5')
manager_list.heading("Col1", text='First Name', anchor=N)
manager_list.column("Col1", width='5')
manager_list.heading("Col2", text='Last Name', anchor=N)
manager_list.column("Col2", width='5')
manager_list.heading("Col3", text='Email', anchor=N)
manager_list.column("Col3", width='120')
manager_list.heading("Col4", text='Address', anchor=N)
manager_list.column("Col4", width='135')
manager_list.heading("Col5", text='Telephone', anchor=N)
manager_list.column("Col5", width='25')
manager_list.heading("Col6", text='Salary (₺)', anchor=N)
manager_list.column("Col6", width='5')

manager_list.place(relx=0.189, rely=0.415, relheight=0.18, relwidth=0.750)

man_list()

#--------------------------------------------------------------------------
emp = Label(staffRoot, text="Employee Table", font=("Comic Sans MC", 9,"bold"))
emp.place(relx=0.480, rely=0.60, height=31, width=90)
emp.configure(background="#EBEDEF")

employee_list = ttk.Treeview(staffRoot, height=10, columns=5)
employee_list.grid(row=4, column=0)


employee_list.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6")
employee_list.heading("#0", text='ID', anchor=N)
employee_list.column("#0", width='5')
employee_list.heading("Col1", text='First Name', anchor=N)
employee_list.column("Col1", width='5')
employee_list.heading("Col2", text='Last Name', anchor=N)
employee_list.column("Col2", width='5')
employee_list.heading("Col3", text='Email', anchor=N)
employee_list.column("Col3", width='120')
employee_list.heading("Col4", text='Address', anchor=N)
employee_list.column("Col4", width='135')
employee_list.heading("Col5", text='Telephone', anchor=N)
employee_list.column("Col5", width='25')
employee_list.heading("Col6", text='Salary (₺)', anchor=N)
employee_list.column("Col6", width='5')

employee_list.place(relx=0.189, rely=0.66, relheight=0.18, relwidth=0.750)
emp_list()

tk.mainloop()
