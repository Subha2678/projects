from tkinter import *
import sqlite3
from tkinter import messagebox
con=sqlite3.connect('database.db')
cur=con.cursor()
class UPdatePerson(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)
        self.person_id=person_id
        self.geometry("650x550+500+120")
        self.title("Update person")
        self.resizable(False,False)
        
        self.top=Frame(self,height=150,bg="#f2f255")
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=500,bg="#38a89d")
        self.bottom.pack(fill=X)
        

         #database---------------------

        query=f"select * from addressbook where person_id={person_id}"
        result=cur.execute(query).fetchone()
        name=result[1]
        surname=result[2]
        email=result[3]
        phone=result[4]
        address=result[5]
        

        #top frame design-------------
        self.top_image=PhotoImage(file="icon\\update.png")
        self.top_image_label=Label(self.top,image=self.top_image,bg="#f2f255")
        self.top_image_label.place(x=70,y=15)

        self.heading=Label(self.top,text="Update Person",bg='#f2f255',fg='#db2727',font='Gabriola 26 bold')
        self.heading.place(x=200,y=30)


        #name
        self.label_name=Label(self.bottom,width=8,text="Name:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_name.place(x=30,y=50)
        self.entry_name=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_name.place(x=150,y=50)
        self.entry_name.insert(0,name)


        #surname
        self.label_surname=Label(self.bottom,width=8,text="Surname:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_surname.place(x=30,y=100)
        self.entry_surname=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_surname.place(x=150,y=100)
        self.entry_surname.insert(0,surname)

        #Email
        self.label_email=Label(self.bottom,width=8,text="Email:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_email.place(x=30,y=150)
        self.entry_email=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_email.place(x=150,y=150)
        self.entry_email.insert(0,email)
        #phone number
        self.label_phone=Label(self.bottom,width=8,text="Phone:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_phone.place(x=30,y=200)
        self.entry_phone=Entry(self.bottom,width=25,bg='#9dfaa4',font='Bahnschrift 14')
        self.entry_phone.place(x=150,y=200)
        self.entry_phone.insert(0,phone)
        #address
        self.label_address=Label(self.bottom,width=8,text="Address:",bg='#fa945c',fg='#3d2221',font='Bahnschrift 14')
        self.label_address.place(x=30,y=250)
        self.textarea_address=Text(self.bottom,width=30,height=5,bg='#9dfaa4',font='Bahnschrift 14')
        self.textarea_address.place(x=150,y=250)
        self.textarea_address.insert(1.0,address)

        #submit button
        self.btn_submit=Button(self.bottom,text="Update",width=10,bd=6,bg='#fa0a66',font='Bahnschrift 14',command=self.update_person)
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
    
    def update_person(self):
        p_id=self.person_id
        p_name=self.entry_name.get()
        p_surname=self.entry_surname.get()
        p_email=self.entry_email.get()
        p_phone=self.entry_phone.get()
        p_address=self.textarea_address.get(1.0,'end-1c')
        query=f"update addressbook set person_name='{p_name}',person_surname='{p_surname}',person_email='{p_email}',person_phone='{p_phone}',person_address='{p_address}' where person_id='{p_id}'"
        if p_name and p_surname and p_email and p_phone and p_address !="":    
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("success","contact updated successfully")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error!",str(e))
        else:
            messagebox.showerror("Error!","please fill all the fields",icon="warning")
            self.destroy()
            UPdatePerson(p_id)