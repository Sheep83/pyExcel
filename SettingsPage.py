import tkinter as tk

class SettingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # tk.geometry("800x600")
        self.controller = controller
        label = tk.Label(self, text="This is the Settings Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Projects",
                            command=lambda: controller.show_frame("ProjectPage"))
        button2 = tk.Button(self, text="Go to Home Page",
                            command=lambda: controller.show_frame("HomePage"))
        button1.pack()
        button2.pack()
