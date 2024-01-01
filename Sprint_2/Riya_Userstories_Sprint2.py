import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families




#Sprint 2 - Riya Divakaran


def us13(individuals):
    """
    Check if there are multiple individuals with the same birth date in the family tree.


    :param individuals: List of individual objects
    :return: True if there are multiple births on the same day, False otherwise
    """
    birth_dates = {}  # Dictionary to store birth dates and corresponding individuals


    for individual in individuals:
        birth_date = individual.birthday


        if birth_date in birth_dates:
            birth_dates[birth_date].append(individual)
        else:
            birth_dates[birth_date] = [individual]


    for date, individuals_list in birth_dates.items():
        if len(individuals_list) > 1:
            print(f"ERROR: US13: Multiple individuals born on the same day {date}:")
            for individual in individuals_list:
                print(f"  - {individual.id}: {individual.name}")
            return False


    print("US13: No multiple births on the same day detected.")
    return True


               
def us14(individuals, families):
    """
    Check if the age difference between spouses in a family is less than 80 years.


    :param individuals: List of individual objects
    :param families: List of family objects
    :return: True if the age difference is less than 80 years, False otherwise
    """
    for family in families:
        husband_id = family.husbandId
        wife_id = family.wifeId


        husband = next((ind for ind in individuals if ind.id == husband_id), None)
        wife = next((ind for ind in individuals if ind.id == wife_id), None)


        if husband and wife:
            husband_birth_date = datetime.strptime(husband.birthday, "%Y/%m/%d").date()
            wife_birth_date = datetime.strptime(wife.birthday, "%Y/%m/%d").date()
            marriage_date = datetime.strptime(family.married, "%Y/%m/%d").date()


            if abs((husband_birth_date - marriage_date).days) > 29200:  # 80 years in days
                print(f"ERROR: US14: Age difference between spouses in Family {family.id} is more than 80 years:")
                print(f"  - Husband: {husband.name} (Birthdate: {husband.birthday})")
                print(f"  - Wife: {wife.name} (Birthdate: {wife.birthday})")
                return False


    print("US14: Age difference between spouses is within acceptable limits (<= 80 years).")
    return True