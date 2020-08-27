import csv

class Cell:
    Grid_Id = 0
    Num_0_15 = 0
    Num_16_65 = 0
    Num_ovr_65 = 0

    def __init__(self, grid_id, num_0_15, num_16_65, num_ovr_65):
        self.Grid_Id =  int(grid_id)
        self.Num_0_15 = int(num_0_15)
        self.Num_16_65 = int(num_16_65)
        self.Num_ovr_65 = int(num_ovr_65)

class CellLoader:
    def FromCsv(self, filename):
        print("Loading grid cells from [{0}]".format(filename))
        cells = []
        with open(filename) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            csvfile.readline()
            for row in csvReader:
                cells.append(Cell(row[0], row[1], row[2], row[3]))

        return cells
            