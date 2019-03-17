import tkinter as tk

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Home Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Projects", command=lambda: controller.show_frame("ProjectPage"))
        button2 = tk.Button(self, text="Go to Settings", command=lambda: controller.show_frame("SettingsPage"))
        button3 = tk.Button(self, text="Import File", command=lambda: controller.importFile())
        # button3.config(height = 10, width = 10)
        button4 = tk.Button(self, text="Analyse Sheet", command=lambda: controller.DataService.categorise(controller.currentFile["Sheet1"]))
        button5 = tk.Button(self, text="Save Analysed Sheet", command=lambda: controller.FileService.saveFile(controller.currentFile))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
