import csv

class PaRG:
    Elevation = -9999
    ID = 0
    GroupType = 1
    TravelMode = 2
    BuildingIndex = 0
    RoadIndex = -9999
    LaneIndex = -9999
    LanePos = -9999
    TFAF = 28800
    IUETA = 900
    VEVT = 60
    VDVFC = 0.6
    VDVTC = 0.8
    VSDC = 0.3
    EvacMode = 0

    def __init__(self, id, buildingIndex):
        self.ID = id
        self.BuildingIndex = buildingIndex

class PaRGsWriter:
    def ToCsv(self, filename, includeHeader, pargs):
        with open(filename, mode='a') as parg_file:
            parg_writer = csv.writer(
                parg_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if includeHeader:
                parg_file.writerow(["Elevation","ID","GroupType","TravelMode","BuildingIndex","RoadIndex","LaneIndex","LanePos","TFAF","IUETA","VEVT","VDVFC","VDVTC","VSDC","EvacMode"])
            
            for p in pargs:
                parg_writer.writerow([p.Elevation,p.ID,p.GroupType,p.TravelMode,p.BuildingIndex,p.RoadIndex,p.LaneIndex,p.LanePos,p.TFAF,p.IUETA,p.VEVT,p.VDVFC,p.VDVTC,p.VSDC,p.EvacMode)

    