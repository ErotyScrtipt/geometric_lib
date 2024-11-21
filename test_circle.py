import unittest
from circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area_positive_radius(self):
        """Тест площади круга с положительным радиусом."""
        radius = 3
        expected = math.pi * radius ** 2
        self.assertAlmostEqual(area(radius), expected, places=5)

    def test_area_zero_radius(self):
        """Тест площади круга с нулевым радиусом."""
        self.assertEqual(area(0), 0)

    def test_area_negative_radius(self):
        """Тест площади круга с отрицательным радиусом."""
        radius = -3
        expected = math.pi * radius ** 2
        self.assertAlmostEqual(area(radius), expected, places=5)

    def test_perimeter_positive_radius(self):
        """Тест периметра (длины окружности) круга с положительным радиусом."""
        radius = 3
        expected = 2 * math.pi * radius
        self.assertAlmostEqual(perimeter(radius), expected, places=5)

    def test_perimeter_zero_radius(self):
        """Тест периметра круга с нулевым радиусом."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative_radius(self):
        """Тест периметра круга с отрицательным радиусом."""
        radius = -3
        expected = 2 * math.pi * radius
        self.assertAlmostEqual(perimeter(radius), expected, places=5)

if __name__ == '__main__':
    unittest.main()