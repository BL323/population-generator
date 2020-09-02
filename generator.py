from GridCells import Cell, CellLoader
from AgeCharacteristics import AgeCharacteristic, AgeCharacteristicLoader
from AgeGroupings import AgeGrouping, AgeGroupingLoader
from PaRUs import PaRU, PaRUsWriter
from itertools import islice

import math

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

# table 4 - load age groups from csv
ag_filename = "InputDataFiles/Table 4 - Age Groupings.csv"
ag_loader = AgeGroupingLoader()
age_groupings = ag_loader.FromCsv(ag_filename)
print("[{0}] age groupings loaded".format(len(age_groupings)))

# global PaRU ID, this variable should be incremented
global paru_id_count
paru_id_count = 0

# global PaRG ID, this variable should be incremented
global parg_id_count
parg_id_count = 0

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

def TakeItems(arry, num):
    output = []
    for j in range(num):
        if(len(arry) > 0):
            output.append(arry.pop())
    return output


def GroupPaRUsForCell(parus_for_cell, age_groupings):
    output_parus_for_cell = []
    parus_ovr65 = list(filter(lambda x: x.Age_Group == "OVR65", parus_for_cell))
    parus_16_65 = list(filter(lambda x: x.Age_Group == "16-65", parus_for_cell))
    parus_0_15 = list(filter(lambda x: x.Age_Group == "0-15", parus_for_cell))

    num_parus_ovr65 = len(parus_ovr65)
    num_parus_16_65 = len(parus_16_65)
    num_parus_0_15 = len(parus_0_15)

    for group in age_groupings:
        target = group.Target
        if target == "OVR65":
            total_in_group = math.floor(num_parus_ovr65 * group.Percentage)
            required_per_group = group.Num_ovr_65
            candidates_in_group = TakeItems(parus_ovr65, total_in_group)

            num_groups = math.floor(total_in_group / required_per_group)
            for i in range(num_groups):
                global parg_id_count
                parg_id_count += 1
                start = i * group.Num_ovr_65
                parg = TakeItems(candidates_in_group, group.Num_ovr_65)
                for paru in parg:
                    paru.SetPargIndex(parg_id_count)
                    output_parus_for_cell.append(paru)

            if(len(candidates_in_group) > 0):
                # create in their own group
                for paru in candidates_in_group:
                    candidates_in_group.remove(paru)
                    parg_id_count += 1
                    paru.SetPargIndex(parg_id_count)
                    output_parus_for_cell.append(paru)



            print("Group: " + group.Group) 
            print("------")

    # ensure any remaining PaRUs in cell are added to a group
    for par_ovr65 in parus_ovr65:
        parus_ovr65.remove(par_ovr65)
        parg_id_count += 1
        par_ovr65.SetPargIndex(parg_id_count)
        output_parus_for_cell.append(par_ovr65)
        

    return output_parus_for_cell, "erff"




parus_writer = PaRUsWriter()

# start the process for each grid cell
isFirstCell = True
for cell in grid_cells:
    print(
        "Processing grid cell #{0}/{1}".format(cell.Grid_Id, len(grid_cells)))
    
    parus_for_cell = GeneratePaRUsForCell(cell, age_characteristics)

    # group parus per cell
    parus_for_cell, pargs_for_cell  = GroupPaRUsForCell(parus_for_cell, age_groupings)

    f = []
    parus_writer.ToCsv(
        "OutputDataFiles/Table 2 - Generated Output.csv", isFirstCell, parus_for_cell)
    isFirstCell = False


print("end...")
