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
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.homeHeading = tk.Label(self, text="Home Page", font=controller.title_font)
        self.homeHeading.grid(row=0, column=2)
        homeButton = tk.Button(self, command=lambda: controller.show_frame("HomePage"), image = self.homeIcon)
        homeButton.grid(row=0, column=0)
        settingsButton = tk.Button(self, command=lambda: controller.show_frame("SettingsPage"), image = self.settingsIcon)
        settingsButton.grid(row=0, column=4)
        #row1
        fileHeading = tk.Label(self, text="File Operations", font=controller.heading_font)
        fileHeading.grid(row=1, column=2)
        importButton = tk.Button(self, command=lambda: controller.importFile(), image = self.loadIcon)
        importLabel = tk.Label(self, text="Import File")
        importLabel.grid(row=3, column=1)
        importButton.grid(row=2, column=1)
        saveButton = tk.Button(self, command=lambda: controller.FileService.saveFile(controller.currentFile), image = self.saveIcon)
        saveLabel = tk.Label(self, text="Save Sheet")
        saveLabel.grid(row=3, column=3)
        saveButton.grid(row=2, column=3)
        #row2
        projectHeading = tk.Label(self, text="Project Browser", font=controller.heading_font)
        projectHeading.grid(row=4, column=2)
        projectButton = tk.Button(self, command=lambda: controller.show_frame("ProjectPage"), image = self.projectIcon)
        projectButton.grid(row=5, column=2)
        projectLabel = tk.Label(self, text="Projects")
        projectLabel.grid(row=6, column=2)
        
        
