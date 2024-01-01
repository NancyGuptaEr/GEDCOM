from tkinter.font import families
import unittest
import datetime
import unittest
from gedcom_parser import individual_parser, family_parser
from Riya_Userstories_Sprint3 import us21, us22

# Load individuals and families from GEDCOM file
individuals = individual_parser("gedcom_test.ged")
families = family_parser("gedcom_test.ged")

class TestUserStorySpouseGender(unittest.TestCase):
    def setUp(self):
        self.individuals = individual_parser("gedcom_test.ged")
        self.families = family_parser("gedcom_test.ged")

    def test_spouse_gender(self):
        result = us21(self.families, self.individuals)
        self.assertTrue(result, "Spouses have correct genders.")
        

    def test_us22(self):
        individuals = individual_parser("gedcom_test.ged")
        families = family_parser("gedcom_test.ged")

        result = us22(individuals, families)
        self.assertTrue(result, "US22 failed: Non-unique IDs found.")
if __name__ == '__main__':
    unittest.main()