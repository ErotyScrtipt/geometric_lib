import math


def area(r):
    '''
        Считает площадь круга по заданному радиусу
        :param r: радиус круга
        :type r: float
        :return: площадь круга
        :rtype: float
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Считает периметр круга по заданному радиусу
        :param r: радиус круга
        :type r: float
        :return: периметр круга
        :rtype: float 
    '''
    return 2 * math.pi * r

