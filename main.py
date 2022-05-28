import tkinter as tk
from tkinter import ttk # library for modern themed widgets
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import subprocess

#Gui setup
root = tk.Tk()
root.title("Putty Command File Transfer")
root.geometry("400x300")
#////////////////////////////////////////////////////////
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',show="",textvariable="",command=None):
        super().__init__(master,cnf={},show=show,textvariable=textvariable)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
    # when select path button is clicked and user selects the file path
    # this function can be used to display the path on to the EntryWithPlaceholder instance widget
    def display_path(self,text):
        self.delete('0','end')
        self.insert(0,text)
        self['fg'] = 'black'
    # wrapper function that gets the text from the EntryWithPlaceholder instance
    def get_text(self):
        return self.get()

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

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    filename = '"' + filename + '"'
    input_path.display_path(text=filename)
   
def run_command():
    if option.get() == 'S':
        command = fr'pscp -P 22 -pw {password_input.get_text()} {input_path.get_text()} {username_input.get_text()}@{address_input.get_text()}:/{second_path.get_text()}'
        print(command)
        subprocess.run(command,shell=True)
        print("Command was run successfully!")
    elif option.get() == 'D':
        command = fr'pscp -P 22 -pw {password_input.get_text()}  {username_input.get_text()}@{address_input.get_text()}:/{second_path.get_text()} {input_path.get_text()}'
        print(command)
        subprocess.run(command,shell=True)
        print("Command was run successfully!")

#////// Variables ////////
option = tk.StringVar()
filename = tk.StringVar()


#////////////////////// CREATE WIDGETS //////////////////////////  
# create input box which will display the path chosen
input_path = EntryWithPlaceholder(root,"Select a Path")
#create remote_path entry box
second_path = EntryWithPlaceholder(root,"Second Path")
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
second_path.place(x=50,y=80)
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
# run button to run subprocess command
run_button.place(x=150,y=250)



# run the application
root.mainloop()













