import city_functions
import unittest


class TestCitiesCountriesAreFormatted(unittest.TestCase):
    def test_city_country(self):
        formatted_city_name = city_functions.city_country_formatted('santiago', 'chile')
        self.assertEqual(formatted_city_name, 'Santiago, Chile')


class TestCitiesCountriesPopulationAreFormatted(unittest.TestCase):
    def test_city_country(self):
        formatted_city_name = city_functions.city_country_formatted('santiago', 'chile', '5 000 000')
        self.assertEqual(formatted_city_name, 'Santiago, Chile - 5 000 000 Population')


if __name__ == '__main__':
    unittest.main()
