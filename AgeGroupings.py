import csv

class AgeGrouping:
    Group = ""
    Target = ""
    Percentage = 0
    Num_0_15 = 0
    Num_16_65 = 0
    Num_ovr_65 = 0

    def __init__(self, group, target, percentage, num_0_15, num_16_65, num_ovr_65):
        self.Group = group
        self.Target = target
        self.Percentage = float(percentage)
        self.Num_0_15 = int(num_0_15)
        self.Num_16_65 = int(num_16_65)
        self.Num_ovr_65 = int(num_ovr_65)

class AgeGroupingLoader:
    def FromCsv(self, filename):
        print("Loading age groupings from [{0}]".format(filename))
        groups = []

        with open(filename) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
            csvfile.readline()
            for row in csvReader:
                groups.append(AgeGrouping(row[0], row[1], row[2], row[3], row[4], row[5]))

        return groups