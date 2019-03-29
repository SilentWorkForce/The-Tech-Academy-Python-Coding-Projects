

import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 175))
        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lblFName = Label(self.master,text='', font=('Helvetica', 16), fg='black', bg='#FFF' )
        self.lblFName.grid(row=8, column=0,padx=(25,0),pady=(10,0))
        
        self.lblLName = Label(self.master,text='', font=('Helvetica', 16), fg='black', bg='#FFF' )
        self.lblLName.grid(row=8, column=0,padx=(25,0),pady=(10,0))

        self.lblDisplay = Label(self.master,text='', font=('Helvetica', 16), fg='black', bg='#FFF')
        self.lblDisplay.grid(row=3, column=1,padx=(25,0),pady=(10,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=('Helvetica', 16), fg='black', bg='#FFF')
        self.txtFName.grid(row=0, column=1,padx=(25,0),pady=(10,0))
        
        self.txtLName = Entry(self.master,text=self.varLName, font=('Helvetica', 16), fg='black', bg='#FFF')
        self.txtLName.grid(row=1, column=1,padx=(25,0),pady=(10,0))

        self.btnBrowse = Button(self.master, text='Browse', width=12, height=1, command=self.submit)
        self.btnBrowse.grid(row=0, column=0,padx=(25,0),pady=(10,0),sticky=N+W)
        
        self.btnBrowse = Button(self.master, text='Browse', width=12, height=1, command=self.submit)
        self.btnBrowse.grid(row=1, column=0,padx=(25,0),pady=(10,0),sticky=N+W)

        self.btnChk = Button(self.master, text='Check for files...', width=12, height=2, command=self.submit)
        self.btnChk.grid(row=2, column=0,padx=(25,0),pady=(10,0),sticky=N+W)


        self.btnCancel = Button(self.master, text='Close Program', width=12, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(25,0),pady=(10,0),sticky=N+E)


    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Checking... {} {}'.format(fn,ln))

    def cancel(self):
        self.master.destroy()




if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
