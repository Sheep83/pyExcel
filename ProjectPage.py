import tkinter as tk

class ProjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Project Browser", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the Home Page",
                           command=lambda: controller.show_frame("HomePage"))
        button2 = tk.Button(self, text="Go to Settings",
                           command=lambda: controller.show_frame("SettingsPage"))
        button1.pack()
        button2.pack()