import tkinter as tk
from tkinter import ttk, Label, IntVar, DoubleVar, StringVar
from openpyxl import Workbook

class ProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def onDeptChange(event):
            # wb = Workbook()
            # wb.create_sheet("temp")
            # ws = wb["temp"]
            print(self.controller.selectedDept.get())
            self.deptSum.set(self.controller.DataService.sumDept(controller.selectedDept.get(), self.ws))
            self.staffCosts.set(self.controller.DataService.sumByCat("Staff Costs", self.ws, controller.selectedDept.get()))
            self.travelCosts.set(self.controller.DataService.sumByCat("Travel", self.ws, controller.selectedDept.get()))
            self.rentCosts.set(self.controller.DataService.sumByCat("Rent and Utilities", self.ws, controller.selectedDept.get()))
            self.advertCosts.set(self.controller.DataService.sumByCat("Advertising", self.ws, controller.selectedDept.get()))
            self.miscCosts.set(self.controller.DataService.sumByCat("Misc", self.ws, controller.selectedDept.get()))
            self.overheadCosts.set(self.controller.DataService.sumByCat("Overheads", self.ws, controller.selectedDept.get()))
            self.purchaseCosts.set(self.controller.DataService.sumByCat("Purchases", self.ws, controller.selectedDept.get()))
            # self.projectAnalysis = self.controller.DataService.calcCatSums(self.controller.selectedDept.get(), self.ws)
            # self.updateVars(self.projectAnalysis)
        label = tk.Label(self, text="Project Browser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        search = ttk.Combobox(self, state="readonly", textvariable=self.controller.selectedDept)
        menuChoices = self.controller.DataService.populateMenu(controller.deptList)
        self.deptSum = IntVar()
        self.travelCosts = IntVar()
        self.staffCosts = IntVar()
        self.purchaseCosts = IntVar()
        self.rentCosts = IntVar()
        self.advertCosts = IntVar()
        self.overheadCosts = IntVar()
        self.miscCosts = IntVar()
        # self.travelString = StringVar()
        # self.staffString = StringVar()
        # self.purchaseString = StringVar()
        # self.rentString = StringVar()
        # self.advertString = StringVar()
        # self.overheadString = StringVar()
        # self.miscString = StringVar()
        search['values'] = menuChoices
        if (controller.deptList.__len__() > 0):
            controller.selectedDept.set(menuChoices[0])
            self.wb = self.controller.currentFile
            self.ws = self.wb["Sheet1"]
        else:
            controller.selectedDept.set("No Data")
        Label(self, text="Choose a Dept").place(x=0, y=250)
        Label(self, text="Dept Total: ").place(x=0, y=300)
        Label(self, textvariable=str(self.deptSum)).place(x=125, y=300)
        Label(self, text="Staff Costs : ").place(x=0, y=350)
        Label(self, textvariable=str(self.staffCosts)).place(x=125, y=350)
        Label(self, text="Travel Costs : ").place(x=0, y=375)
        Label(self, textvariable=str(self.travelCosts)).place(x=125, y=375)
        Label(self, text="Purchases : ").place(x=0, y=400)
        Label(self, textvariable=str(self.purchaseCosts)).place(x=125, y=400)
        Label(self, text="Rent & Utilities : ").place(x=0, y=425)
        Label(self, textvariable=str(self.rentCosts)).place(x=125, y=425)
        Label(self, text="Advertising : ").place(x=0, y=450)
        Label(self, textvariable=str(self.advertCosts)).place(x=125, y=450)
        Label(self, text="Overheads : ").place(x=0, y=475)
        Label(self, textvariable=str(self.overheadCosts)).place(x=125, y=475)
        Label(self, text="Misc Costs : ").place(x=0, y=500)
        Label(self, textvariable=str(self.miscCosts)).place(x=125, y=500)
        search.configure(width = 50)
        search.bind("<<ComboboxSelected>>", onDeptChange)
        search.place(x=100, y=250)
        button1 = tk.Button(self, text="Go to the Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button2 = tk.Button(self, text="Go to Settings",
                           command=lambda: controller.show_frame("SettingsPage"))
        # button3 = tk.Button(self, text="Calculate Dept Total(s)",
                        #    command=lambda: controller.DataService.sumDept(str(self.controller.selectedDept), controller.currentFile["Sheet1"]))
        button1.pack()
        button2.pack()
        # button3.pack()
        
        
