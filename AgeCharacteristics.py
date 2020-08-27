import csv

class AgeCharacteristic:
    Age_Group = ""
    X = -9999
    Y = -9999
    Elevation = -9999
    ID = 0
    PARGINDEX = 0
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

    def __init__(self, age_group, pcc, ppcc, pltda, phsda, pdvtca, pdvdca, psa, pdeua, pdeva, pcdvm):
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

class AgeCharacteristicLoader:
    def FromCsv(self, filename):
        print("Loading age characteristics from [{0}]".format(filename))
        characteristics = []
        with open(filename) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            csvfile.readline()
            for row in csvReader:
                characteristics.append(AgeCharacteristic(row[0], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))

        return characteristics
