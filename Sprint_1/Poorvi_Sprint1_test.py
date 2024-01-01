
from tkinter.font import families
import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
# from gedcom_parser import us02, us07, us01
from Poorvi_Userstories_Sprint1 import us03, us04

# Load individuals and families from GEDCOM file
individuals = gedcom_parser.individual_parser("gedcom_test.ged")
families = gedcom_parser.family_parser("gedcom_test.ged")

class TestGedcomFile(unittest.TestCase):

    def test_us03(self):
        # Test that children's births occur before the death of parents
        self.assertTrue(us03(individuals, families))

    def test_us04(self):
        # Test listing upcoming birthdays
        us04(individuals)  

if __name__ == '__main__':
    unittest.main()