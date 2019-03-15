from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from FileService import FileService


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.currentFile = None
        self.entryList = []
        self.nominalList = []
        self.deptList=[]
        self.tkvar = StringVar()
        self.init_window()
        

    def init_window(self):
        self.master.title("pyExcel")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label='Import File', command=FileService.loadFile)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        func = Menu(menu)
        menu.add_cascade(label="Functions", menu=func)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

    # def showImg(self):
    #     load = Image.open('pic.jpg')
    #     render = ImageTk.PhotoImage(load)
    #     img = Label(self, image=render)
    #     img.image = render
    #     img.place(x=0, y=0)

    # def showTxt(self):
    #     text = Label(self, text='PyExcel v0.1a')
    #     text.pack()

    # def populateMenu(self, list):
    #     options = []
    #     for item in list:
    #         options.append(str(item.name))
    #     return options


    # def openFile(self):
    #     filename = askopenfilename()
    #     self.currentFile = FileService.loadFile(filename)
    #     ws = self.currentFile['Sheet1']
    #     DataService.categorise(ws)
    #     self.entryList = DataService.importEntries(self.currentFile, 'Sheet1')
    #     entryLength = IntVar()
    #     entryLength.set(self.entryList.__len__())
    #     self.nominalList = DataService.getList(ws, 3, 4)
    #     nominalLength = IntVar()
    #     nominalLength.set(self.nominalList.__len__()) 
    #     self.deptList = DataService.getList(ws, 1, 2)
    #     deptLength = IntVar()
    #     deptLength.set(self.deptList.__len__())
    #     nominalText = Label(self, text="Unique Nominal Codes: " + str(nominalLength.get()))
    #     nominalText.pack()
    #     deptText = Label(self, text="Unique Departments: " + str(deptLength.get()))
    #     deptText.pack()
    #     entryText = Label(self, text="Unique Postings: " + str(entryLength.get()))
    #     entryText.pack()
    #     # tkvar = StringVar(root)
    #     search = ttk.Combobox(self, state="readonly", textvariable=self.tkvar)
    #     menuChoices = self.populateMenu(self.deptList)
    #     search['values'] = self.populateMenu(self.deptList)
    #     # menuChoices = ['Dept 1', 'Dept 2']
    #     # tkvar.set(menuChoices[0])
    #     print(menuChoices[1])
    #     # popupMenu = OptionMenu(root, tkvar, *menuChoices)
    #     Label(root, text="Choose a Dept").place(x=50, y=250)
    #     # popupMenu.place(x=50, y=300)
    #     search.place(x=50, y=250)
    #     sumText = Label(self, text=("Dept Total"  + (self.getDeptTotal)))
    #     sumText.place(x=200, y=550)
 
    #     def change_dropdown(*args):
    #         print( self.tkvar.get() )

    #     # link function to change dropdown
    #     self.tkvar.trace('w', change_dropdown)
    #     print(filename)

        

    # def getDeptTotal(self):
    #     ws = self.currentFile["Sheet1"]
    #     dept = self.tkvar.get()
    #     total = DataService.sumDept(dept, ws)
    #     return str(total)
        

root = Tk()
root.geometry("800x600")
# DataService = DataService()
app = Window(root)
app.mainloop()