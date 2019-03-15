from openpyxl import load_workbook
# from Window import *
# from Posting import *
# from ListItem import *
from tkinter.filedialog import askopenfilename


class FileService():
    def __init__(self):
        self.currentFile = None
    
    def loadFile(self):
        filename = askopenfilename()
        # self.currentFile = DataService.openFile(filename)
        self.currentFile = load_workbook(filename)
        return self.currentFile