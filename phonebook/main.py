from tkinter import *
from datetime import date
from mypeople import MyPeople
from addpeople import AddPerson
today_date=date.today()

class Application(object):
    def __init__(self,master):
        self.master=master

        #frames---------------

        self.top=Frame(master,height=150,bg="#f2f255")
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=500,bg="#599ad4")
        self.bottom.pack(fill=X)

        #top frame design-------------
        self.top_image=PhotoImage(file="icon\\phonebook.png")
        self.top_image_label=Label(self.top,image=self.top_image,bg="#f2f255")
        self.top_image_label.place(x=70,y=15)

        self.heading=Label(self.top,text="My Phonebook App",bg='#f2f255',fg='#db2727',font='Gabriola 26 bold')
        self.heading.place(x=200,y=30)

        self.date_label=Label(self.top,text=f"Today\'s date:{today_date}",bg='#f2f255',fg='#db2727',font='Gabriola 17 bold underline')
        self.date_label.place(x=420,y=5)

        #bottom frame design-------------------------
        self.view_button=Button(self.bottom,text="My people",width=14,bd=10,bg="#c480bc",height=2,font="impact 14",fg='#293030',command=self.my_people)
        self.view_button.place(x=250,y=50)
        self.add_button=Button(self.bottom,text="Add people",width=14,bd=10,bg="#c480bc",height=2,font="impact 14",fg='#293030',command=self.add_person)
        self.add_button.place(x=250,y=150)
        self.about_button=Button(self.bottom,text="About me",width=14,bd=10,bg="#c480bc",height=2,font="impact 14",fg='#293030')
        self.about_button.place(x=250,y=250)
    def my_people(self):
        people= MyPeople()

    def add_person(self):
        AddPerson()   


def main():
    root=Tk()
    root.geometry("650x550+500+120")
    app=Application(root)
    root.title("Phonebook App")
    root.resizable(False,False)
    root.mainloop()
if __name__ == "__main__":
    main()