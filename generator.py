from GridCells import Cell, CellLoader
from AgeCharacteristics import AgeCharacteristic, AgeCharacteristicLoader
from PaRUs import PaRU, PaRUsWriter

# table 1 - load grid cell data from csv
cell_filename = "InputDataFiles/Table 1 - Test.csv"
cell_loader = CellLoader()
grid_cells = cell_loader.FromCsv(cell_filename)

print("[{0}] grid cells loaded".format(len(grid_cells)))

# table 3 - load age characteristics from csv
ac_filename = "InputDataFiles/Table 3 - Age Characteristics.csv"
ac_loader = AgeCharacteristicLoader()
age_characteristics = ac_loader.FromCsv(ac_filename)

print("[{0}] age characteristics loaded".format(len(age_characteristics)))

# global PaRU ID, this variable should be incremented
global paru_id_count
paru_id_count = 0


def LastOrDefault(sequence, default=None):
    lastItem = default
    for s in sequence:
        lastItem = s
    return lastItem


def GeneratePaRUsForCell(grid_cell, age_chars):
    ac_0_15 = LastOrDefault((f for f in age_chars if f.Age_Group == "0-15"))
    parus = GeneratePaRUsForAgeGroup(
        ac_0_15, grid_cell.Grid_Id, grid_cell.Num_0_15)

    ac_16_65 = LastOrDefault((f for f in age_chars if f.Age_Group == "16-65"))
    parus.extend(GeneratePaRUsForAgeGroup(
        ac_16_65, grid_cell.Grid_Id, grid_cell.Num_16_65))

    ac_OVR_65 = LastOrDefault((f for f in age_chars if f.Age_Group == "OVR65"))
    parus.extend(GeneratePaRUsForAgeGroup(
        ac_OVR_65, grid_cell.Grid_Id, grid_cell.Num_ovr_65))

    return parus


def GeneratePaRUsForAgeGroup(age_group, grid_id, num_parus):
    parus = []

    for i in range(num_parus):
        global paru_id_count
        paru_id_count += 1
        parus.append(PaRU(paru_id_count, grid_id, age_group.Age_Group, age_group.PPC, age_group.PPCC, age_group.PLTDA, age_group.PHSDA,
                          age_group.PDVTCA, age_group.PDVDCA, age_group.PSA, age_group.PDEUA, age_group.PDEVA, age_group.PCDVM))
    return parus


parus_writer = PaRUsWriter()


# start the process for each grid cell
isFirstCell = True
for cell in grid_cells:
    print(
        "Processing grid cell #{0}/{1}".format(cell.Grid_Id, len(grid_cells)))
    parus_for_cell = GeneratePaRUsForCell(cell, age_characteristics)
    parus_writer.ToCsv(
        "OutputDataFiles/Table 2 - Generated Output.csv", isFirstCell, parus_for_cell)
    isFirstCell = False


print("end...")
