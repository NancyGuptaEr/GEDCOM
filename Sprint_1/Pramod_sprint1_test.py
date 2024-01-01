
from tkinter.font import families
import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
# from gedcom_parser import us02, us07, us01
from Pramod_sprint1_validation import UserStory5, UserStory6

# Load individuals and families from GEDCOM file
individuals = gedcom_parser.individual_parser("gedcom_test.ged")
families = gedcom_parser.family_parser("gedcom_test.ged")


class TestGedcomFile(unittest.TestCase):

    def test_UserStory5(self):
        # Test that children's births occur before the death of parents
        UserStory5(individuals,families)

    def test_UserStory6(self):
        # Test that children's births occur before the death of parents
        UserStory6(individuals,families)
    

if __name__ == '__main__':
    unittest.main()