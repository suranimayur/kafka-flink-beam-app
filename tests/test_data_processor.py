import unittest
from app.data_processor import calculate_age

class TestDataProcessor(unittest.TestCase):
    def test_calculate_age(self):
        self.assertEqual(calculate_age('2000-01-01'), 23)  # Adjust based on current year
        self.assertEqual(calculate_age('1990-12-31'), 32)  # Adjust based on current year

if __name__ == '__main__':
    unittest.main()