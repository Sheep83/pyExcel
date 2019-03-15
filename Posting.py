class Posting:
    def __init__(self, row):
        self.deptCode = row[0].value
        self.deptName = row[1].value
        self.nominalCode = row[2].value
        self.nominalName = row[3].value
        self.date = row[4].value
        self.narrative = row[5].value
        self.blank = row[6].value
        self.transValue = row[7].value
        self.cat = row[8].value