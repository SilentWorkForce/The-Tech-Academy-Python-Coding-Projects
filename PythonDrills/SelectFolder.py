import os
from tkinter import filedialog
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600,200))
        self.master.title('AskDir')
        self.master.config(bg='#fff')


        self.btnSubmit = Button(self.master, text='Select Folder', width=12, height=2, command=self.submit)
        self.btnSubmit.grid(row=0, column=0,padx=(50,0),pady=(50,0),sticky=N+W)

        self.txtSearch = Entry(self.master,text='',font=('Helvetica',16),fg='black', bg='#FFF')
        self.txtSearch.grid(row=0, column=1,padx=(50,0),pady=(50,0))

        
    def submit(self):
        global folder_path
        dir = filedialog.askdirectory()
        folder_path.set(filename)
        print(filename)
        folder_path = 



if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
