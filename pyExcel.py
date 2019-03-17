import tkinter as tk
from tkinter import StringVar, ttk, Menu
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import font  as tkfont
from HomePage import HomePage
from ProjectPage import ProjectPage
from SettingsPage import SettingsPage
from FileService import FileService
from DataService import DataService


class PyExcel(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.currentFile = None
        self.files = []
        self.DataService = DataService()
        self.FileService = FileService()
        self.entryList = []
        self.nominalList = []
        self.deptList=[]
        self.tkvar = StringVar()
        menu = Menu(self.master)
        self.config(menu=menu)
        file = Menu(menu)
        file.add_command(label='Import File', command=FileService.loadFile)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        func = Menu(menu)
        menu.add_cascade(label="Functions", menu=func)
        self.page = StringVar()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (HomePage, ProjectPage, SettingsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


    def client_exit(self):
        exit()


    def importFile(self):
        self.currentFile = self.FileService.loadFile()
        self.files.append(self.currentFile)
        self.getWorkbookInfo(self.currentFile)        


    def getWorkbookInfo(self, wb):
        self.DataService.printSheetTitles(wb)
        print("Sheet Row Count: " + str(self.DataService.getRowCount(wb, "Sheet1")))


if __name__ == "__main__":
    app = PyExcel()
    app.geometry("800x600")
    app.mainloop()


        