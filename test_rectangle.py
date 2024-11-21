import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero_width(self):
        """Тест площади при ширине 0"""
        self.assertEqual(area(10, 0), 0)

    def test_area_square(self):
        """Тест площади квадрата"""
        self.assertEqual(area(10, 10), 100)

    def test_perimeter_zero_width(self):
        """Тест периметра при ширине 0"""
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_square(self):
        """Тест периметра квадрата"""
        self.assertEqual(perimeter(10, 10), 40)

    def test_area_negative_values(self):
        """Тест площади при отрицательных значениях"""
        self.assertEqual(area(-5, 10), -50)

    def test_perimeter_negative_values(self):
        """Тест периметра при отрицательных значениях"""
        self.assertEqual(perimeter(-5, 10), 10)