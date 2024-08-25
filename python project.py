from tkinter import *
from tkinter import ttk
import sqlite3




class Create_Student:   
    def __init__(self, main):
        self.main_window = main
        self.C_Frame = Frame(self.main_window, height=600, width=400, relief=GROOVE,border=2, bg="white")
        self.C_Frame.pack(side=LEFT)
        Label(self.C_Frame, text="Student Details", font="arial 12 bold", bg="white").place(x = 10, y=10)
        self.C_Frame.pack_propagate(0)

#========================== name and entries ====================================================================
        self.S_ID = Label(self.C_Frame, text="ID:", font="arial 12 bold", bg="white")
        self.S_ID.place(x = 40, y = 60)
        self.S_ID_Field = Entry(self.C_Frame,  width=40)
        self.S_ID_Field.place(x=150, y=60)

        self.S_Name = Label(self.C_Frame, text="Name:", font="arial 12 bold", bg="white")
        self.S_Name.place(x=40, y=90)
        self.S_Name_Field = Entry(self.C_Frame, width=40)
        self.S_Name_Field.place(x=150, y=90)


        self.S_Age = Label(self.C_Frame, text="Age:", font="arial 12 bold", bg="white")
        self.S_Age.place(x = 40, y = 120)
        self.S_Age_Field = Entry(self.C_Frame,  width=40)
        self.S_Age_Field.place(x=150, y=120)

        self.S_DOB = Label(self.C_Frame, text="DOB:", font="arial 12 bold", bg="white")
        self.S_DOB.place(x = 40, y = 150)
        self.S_DOB_Field = Entry(self.C_Frame, width=40)
        self.S_DOB_Field.place(x=150, y=150)

        self.S_Gender = Label(self.C_Frame, text="Gender:", font="arial 12 bold", bg="white")
        self.S_Gender.place(x = 40, y = 180)
        self.S_Gender_Field = Entry(self.C_Frame, width=40)
        self.S_Gender_Field.place(x=150, y=180)

        self.S_City = Label(self.C_Frame, text="City:", font="arial 12 bold", bg="white")
        self.S_City.place(x = 40, y = 210)
        self.S_City_Field = Entry(self.C_Frame,  width=40)
        self.S_City_Field.place(x=150, y=210)

