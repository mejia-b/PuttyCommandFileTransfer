import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import subprocess

#Gui setup
root = tk.Tk()
root.title("Putty Command File Transfer")
root.geometry("400x300")
#////////////////////////////////////////////////////////
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',show=""):
        super().__init__(master,cnf={},show=show)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    global filename

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
   
def run_command():
    pass
#////// Variables ////////
option = tk.StringVar()


#////////////////////// CREATE WIDGETS //////////////////////////  
# create input box which will display the path chosen
input_path = EntryWithPlaceholder(root,"Select a Path")
#create remote_path entr box
remote_path = EntryWithPlaceholder(root,"Remote Path")
#create username input box
username_input = EntryWithPlaceholder(root,"Username")
#create address input box
address_input = EntryWithPlaceholder(root,"Address")
# create password input box
password_input = EntryWithPlaceholder(root,"Password",show="*")
# select path button 
select_button = ttk.Button(root,text='Select Path',command=select_file)
# run command button
run_button = ttk.Button(root,text="Run command",command = run_command)
# radio option source
source_radio = ttk.Radiobutton(root,text="Source",value= "S",variable=option)
# radio option destination
destination_radio = ttk.Radiobutton(root,text="Destination",value="D",variable=option)

#//////////// PLACE IN WINDOW ///////////////////////////////////////////////
# display the path chosen from pressing select path button
input_path.place(x=50,y=50)
# enter remote path
remote_path.place(x=50,y=80)
# username input box
username_input.place(x=50,y=130)
# address input box
address_input.place(x=50,y=160)
# password input box -> once command is run 
# successfuly it will require the password
# in order to transfer the folder(s)/file(s)
password_input.place(x=50,y=190)
# select button will allow for choosing a file path
select_button.place(x=190,y=47)
# radio option source
source_radio.place(x=280,y=40)
# radio option destination
destination_radio.place(x=280,y=60)



# run the application
root.mainloop()













