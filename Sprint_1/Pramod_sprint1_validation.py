import datetime
from datetime import date
from datetime import datetime

#Sprint 1 - Pramod Kanigiri
def UserStory5(individuals,families):

    individuals = {}
    families = {}

    # Iterate through individuals and families
    for individual in individuals:
        individuals[individual.id] = individual

    for family in families:
        families[family.id] = family

    # Create a dictionary to store family information (spouse pairs)
    unique_families = {}

    # Iterate through the families
    for family_id, family in families.items():
        spouses = []
        for spouse_ref in family.spouse_refs:
            spouse_id = spouse_ref.indi_id
            if spouse_id in individuals:
                spouses.append(individuals[spouse_id])
    
        # Ensure there are exactly two spouses (husband and wife)
        if len(spouses) == 2:
            unique_families[family_id] = spouses

    # Print unique families by spouses
    for family_id, spouses in unique_families.items():
        husband, wife = spouses
        print(f"Family ID: {family_id}")
        print(f"Husband: {husband.name}")
        print(f"Wife: {wife.name}")
        print()

def UserStory6(individuals, families):
    # Create a dictionary to store unique first names within families
    unique_first_names_in_families = {}

        # Iterate through individuals
    for individual in individuals:
        # Check if the individual has families
        if families:
            for family_ref in families:
                # Get the family ID
                family_id = family_ref.id

                # Check if the family exists
                if family_id in families:
                    family = families[family_id]

                    # Extract the first name from the individual's name
                    first_name = individual.name.split()[0]

                    # Create a set for the family if it doesn't exist in the dictionary
                    if family_id not in unique_first_names_in_families:
                        unique_first_names_in_families[family_id] = set()

                    # Add the first name to the set of unique first names in this family
                    unique_first_names_in_families[family_id].add(first_name)

    # Print or process the results
    for family_id, first_names in unique_first_names_in_families.items():
        print(f"Family ID: {family_id}")
        print("Unique First Names:")
        for first_name in first_names:
            print(first_name)
        print()