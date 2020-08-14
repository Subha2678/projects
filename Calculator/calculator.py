from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Calculator")
root.geometry("400x650+900+50")
root.config(bg="#00ffff")
root.resizable(FALSE,FALSE)

# ----------------functions--------------------
def enterNumber(x):
    if x=='.':
        if entry_box.get()=='0':
           entry_box.insert(1,'.')
        else:
            all_str=entry_box.get()
            lst_chr=all_str[-1:]
            if lst_chr!='.':
                length=len(entry_box.get())
                entry_box.insert(length,x)

    else:
            if entry_box.get()=='0':
                entry_box.delete(0,END)
                entry_box.insert(1,str(x))
            else:
                length=len(entry_box.get())
                entry_box.insert(length,str(x))

def enter_operator(x):
    if entry_box.get()!='0':
        all_text=entry_box.get()
        last_char=all_text[-1:]
        if last_char in ['+','-','/'] or all_text[-2:]=='**':
            pass
        else: 
            entry_box.insert(len(entry_box.get()),btn_operation[x])

result=0
history=[]
def funOperator():
    content=entry_box.get()
    result=eval(content)
    entry_box.delete(0,END)
    entry_box.insert(0,str(result))
    history.append(content)
    history.reverse()
    status.configure(text="History:" + " | ".join(history[0:4]),font="verdana 11 bold")

def clear_func():
    entry_box.delete(0,END)
    entry_box.insert(0,'0')

def dlt_func():
    if entry_box.get()!='0':
        length=len(entry_box.get())
        entry_box.delete(length-1)
        if length == 1:
            entry_box.insert(0,'0')


def exit_func():
    result=messagebox.askquestion('Exit',"Are you sure?")
    if result=='yes':
        root.quit()


#---------------entry_box-----------------

entry_box=Entry(root,font="verdana 14 bold",width=22,bd=6,bg="#c27ba0",justify=RIGHT)
entry_box.insert(0,"0")
entry_box.place(x=30,y=30)



# ----------------buttons--------------------

btn_numbers=[]
for i in range(0,10):
    btn_numbers.append(Button(width=4,text=str(i),bd=6,bg="#ffff00",command=lambda x=i: enterNumber(x)))

btn_text=1
for i in range(0,3):
    for j in range(0,3):
        btn_numbers[btn_text].place(x=70+j*90,y=100+i*70)
        btn_text+=1



#---------------operator button----------------
btn_operator=[]
btn_operation=['+','-','/','*']
for i in range(4):
    btn_operator.append(Button(text=btn_operation[i],width=4,font="times 15 bold",bd=5,bg="#4a86e8",command=lambda x=i:enter_operator(x)))
for i in range(4):
    btn_operator[i].place(x=110*i,y=370)



# ------------------zero,dot & equal button----------------

btn_zero=Button(width=4,text='0',bd=6,bg="#ffff00",command=lambda x=0: enterNumber(x))
btn_zero.place(x=160,y=310)

btn_dot=Button(width=4,text='.',bd=6,bg="#ffff00",command=lambda x='.': enterNumber(x))
btn_dot.place(x=70,y=310)

btn_equal=Button(width=4,text='=',bd=6,bg="#ffff00",command=funOperator)
btn_equal.place(x=250,y=310)

#----------------------------clear & delete button--------------------

btn_clear=Button(width=14,text="Clear",bd=4,bg='#00ff00',font='impact',command=clear_func)
btn_clear.place(x=25,y=440)

btn_delete=Button(width=14,text="Delete",bd=4,bg='#00ff00',font='impact',command=dlt_func)
btn_delete.place(x=195,y=440)

#--------------------------------status bar---------------------------------
status=Label(root,text="History:",height=3,anchor=W,font="verdana 11 bold",relief=SUNKEN,bd=5)
status.pack(side=BOTTOM,fill=X)

#--------------------------------Exit button--------------------------------------
btn_exit=Button(root,text="EXIT",width=14,bd=6,bg='red',font='impact',command=exit_func)
btn_exit.place(x=120,y=500)

root.mainloop()