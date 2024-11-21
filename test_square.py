import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_positive(self):
        """Тест площади квадрата с положительной стороной."""
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        """Тест площади квадрата с нулевой стороной."""
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        """Тест площади квадрата с отрицательной стороной."""
        self.assertEqual(area(-4), 16)

    def test_perimeter_positive(self):
        """Тест периметра квадрата с положительной стороной."""
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        """Тест периметра квадрата с нулевой стороной."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        """Тест периметра квадрата с отрицательной стороной."""
        self.assertEqual(perimeter(-4), -16)

if __name__ == '__main__':
    unittest.main()