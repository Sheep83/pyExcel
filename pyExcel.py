import tkinter as tk
from tkinter import StringVar, ttk, Menu, IntVar
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import font  as tkfont
from HomePage import HomePage
from ProjectPage import ProjectPage
from SettingsPage import SettingsPage
from FileService import FileService
from DataService import DataService
from openpyxl import load_workbook


class PyExcel(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.currentFile = None
        # path = 'C:\Dev\Python\pyExcel\files\optionsFile.xlsx'
        self.files = []
        self.DataService = DataService()
        self.FileService = FileService()
        # self.entryList = None
        # self.optionsFile = self.FileService.loadFile()
        self.optionsFile = load_workbook('C:/Dev/files/optionsFile.xlsx')
        self.nominalList = None
        self.deptList = []
        self.selectedDept = StringVar()
        self.selectedDept.set("")
        self.deptSum = IntVar()
        menu = Menu(self.master)
        self.config(menu=menu)
        file = Menu(menu)
        file.add_command(label='Import File', command=FileService.loadFile)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        func = Menu(menu)
        menu.add_cascade(label="Functions", menu=func)
        self.page = StringVar()
        self.frames = {}
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        for F in (HomePage, ProjectPage, SettingsPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")


    def show_frame(self, page_name):
        self.refresh()
        frame = self.frames[page_name]
        frame.tkraise()


    def client_exit(self):
        exit()

    def refresh(self):
        self.container.destroy()
        self.frames = {}
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        for F in (HomePage, ProjectPage, SettingsPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        
    def importFile(self):
        self.currentFile = self.FileService.loadFile()
        self.files.append(self.currentFile)
        self.getWorkbookInfo(self.currentFile)


    def getWorkbookInfo(self, wb):
        self.DataService.printSheetTitles(wb)
        print("Sheet Row Count: " + str(self.DataService.getRowCount(wb, "Sheet1")))
        self.deptList = self.DataService.getList(wb["Sheet1"], 1, 2)


if __name__ == "__main__":
    app = PyExcel()
    app.geometry("800x600")
    app.mainloop()


        