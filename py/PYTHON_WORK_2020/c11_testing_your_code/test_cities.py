import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    
    def test_city_country(self):
        """Do cases like 'Santiago, Chile' work?"""
        test_1 = city_country('santiago', 'chile')
        self.assertEqual(test_1, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cases like 'Santiago, Chile - population 5000000' work?"""
        test_2 = city_country('santiago', 'chile', 5_000_000)
        self.assertEqual(test_2, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()