#======================================= buttons =========================================================

        self.Button_Frame = Frame(self.C_Frame, height=250, width=250, relief=GROOVE, border=2, bg="white")
        self.Button_Frame.place(x = 40, y = 250)

        # create buttons
        self.Add_Button = Button(self.Button_Frame, text="Add", font="arial 15 bold", width=25, command=self.Add)
        self.Add_Button.pack()

        self.Delete_Button = Button(self.Button_Frame, text="Delete" , font="arial 15 bold", width=25, command=self.Delete)
        self.Delete_Button.pack()

        self.Update_Button = Button(self.Button_Frame, text="Update", font="arial 15 bold", width=25, command=self.Update)
        self.Update_Button.pack()

        self.Clear_Button = Button(self.Button_Frame, text="Clear", font="arial 15 bold", width=25, command=self.Clear)
        self.Clear_Button.pack()





        self.S_S_Details = Frame(main, height=600, width=800, relief=GROOVE,border=2, bg="white")
        self.S_S_Details.pack(side=LEFT)

        self.tree = ttk.Treeview(self.S_S_Details, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings',
                                         height=25)

        self.tree.column("#1", anchor=CENTER, width=50)
        self.tree.heading("#1", text="ID")
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="Name")
        self.tree.column("#3", anchor=CENTER, width=120)
        self.tree.heading("#3", text="DOB")
        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="Age")
        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="Gender")
        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="City")
        c = sqlite3.connect("data.db")
        cursor = c.cursor()
        cursor.execute("select * from data")
        a = cursor.fetchall()
        n = 0
        for i in a:
            b = a[n]
            id = b[0]
            name = b[1]
            age = b[2]
            dob = b[3]
            gender = b[4]
            city = b[5]
            self.tree.insert("", index=END, values=(id, name, age, dob, gender, city))
            n += 1
        c.commit()
        c.close()

        self.tree.place(x=0, y=0)



    def Add(self):
        id = self.S_ID_Field.get()
        name = self.S_Name_Field.get()
        age = self.S_Age_Field.get()
        dob = self.S_DOB_Field.get()
        gender = self.S_Gender_Field.get()
        city = self.S_City_Field.get()
        try:
            c = sqlite3.connect("data.db")
            cursor = c.cursor()
            cursor.execute('insert into data values(?,?,?,?,?,?)', (id, name, age, dob, gender, city))
            c.commit()
            c.close()
            self.tree.insert("", index=0, values=(id, name, age, dob, gender, city))
            print("Row inserted")
        except sqlite3.OperationalError:

            c = sqlite3.connect("data.db")
            cursor = c.cursor()
            t = """CREATE TABLE IF NOT EXISTS data(ID INTEGER, NAME VARCHAR(20), DOB VARCHAR(20), AGE VARCHAR(20), GENDER VARCHAR(20), CITY VARCHAR(20))
            """
            print("Table Created")

            cursor.execute(t)
            c.commit()
            c.close()



    def Delete(self):
        try:
            c = sqlite3.connect("data.db")
            cursor = c.cursor()
            item = self.tree.selection()[0]
            selected_item = self.tree.item(item)['values'][0]
            print(selected_item)
            cursor.execute("delete from data where ID={}".format(selected_item))
            print("Deleted")
            self.tree.delete(item)
            c.commit()
            c.close()
        except sqlite3.OperationalError:

            c = sqlite3.connect("data.db")
            cursor = c.cursor()
            t = """CREATE TABLE IF NOT EXISTS data(ID INTEGER, NAME VARCHAR(20), DOB VARCHAR(20), AGE VARCHAR(20), GENDER VARCHAR(20), CITY VARCHAR(20))
            """
            print("Table Created")

            cursor.execute(t)
            c.commit()
            c.close()

    def Update(self):
        id = self.S_ID_Field.get()
        name = self.S_Name_Field.get()
        age = self.S_Age_Field.get()
        dob = self.S_DOB_Field.get()
        gender = self.S_Gender_Field.get()
        city = self.S_City_Field.get()
        s_item = self.tree.selection()[0]
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        try:
            c = sqlite3.connect("data.db")
            cursor = c.cursor()

            cursor.execute('update data set ID=?, NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? where ID=?',
                           (selected_item, name, age, dob, gender, city, selected_item))
            print("Row updated")
            self.tree.item(s_item, values=(id, name, age, dob, gender, city))
            c.commit()
            c.close()
        except sqlite3.OperationalError:

            c = sqlite3.connect("data.db")
            cursor = c.cursor()
            t = """CREATE TABLE IF NOT EXISTS data(ID INTEGER, NAME VARCHAR(20), DOB VARCHAR(20), AGE VARCHAR(20), GENDER VARCHAR(20), CITY VARCHAR(20))
            """
            print("Table Created")

            cursor.execute(t)
            c.commit()
            c.close()


    def Clear(self):
        self.S_ID_Field.delete(0, END)
        self.S_Name_Field.delete(0, END)
        self.S_Age_Field.delete(0, END)
        self.S_DOB_Field.delete(0, END)
        self.S_Gender_Field.delete(0, END)
        self.S_City_Field.delete(0, END)




main_window = Tk()
main_window.title("Student Data Management System")
main_window.resizable(False, False)
main_window.geometry("1200x600")
Title = Frame(main_window, height=50, width=1200, relief=GROOVE, bg="white")
Title.pack()
T_Text = Label(Title, text="Student Data Management System", width=1200, font="arial 24 bold", bg="white")
T_Text.pack()

Datas = Create_Student(main_window)

main_window.mainloop()
