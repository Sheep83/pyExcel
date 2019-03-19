from Posting import Posting
from ListItem import ListItem

class DataService():
    def __init__(self):
        self.wb = None


    def printSheetTitles(self, wb):
        for sheet in wb:
            print(sheet.title)


    def getRow(self, ws, rowno):
        # ws = wb[sheetName]
        newRow = ws[rowno]
        return newRow


    def getRowCount(self, wb, sheetName):
        ws = wb[sheetName]
        return ws.max_row


    def getEntriesByDept(self, ws, dept):
        entryList = []
        for i in range (1, ws.max_row):
            if(ws.cell(i, 2).value == dept):
                newEntry = Posting(self.getRow(ws, i))
                entryList.append(newEntry)
        print(entryList.__len__())
        return entryList


    def categorise(self, ws, options):
        for i in range(1, ws.max_row+1):
            cell = ws.cell(i, 3)
            for j in range(1, options.max_row+1):
                cell2 = options.cell(j, 1)
                if (cell.value == cell2.value):
                    ws.cell(i, 8).value = options.cell(j, 3).value
                    # break
        print("Done!")
        

    def searchByNominal(self, entryList, nominalCode):
        filteredList = []
        for item in entryList:
            if item.nominalCode == nominalCode:
                filteredList.append(item)
        return filteredList


    def getList(self, ws, codeCol, nameCol):
        found = False
        list = []
        initCode = ws.cell(1, codeCol).value
        initName = ws.cell(1, nameCol).value
        list.append(ListItem(initCode, initName))
        for i in range(2, ws.max_row):
            itemCode = ws.cell(i, codeCol).value
            itemName = ws.cell(i, nameCol).value
            for item in list:
                if item.code == itemCode:
                    found = True
                else:
                    found = False
            if found == False:
                newItem = ListItem(itemCode, itemName)
                list.append(newItem)
        return list


    def writeList(self, wb, list, row, column, sheetname):
        newWs = wb.create_sheet(sheetname)
        i = 0
        for item in list:
            newWs.cell(row + i, column).value = item.code
            newWs.cell(row + i, column + 1).value = item.name
            i += 1


    def writeEntryList(self, wb, entryList, col1, sheetname):
        newWs = wb.create_sheet(sheetname)
        for i in range(1, entryList.__len__()):
            newWs.cell(i, 1).value = entryList[i].nominalCode
            newWs.cell(i, 2).value = entryList[i].transValue


    def sumDept(self, dept, ws):
        deptTotal = 0
        for i in range(1, ws.max_row):
            value = ws.cell(i, 2).value
            if value == dept:
                deptTotal += ws.cell(i, 7).value
        print (str(deptTotal))
        return deptTotal


    def populateMenu(self, list):
        options = []
        if (list.__len__() > 0):
            for item in list:
                options.append(str(item.name))
        return options


    def sumByCat(self, cat, ws, dept):
        catTotal = 0
        for i in range(1, ws.max_row):
            value = ws.cell(i, 8).value
            deptValue = ws.cell(i,2).value
            if (value == cat) and (deptValue == dept):
                catTotal += ws.cell(i, 7).value
        print (cat + " Total : " + str(catTotal))            
        return catTotal
