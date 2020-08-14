from tkinter import *
import sqlite3
from tkinter import messagebox
con=sqlite3.connect('database.db')
cur=con.cursor()
class AddPerson(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+500+120")
        self.title("Add People")
        self.resizable(False,False)
        
        self.top=Frame(self,height=150,bg="#f2f255")
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=500,bg="#38a89d")
        self.bottom.pack(fill=X)

        #top frame design-------------
        self.top_image=PhotoImage(file="icon\\person.png")
        self.top_image_label=Label(self.top,image=self.top_image,bg="#f2f255")
        self.top_image_label.place(x=70,y=15)

        self.heading=Label(self.top,text="Add Person",bg='#f2f255',fg='#db2727',font='Gabriola 26 bold')
        self.heading.place(x=200,y=30)


        #name
        self.label_name=Label(self.bottom,width=8,text="Name:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_name.place(x=30,y=50)
        self.entry_name=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_name.place(x=150,y=50)

        #surname
        self.label_surname=Label(self.bottom,width=8,text="Surname:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_surname.place(x=30,y=100)
        self.entry_surname=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_surname.place(x=150,y=100)
        #Email
        self.label_email=Label(self.bottom,width=8,text="Email:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_email.place(x=30,y=150)
        self.entry_email=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_email.place(x=150,y=150)
        #phone number
        self.label_phone=Label(self.bottom,width=8,text="Phone:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_phone.place(x=30,y=200)
        self.entry_phone=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_phone.place(x=150,y=200)
        #address
        self.label_address=Label(self.bottom,width=8,text="Address:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_address.place(x=30,y=250)
        self.textarea_address=Text(self.bottom,width=30,height=5,bg='#9dfaa4',font='Bahnschrift 14')
        self.textarea_address.place(x=150,y=250)

        #submit button
        self.btn_submit=Button(self.bottom,text="Add person",width=10,bd=6,bg='#fa0a66',font='Bahnschrift 14',command=self.add_person)
        self.btn_submit.place(x=500,y=160)
        #clear button
        self.btn_clear=Button(self.bottom,text="Clear",width=10,bd=6,bg='#fa0a66',font='Bahnschrift 14',command=self.clear)
        self.btn_clear.place(x=500,y=90)
    def clear(self):
        self.entry_name.delete(0,END)
        self.entry_surname.delete(0,END)
        self.entry_email.delete(0,END)
        self.entry_phone.delete(0,END)
        self.textarea_address.delete(1.0,END)
    def add_person(self):
        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        address=self.textarea_address.get(1.0,'end-1c')
        if name and surname and email and phone and address !="":    
            try:
                query="insert into 'addressbook' (person_name,person_surname,person_email,person_phone,person_address) values(?,?,?,?,?)"
                cur.execute(query,(name,surname,email,phone,address))
                con.commit()
                messagebox.showinfo("success","contact added successfully")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error!",str(e))
        
        else:
            messagebox.showerror("Error!","please fill all the fields",icon="warning")
            self.destroy()
            AddPerson()