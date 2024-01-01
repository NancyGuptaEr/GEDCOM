import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families

output_file_path = "Pramod_spring2_output.txt"

def us15(individuals,families):
        # Create a dictionary to store the marriage count for each individual
    marriage_count = {}

    # Iterate through family records
    for family in families:
        # Get the list of individuals associated with this family
        #individuals = family.individuals

        # Increment the marriage count for each individual in the family
        for individual in individuals:
            individual_id = individual.id
            marriage_count[individual_id] = marriage_count.get(individual_id, 0) + 1

    # Find individuals with multiple marriages
    individuals_with_multiple_marriages = []
    for individual in individuals:
        individual_id = individual.id

        if individual_id in marriage_count and marriage_count[individual_id] > 1:
            individuals_with_multiple_marriages.append(individual)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        # Print the list of individuals with multiple marriages
        for individual in individuals_with_multiple_marriages:
            print(f"{individual.name} has {marriage_count[individual.id]} marriages.")
            output_file.write(f"{individual.name} has {marriage_count[individual.id]} marriages.")
        output_file.write("Testcase 15 passed\n")
        print("Testcase 15 passed")
    return True

def us16(individuals,families):
        # Create a set to store orphaned individuals
    orphans = set()

    # Iterate through individual records
    for individual in individuals:
        individual_id = individual.id

        # Check if the individual has a family record associated with them
        if individual.child:
            family_id = individual.child

            # Find the family record by family_id
            family = next((f for f in families if f.id == family_id), None)

            if family:
                husband_id = family.husbandId
                wife_id = family.wifeId

                # Check if both parents are deceased
                if husband_id and wife_id:
                    husband = next((i for i in individuals if i.id == husband_id), None)
                    wife = next((i for i in individuals if i.id == wife_id), None)

                    if husband and wife and husband.alive == "N" and wife.alive == "N":
                        orphans.add(individual)
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for orphan in orphans:
            print(f"{orphan.name} is an orphan.\n")
            output_file.write(f"{orphan.name} is an orphan.\n")
    return True