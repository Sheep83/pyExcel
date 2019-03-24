import tkinter as tk
from tkinter import ttk, Label, IntVar, DoubleVar, StringVar
from openpyxl import Workbook

class ProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        menuChoices = self.controller.DataService.populateMenu(controller.deptList)
        if (controller.deptList.__len__() > 0):
            controller.selectedDept.set(menuChoices[0])
            self.wb = self.controller.currentFile
            self.ws = self.wb["Sheet1"]
        else:
            controller.selectedDept.set("No Data")
        self.deptSum = IntVar()
        self.travelCosts = IntVar()
        self.staffCosts = IntVar()
        self.purchaseCosts = IntVar()
        self.rentCosts = IntVar()
        self.advertCosts = IntVar()
        self.overheadCosts = IntVar()
        self.miscCosts = IntVar()
        self.deptTotals = []
        self.homeIcon = tk.PhotoImage(file='C:/Dev/files/home.png')
        self.settingsIcon = tk.PhotoImage(file='C:/Dev/files/settings.png')
        def onDeptChange(event):
            Label(self, text=" ").grid(row=2, column=1)
            Label(self, text=" ").grid(row=3, column=1)
            Label(self, text=" ").grid(row=4, column=1)
            Label(self, text=" ").grid(row=5, column=1)
            Label(self, text=" ").grid(row=6, column=1)
            print(self.controller.selectedDept.get())
            self.deptTotals = self.controller.DataService.calcCatSums(controller.selectedDept.get(), self.ws)
            for i in range(0, self.deptTotals.__len__()):
                Label(self, text=self.deptTotals[i].name).grid(row=2+i, column=1)
                Label(self, text=self.deptTotals[i].code).grid(row=2+i, column=2)
            # self.deptSum.set(self.controller.DataService.sumDept(controller.selectedDept.get(), self.ws))
            # self.staffCosts.set(self.controller.DataService.sumByCat("Staff Costs", self.ws, controller.selectedDept.get()))
            # self.travelCosts.set(self.controller.DataService.sumByCat("Travel", self.ws, controller.selectedDept.get()))
            # self.rentCosts.set(self.controller.DataService.sumByCat("Rent and Utilities", self.ws, controller.selectedDept.get()))
            # self.advertCosts.set(self.controller.DataService.sumByCat("Advertising", self.ws, controller.selectedDept.get()))
            # self.miscCosts.set(self.controller.DataService.sumByCat("Misc", self.ws, controller.selectedDept.get()))
            # self.overheadCosts.set(self.controller.DataService.sumByCat("Overheads", self.ws, controller.selectedDept.get()))
            # self.purchaseCosts.set(self.controller.DataService.sumByCat("Purchases", self.ws, controller.selectedDept.get()))

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.projectHeading = tk.Label(self, text="Project Page", font=controller.title_font)
        self.projectHeading.grid(row=0, column=2)
        homeButton = tk.Button(self, command=lambda: controller.show_frame("HomePage"), image = self.homeIcon)
        homeButton.grid(row=0, column=0)
        settingsButton = tk.Button(self, command=lambda: controller.show_frame("SettingsPage"), image = self.settingsIcon)
        settingsButton.grid(row=0, column=4)
        search = ttk.Combobox(self, state="readonly", textvariable=self.controller.selectedDept)
        search['values'] = menuChoices
        searchLabel = tk.Label(self, text="Select Dept: ")
        search.configure(width = 50)
        search.grid(row=1, column=2)
        searchLabel.grid(row=1, column=1)
        search.bind("<<ComboboxSelected>>", onDeptChange)
              
        # Label(self, text="Dept Total: ").place(x=0, y=300)
        # Label(self, textvariable=str(self.deptSum)).place(x=125, y=300)
        # Label(self, text="Staff Costs : ").place(x=0, y=350)
        # Label(self, textvariable=str(self.staffCosts)).place(x=125, y=350)
        # Label(self, text="Travel Costs : ").place(x=0, y=375)
        # Label(self, textvariable=str(self.travelCosts)).place(x=125, y=375)
        # Label(self, text="Purchases : ").place(x=0, y=400)
        # Label(self, textvariable=str(self.purchaseCosts)).place(x=125, y=400)
        # Label(self, text="Rent & Utilities : ").place(x=0, y=425)
        # Label(self, textvariable=str(self.rentCosts)).place(x=125, y=425)
        # Label(self, text="Advertising : ").place(x=0, y=450)
        # Label(self, textvariable=str(self.advertCosts)).place(x=125, y=450)
        # Label(self, text="Overheads : ").place(x=0, y=475)
        # Label(self, textvariable=str(self.overheadCosts)).place(x=125, y=475)
        # Label(self, text="Misc Costs : ").place(x=0, y=500)
        # Label(self, textvariable=str(self.miscCosts)).place(x=125, y=500)
        
        
        
        
