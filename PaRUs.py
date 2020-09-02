import csv

class PaRU:
    ID = -1
    Grid_Number = -1
    Age_Group = ""
    X = -9999
    Y = -9999
    Elevation = -9999
    PPC = 0
    PPCC = 0
    PLTDA = 0
    PHSDA = 0
    PDVTCA = 0
    PDVDCA = 0
    PSA = 0
    PDEUA = 0
    PDEVA = 0
    PCDVM = 0
    PARGINDEX = -1

    def __init__(self, id, grid_number, age_group, pcc, ppcc, pltda, phsda, pdvtca, pdvdca, psa, pdeua, pdeva, pcdvm):
        self.ID = id
        self.Grid_Number = grid_number
        self.Age_Group = age_group
        self.PCC = pcc
        self.PPCC = ppcc
        self.PLTDA = pltda
        self.PHSDA = phsda
        self.PDVTCA = pdvtca
        self.PDVDCA = pdvdca
        self.PSA = psa
        self.PDEUA = pdeua
        self.PDEVA = pdeva
        self.PCDVM = pcdvm

    def SetPargIndex(self, pargIdx):
        self.PARGINDEX = pargIdx

    def GetAgeGroupInOutputFormat(self):
        if self.Age_Group == "OVR65":
            return "65+"

        return self.Age_Group


class PaRUsWriter:
    def ToCsv(self, filename, includeHeader, parus):
        with open(filename, mode='a') as paru_file:
            paru_writer = csv.writer(
                paru_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if includeHeader:
                paru_writer.writerow(['Age Group','Grid Number','X','Y','Elevation','ID','PARGINDEX','PPC','PPCC','PLTDA','PHSDA','PDVTCA','PDVDCA','PSA','PDEUA','PDEVA','PCDVM'])
            
            for p in parus:
                paru_writer.writerow([p.GetAgeGroupInOutputFormat(), p.Grid_Number, p.X, p.Y, p.Elevation, p.ID, p.PARGINDEX, p.PPC, p.PPCC, p.PLTDA, p.PHSDA, p.PDVTCA, p.PDVDCA, p.PSA, p.PDEUA, p.PDEVA, p.PCDVM])
