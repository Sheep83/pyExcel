import tkinter as tk
from tkinter import ttk, Label

class ProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Project Browser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        search = ttk.Combobox(self, state="readonly", textvariable=self.controller.selectedDept)
        menuChoices = self.controller.DataService.populateMenu(controller.deptList)
        search['values'] = menuChoices
        if (controller.deptList.__len__() > 0):
            controller.selectedDept.set(menuChoices[0])
        else:
            controller.selectedDept.set("No Data")
        Label(self, text="Choose a Dept").place(x=0, y=250)
        search.place(x=100, y=250)
        button1 = tk.Button(self, text="Go to the Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button2 = tk.Button(self, text="Go to Settings",
                           command=lambda: controller.show_frame("SettingsPage"))
        button3 = tk.Button(self, text="Refresh",
                           command=lambda: controller.refresh())
        button1.pack()
        button2.pack()
        button3.pack()

    