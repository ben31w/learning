import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Instantiate an employee to use in the tests."""
        self.employee = Employee('John', 'Smith', 63_000)

    def test_change_first_name(self):
        """Tests that changing only the first name w/ change_name() works."""
        self.employee.change_name('Alex')
        self.assertEqual(self.employee.first_name, 'Alex')

    def test_change_first_and_last_name(self):
        """Tests that changing both names w/ change_name works."""
        self.employee.change_name('Alex', 'Young')
        self.assertEqual(self.employee.first_name, 'Alex')
        self.assertEqual(self.employee.last_name, 'Young')

    def test_change_last_name(self):
        """Test that change_last_name() works."""
        self.employee.change_last_name('Wright')
        self.assertEqual(self.employee.last_name, 'Wright')

    def test_give_default_raise(self):
        """Tests that give_raise() method works w/o parameters."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 68_000)

    def test_give_custom_raise(self):
        """Tests that give_raise() works w/ a custom amount."""
        self.employee.give_raise(10_000)
        self.assertEqual(self.employee.annual_salary, 73_000)

if __name__ == '__main__':
    unittest.main()