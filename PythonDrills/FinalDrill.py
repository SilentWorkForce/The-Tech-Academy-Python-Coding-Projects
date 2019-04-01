from os.path import join
import shutil
import sqlite3
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

        self.btnSelect = Button(self.master, text='Select', width=12, height=2, command=self.select)
        self.btnSelect.grid(row=1, column=0,padx=(50,0),pady=(25,0),sticky=N+W)

        self.txtSearch = Entry(self.master,text='',font=('Helvetica',16),fg='black', bg='#FFF')
        self.txtSearch.grid(row=0, column=1,padx=(50,0),pady=(50,0))

        self.txtSearch = Entry(self.master,text='',font=('Helvetica',16),fg='black', bg='#FFF')
        self.txtSearch.grid(row=1, column=1,padx=(50,0),pady=(25,0))

    def submit(self):
        dir = filedialog.askdirectory()
        self.txtSearch.insert(END, dir)
        print(dir)
        import os
        files = os.listdir('C:\PyProjects')   
        time = os.path.getmtime('C:\PyProjects')
        for file in os.listdir('C:\\PyProjects\\'):
            if file.endswith(".txt"):
                print(os.path.join,("/PyProjects", file,))
        path = 'C:\PyProjects'
        name_list = os.listdir(path)
        full_list = [os.path.join(path,i) for i in name_list]
        time_sorted_list = sorted(full_list, key=os.path.getmtime)
        print (time_sorted_list)

       
    def select(self):
        source = join('C', 'PyProjects', 'Drill5.txt', 'Drill6.txt', 'Drill7.txt')
        destination = join('D', 'Final')
        shutil.move(source, destination)


for file in os.listdir('C:\PyProjects'):
    if file.endswith('.txt'):
        print(os.path.join("/PyProjects", file,))
     

        
##        source = os.listdir("C:/PyProjects/")
##        destination = ("D:/Final/")
##        shutil.copy('C:/PyProjects/Drill4.txt','C:/PyProjects/Drill5.txt')
##        shutil.move(r'C:/PyProjects/Drill4.txt','C:/PyProjects/Drill5.txt')
##        for files in source:
##            if files.endswith(".txt"):
##                shutil.copy(files,destination)
        



if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
