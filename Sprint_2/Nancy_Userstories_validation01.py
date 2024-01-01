import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 2 - Nancy Gupta

# us10 birth before death
def us10(individuals,families):
    for individual in individuals:
        birthdate = individual.birthday.split("/")
        date_of_birth = date(
                        int(birthdate[0]),
                        int(birthdate[1]),
                        int(birthdate[2]))
        
        if individual.alive == False:
            deathdate = individual.deathday.split("/")
            date_of_death = date(
                        int(deathdate[0]),
                        int(deathdate[1]),
                        int(deathdate[2]))
            if date_of_birth > date_of_death:
                print('Error : Birth should be before death of an individual.')
                return False
                
    print('Test 10 passed succesfully')
    return True

# us09 less than 150 years old
def us09(individuals, families):
    for individual_person in individuals:
        birthdate = individual_person.birthday.split("/")
        date_of_birth = date(
                            int(birthdate[0]),
                            int(birthdate[1]),
                            int(birthdate[2]))
        is_alive = individual_person.alive

        if is_alive == 'True':
            # Check if death date is provided, if not, skip the check
            if individual_person.deathday != 'NA':
                deathdate = individual_person.deathday.split("/")
                date_of_death = date(int(deathdate[0]), int(deathdate[1]), int(deathdate[2]))
                if individual_person.age > 150:
                    print("ERROR: INDIVIDUAL: US07: More than 150 years old at Death - Birth {} : Death {}".format(birthdate, deathdate))
                    return False
        else:
            # Check if death date is provided and not 'NA', if not, skip the check
            if individual_person.deathday != 'NA':
                deathdate = individual_person.deathday.split("/")
                date_of_death = date(
                                int(deathdate[0]),
                                int(deathdate[1]),
                                int(deathdate[2]))
                # Check the age considering the birth and death dates
                if individual_person.age > 150:
                    print("ERROR: INDIVIDUAL: US07: More than 150 years old at Death - Birth {} : Death {}".format(birthdate, deathdate))
                    return False           
    print('Test 9 passed successfully')
    return True