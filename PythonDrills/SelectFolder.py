import os
from tkinter import filedialog
from tkinter import *



class ParentWindow(Frame):
    global folder_path
    def __init__ (self,master):
        Frame.__init__(self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600,200))
        self.master.title('AskDir')
        self.master.config(bg='#fff')


        self.btnSubmit = Button(self.master, text='Submit', width=12, height=2, command=self.submit)
        self.btnSubmit.grid(row=0, column=0,padx=(50,0),pady=(50,0),sticky=N+W)

        self.txtSearch = Entry(self.master,text='',font=('Helvetica',16),fg='black', bg='#FFF')
        self.txtSearch.grid(row=0, column=1,padx=(50,0),pady=(50,0))



        
    def submit(self):
        dir = filedialog.askdirectory()
##        text = Text(root)
        self.txtSearch.insert(END, dir)
        print(dir)
        
##        folder_path.set('C:\Users\chris\OneDrive\Desktop\__pycache__\SelectFolder.py')
##        print('C:\Users\chris\OneDrive\Desktop\__pycache__\SelectFolder.py')
        



if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
