import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families



def us07(individuals, families):
    for family in families:
        if family.divorced != "NA":
            divorced_date = datetime.strptime(family.divorced, "%Y/%m/%d").date()

            for individual in individuals:
                if individual.id == family.husbandId or individual.id == family.wifeId:
                    marriage_date = datetime.strptime(family.married, "%Y/%m/%d").date()

                    # Check if divorce date is before marriage date
                    if divorced_date < marriage_date:
                        print(f'Error: Divorce date ({divorced_date}) is before marriage date ({marriage_date}) for family {family.id}')
                        return False

    print('User Story 7: Check for Divorce and Remarriage - Passed')
    return True



def us08(individuals, families):
    for family in families:
        for individual in individuals:
            if individual.id == family.husbandId or individual.id == family.wifeId:
                if individual.deathday != "NA":
                    death_date = datetime.strptime(individual.deathday, "%Y/%m/%d").date()

                    for other_family in families:
                        if other_family.id != family.id:
                            if individual.id == other_family.husbandId or individual.id == other_family.wifeId:
                                marriage_date = datetime.strptime(other_family.married, "%Y/%m/%d").date()

                                # Check if death date is before marriage date in any other family
                                if death_date < marriage_date:
                                    print(f'Error: Death date ({death_date}) is before marriage date ({marriage_date}) for individual {individual.id}')
                                    return False

    print('User Story 8: Check for Death and Remarriage - Passed')
    return True




