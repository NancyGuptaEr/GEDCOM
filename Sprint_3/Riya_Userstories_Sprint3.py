import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families




#Sprint 3 - Riya Divakaran


def us21(families, individuals):
    """
    Ensure that the spouse in a family has the correct gender.

    :param families: List of family objects
    :param individuals: List of individual objects
    :return: True if spouses have the correct gender, False otherwise
    """
    for family in families:
        husband_id = family.husbandId
        wife_id = family.wifeId

        husband = next((ind for ind in individuals if ind.id == husband_id), None)
        wife = next((ind for ind in individuals if ind.id == wife_id), None)

        # Ensure both husband and wife exist and have the correct gender
        if husband and wife:
            if husband.gender == 'F':
                print(f"ERROR: US21: Husband {husband.name} (ID: {husband.id}) in family {family.id} has the incorrect gender.")
                return False

            if wife.gender == 'M':
                print(f"ERROR: US21: Wife {wife.name} (ID: {wife.id}) in family {family.id} has the incorrect gender.")
                return False

    print("US21: Spouses have the correct gender.")
    return True

def us22(individuals, families):
    all_ids = set()
    non_unique_ids = []

    # Checking individual IDs
    for ind in individuals:
        ind_id = ind.id
        if ind_id in all_ids:
            non_unique_ids.append(ind_id)
        else:
            all_ids.add(ind_id)

    # Checking family IDs
    for family in families:
        family_id = family.id
        if family_id in all_ids:
            non_unique_ids.append(family_id)
        else:
            all_ids.add(family_id)

    if non_unique_ids:
        print(f"ERROR: US22: Non-unique IDs found: {', '.join(non_unique_ids)}")
        return False
    else:
        print("US22: All IDs are unique.")
        return True

