import tkinter as tk
from PIL import Image, ImageTk

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.loadIcon = tk.PhotoImage(file='C:/Dev/files/open.png')
        self.saveIcon = tk.PhotoImage(file='C:/Dev/files/save.png')
        self.homeIcon = tk.PhotoImage(file='C:/Dev/files/home.png')
        self.projectIcon = tk.PhotoImage(file='C:/Dev/files/projects.png')
        self.settingsIcon = tk.PhotoImage(file='C:/Dev/files/settings.png')
        # self.analyseIcon = tk.PhotoImage(file='C:/Dev/files/analyse.png')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        label = tk.Label(self, text="Home Page", font=controller.title_font)
        label.grid(row=0, column=1, pady=10)
        #row1
        heading1 = tk.Label(self, text="File Operations", font=controller.heading_font)
        heading1.grid(row=1, column=1)
        button3 = tk.Button(self, text="Import", command=lambda: controller.importFile(), image = self.loadIcon)
        heading3 = tk.Label(self, text="Import File")
        heading3.grid(row=3, column=0)
        # button4 = tk.Button(self, text="Analyse Sheet", command=lambda: controller.DataService.categorise(controller.currentFile["Sheet1"], controller.optionsFile["ChartOfAccounts"]), image = self.analyseIcon)
        # heading4 = tk.Label(self, text="Analyse Sheet")
        # heading4.grid(row=3, column=1)
        button5 = tk.Button(self, text="Save Analysed Sheet", command=lambda: controller.FileService.saveFile(controller.currentFile), image = self.saveIcon)
        heading5 = tk.Label(self, text="Save Sheet")
        heading5.grid(row=3, column=2)
        button3.grid(row=2, column=0, pady=5)
        # button4.grid(row=2, column=1, pady=5)
        button5.grid(row=2, column=2, pady=5)
        #row2
        heading2 = tk.Label(self, text="Project Browser", font=controller.heading_font)
        heading2.grid(row=4, column=1)
        button1 = tk.Button(self, text="Projects", command=lambda: controller.show_frame("ProjectPage"), image = self.projectIcon)
        button1.grid(row=5, column=1, pady=5)
        heading6 = tk.Label(self, text="Projects")
        heading6.grid(row=6, column=1)
        button2 = tk.Button(self, text="Go to Settings", command=lambda: controller.show_frame("SettingsPage"), image = self.settingsIcon)
        button2.grid(row=0, column=2, pady=5)
        
