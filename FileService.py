from openpyxl import load_workbook
from tkinter.filedialog import askopenfilename, asksaveasfilename

class FileService():
    def __init__(self):
        self.currentFile = None
    
    def loadFile(self):
        filename = askopenfilename()
        self.currentFile = load_workbook(filename)
        print("File Loaded")
        return self.currentFile

    def saveFile(self, wb):
        filename = asksaveasfilename()
        wb.save(filename + ".xlsx")
        print("File Saved!")
