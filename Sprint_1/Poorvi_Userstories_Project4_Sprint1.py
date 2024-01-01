import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 1 -Poorvi Raut

# User Story 11: Number of Divorces in the Family
def us12(families):
    num_divorces = 0
    for family in families:
        if family.divorced != "NA":
            num_divorces += 1
    print(f'Number of divorces in the family: {num_divorces}')
    return num_divorces

# User Story 12: Unique Last Names in the Family
def us12(individuals):
    last_names = set()
    for individual in individuals:
        name_parts = individual.name.split()
        if len(name_parts) >= 2:
            last_name = name_parts[-1]
            last_names.add(last_name)
    
    if len(last_names) == len(individuals):
        print('All individuals have unique last names.')
        return True
    else:
        print('Error: Not all individuals have unique last names.')
        return False






