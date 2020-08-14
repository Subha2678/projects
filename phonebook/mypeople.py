from tkinter import *
from tkinter import messagebox
from addpeople import AddPerson
from updatepeople import UPdatePerson
from displaypepople import DisplayPeople
import sqlite3
con=sqlite3.connect('database.db')
cur=con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x550+500+120")
        self.title("My People")
        self.resizable(False,False)
        
        self.top=Frame(self,height=150,bg="#f2f255")
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=500,bg="#38a89d")
        self.bottom.pack(fill=X)

        #top frame design-------------
        self.top_image=PhotoImage(file="icon\\mypeople.png")
        self.top_image_label=Label(self.top,image=self.top_image,bg="#f2f255")
        self.top_image_label.place(x=70,y=15)

        self.heading=Label(self.top,text="My People",bg='#f2f255',fg='#db2727',font='Gabriola 26 bold')
        self.heading.place(x=200,y=30)

        #listbox and scrollbar-------------------
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        self.listbox=Listbox(self.bottom,width=35,height=25,bg='#d45f98',font='6')
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listbox.yview)
        self.listbox.grid(row=0,column=0,padx=(40,0))
        self.scroll.grid(row=0,column=1,sticky=N+S)

        

        #buttons-add,update,display,delete----------------------
        
        self.add_btn=Button(self.bottom,width=8,height=2,bd=4,bg='#0fd488',fg="#0526fa",text='Add',font='Fixedsys 16 bold',command=self.add_people)
        self.add_btn.place(x=470,y=50)
        self.update_btn=Button(self.bottom,width=8,height=2,bd=4,bg='#0fd488',fg="#0526fa",text='Update',font='Fixedsys 16 bold',command=self.update_func)
        self.update_btn.place(x=470,y=120)
        
        self.display_btn=Button(self.bottom,width=8,height=2,bd=4,bg='#0fd488',fg="#0526fa",text='Display',font='Fixedsys 16 bold',command=self.display_func)
        self.display_btn.place(x=470,y=190)
        self.delete_btn=Button(self.bottom,width=8,height=2,bd=4,bg='#0fd488',fg="#0526fa",text='Delete',font='Fixedsys 16 bold',command=self.delete_func)
        self.delete_btn.place(x=470,y=260)
        
        #database------------------------------
        persons=cur.execute("select * from addressbook").fetchall()
        count=0
        for person in persons:
            self.listbox.insert(count,(f"{person[0]}.{person[1]} {person[2]}"))
            count+=1
   
    def add_people(self):
        AddPerson()
        self.destroy()

    def update_func(self):
        try:
            selected_person=self.listbox.curselection()
            person=self.listbox.get(selected_person)
            person_id=person.split(".")[0]
            UPdatePerson(person_id)
            self.destroy()
        except Exception as ex:
            messagebox.showinfo("Selct","Please select any person")
            self.destroy()
            MyPeople()




    def display_func(self):
        try:
            selected_person=self.listbox.curselection()
            person=self.listbox.get(selected_person)
            person_id=person.split(".")[0]
            DisplayPeople(person_id)
            self.destroy()
        except Exception as ex:
            messagebox.showinfo("Selct","Please select any person")
            self.destroy()
            MyPeople()

    def delete_func(self):
        try:
            selected_person=self.listbox.curselection()
            person=self.listbox.get(selected_person)
            person_id=person.split(".")[0]
            query=f"delete from addressbook where person_id={person_id}"
            msgbx=messagebox.askyesnocancel("confirm","Are you sure to delete this person?")
            if msgbx:
                try:
                    cur.execute(query)
                    con.commit()
                    messagebox.showinfo("success","contact deleted successfully")
                    self.destroy()
                    MyPeople()
                except Exception as e:
                    messagebox.showerror("Error!",str(e))
        except Exception as ex:
            messagebox.showinfo("Selct","Please select any person")
            self.destroy()
            MyPeople()
            