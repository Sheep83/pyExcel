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

        label = tk.Label(self, text="Project Browser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        search = ttk.Combobox(self, state="readonly", textvariable=self.controller.selectedDept)
        menuChoices = self.controller.DataService.populateMenu(controller.deptList)
        self.deptSum = IntVar()
        self.staffCosts = IntVar()
        self.travelCosts = IntVar()
        search['values'] = menuChoices
        if (controller.deptList.__len__() > 0):
            controller.selectedDept.set(menuChoices[0])
            self.wb = self.controller.currentFile
            self.ws = self.wb["Sheet1"]
        else:
            controller.selectedDept.set("No Data")
        Label(self, text="Choose a Dept").place(x=0, y=250)
        Label(self, text="Dept Total: ").place(x=0, y=350)
        Label(self, textvariable=str(self.deptSum)).place(x=125, y=350)
        Label(self, text="Staff Costs Total: ").place(x=0, y=400)
        Label(self, textvariable=str(self.staffCosts)).place(x=125, y=400)
        Label(self, text="Travel Costs Total: ").place(x=0, y=450)
        Label(self, textvariable=str(self.travelCosts)).place(x=125, y=450)

        search.configure(width = 50)
        search.bind("<<ComboboxSelected>>", onDeptChange)
        search.place(x=100, y=250)
        button1 = tk.Button(self, text="Go to the Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button2 = tk.Button(self, text="Go to Settings",
                           command=lambda: controller.show_frame("SettingsPage"))
        button3 = tk.Button(self, text="Calculate Dept Total(s)",
                           command=lambda: controller.DataService.sumDept(str(self.controller.selectedDept), controller.currentFile["Sheet1"]))
        button1.pack()
        button2.pack()
        button3.pack()
        
        
