from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")

        title=Label(self.root, text = "Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"), bg="blue",fg="red")
        title.pack(side=TOP,fill=X)

    #============All variables======
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()


    #============M frame ============
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=480,height=660)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white", font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_rolL = Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white", font=("times new roman",20,"bold"))
        lbl_rolL.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable = self.roll_no_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame,textvariable = self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame,textvariable = self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable = self.gender_var,font=("times new roman", 13, "bold"),state='readonly')
        combo_gender['values']=("male","female","others")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame,textvariable = self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame,textvariable = self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_add = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_add.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_add=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_add.grid(row=7,column=1,padx=20,pady=10,sticky="w")

    #=========B frame========
        Btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        Btn_Frame.place(x=15, y=560, width=420)

        addbtn=Button(Btn_Frame,text="Add",width=10,command=self.add_students)
        addbtn.grid(row=0,column=0,padx=10,pady=10)

        upbtn = Button(Btn_Frame, text="Update", width=10,command=self.up)
        upbtn.grid(row=0, column=1, padx=10, pady=10)

        dltbtn = Button(Btn_Frame, text="Delete", width=10,command=self.dlt)
        dltbtn.grid(row=0, column=2, padx=10, pady=10)

        clrbtn = Button(Btn_Frame, text="Clear", width=10,command=self.clear)
        clrbtn.grid(row=0, column=3, padx=10, pady=10)

    #============D frame ============
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=550, y=100, width=930, height=660)

        lbl_search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search= ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by_var, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll", "name", "contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame, width=20,textvariable=self.search_txt_var,font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        srcbtn = Button(Detail_Frame, text="Search", width=10,command=self.src)
        srcbtn.grid(row=0, column=3, padx=10, pady=10)

        showbtn = Button(Detail_Frame, text="Show All", width=10,command=self.fdt)
        showbtn.grid(row=0, column=4, padx=10, pady=10)

    #============T frame ============
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=900, height=570)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.getc)
        self.fdt()

    def add_students(self):
        if self.roll_no_var.get()=="" or self.name_var.get() == "":
            messagebox.showerror("Error","All fields are required!")
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="munna")
            cur = mydb.cursor()
            cur.execute("INSERT INTO student_table VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                    self.name_var.get(),
                                                                    self.email_var.get(),
                                                                    self.gender_var.get(),
                                                                    self.contact_var.get(),
                                                                    self.dob_var.get(),
                                                                    self.txt_add.get('1.0',END)
                                                                    ))
            mydb.commit()
            self.fdt()
            self.clear()
            mydb.close()
            messagebox.showinfo("Success","Record has been insreted!")
    def fdt(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="munna")
        cur = mydb.cursor()
        cur.execute("select * from student_table")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                mydb.commit()
        mydb.close()

    def clear(self):
        self.roll_no_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_add.delete('1.0', END)

    def getc(self,ev):
        cr=self.student_table.focus()
        cont=self.student_table.item(cr)
        row=cont['values']
        self.roll_no_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_add.delete('1.0', END)
        self.txt_add.insert(END,row[6])

    def up(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="munna")
        cur = mydb.cursor()
        cur.execute("update student_table set name=%s,email=%s,gender=%s,contact=%s,DOB=%s,Address=%s where Roll=%s", (
                                                                     self.name_var.get(),
                                                                     self.email_var.get(),
                                                                     self.gender_var.get(),
                                                                     self.contact_var.get(),
                                                                     self.dob_var.get(),
                                                                     self.txt_add.get('1.0', END),
                                                                     self.roll_no_var.get()
                                                                     ))

        mydb.commit()
        self.fdt()
        self.clear()
        mydb.close()

    def dlt(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="munna")
        cur = mydb.cursor()
        cur.execute("delete from student_table where Roll= %s",(
                                                      self.roll_no_var.get(),
                                                     ))
        mydb.commit()
        self.fdt()
        self.clear()
        mydb.close()

    def src(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="munna")
        cur = mydb.cursor()
        cur.execute("select * from student_table where "+str(self.search_by_var.get())+" LIKE '%"+str(self.search_txt_var.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                mydb.commit()
        mydb.close()




root=Tk()
ob=student(root)
root.mainloop()