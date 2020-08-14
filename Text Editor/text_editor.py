from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
class text_editor:
    currnt_open_file="no_file"

    def open_file(self):
        open_return=filedialog.askopenfile(initialdir="G:\\",title="Select file to open",filetypes=(("text files","*.txt"),("all files","*.*")))
        if(open_return!=None):
            self.text_area.delete(1.0,END)
            for line in open_return:
                self.text_area.insert(END,line)
            self.currnt_open_file=open_return.name
            open_return.close()



    def save_as(self):
        f=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        if f is None:
            return
        text2save=self.text_area.get(1.0,END)
        f.write(text2save)
        self.currnt_open_file=f.name
        f.close()

    def save_file(self):
        if self.currnt_open_file=="no_file":
            self.save_as()
        else:
            f=open(self.currnt_open_file,"w")
            f.write(self.text_area.get(1.0,END))
            f.close()

    def new_file(self):
        if self.currnt_open_file=="no_file":
            return_value=messagebox.askquestion("save or not",message="Do you want to save current file?")
            if return_value=="yes":
                self.save_file()
            
        self.text_area.delete(1.0,END)
        self.currnt_open_file="no_file"

    def exit_file(self):
        if self.currnt_open_file!="no_file":
            return_value=messagebox.askquestion("save or not",message="Do you want to save current file?")
            if return_value=="yes":
                self.save_file()
        self.master.quit()

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
    
    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")

    def paste_text(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())









    def __init__(self,master):
        self.master=master
        master.title("textpad")
        self.text_area=Text(master,bg="#CCFFFF",undo=True)
        self.text_area.pack(fill=BOTH,expand=1)
        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)

        #creating file menu
        self.file_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="New",command=self.new_file)
        self.file_menu.add_command(label="Open",command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save",command=self.save_file)
        self.file_menu.add_command(label="Save as",command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.exit_file)
        
        #creating edit menu
        self.edit_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu)
        self.edit_menu.add_command(label="cut",command=self.cut_text)
        self.edit_menu.add_command(label="copy",command=self.copy_text)
        self.edit_menu.add_command(label="paste",command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo",command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo",command=self.text_area.edit_redo)


         
root=Tk()
te=text_editor(root)

























root.mainloop()