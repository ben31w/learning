# To use unit tests, import unittest and the function you want to test.
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    # Any method that starts with 'test_' will run automatically when
    #  test_name_function is run, since the program contains a class that
    #  extends TestCase. 'test_' methods can have long, descriptive names, since
    #  you'll never have to retype them.
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')

        # assertEqual() will verify if the first argument equals the second
        #  argument. Other unittest assert methods include:
        #  -assertNotEqual(a, b)    - verify that a != b
        #  -assertTrue(x)           - verify that x is True
        #  -assertFalse(x)          - verify that x is False
        #  -assertIn(item list)     - verify that an item is in a list
        #  -assertNotIn(item, list) - verify that an item is not in a list
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# __name__ is a special variable that gets set when a program is executed.
#  If this file is being run as the main program (which it is), __name__ is set
#  to '__main__'
if __name__ == '__main__':
    unittest.main()
# This method will run through each test you created. A passing test prints a
#  dot (.), a test that results in an error prints an E, and a failing test
#  prints an F.