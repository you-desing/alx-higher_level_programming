#!/usr/bin/python3
"""rectangle file"""


class BaseGeometry:
    """base class"""
    def area(self):
        """area method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """integer valid method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        """init method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """area rectangle"""
        return self.__width * self.__height
    def __str__(self):
        """str method"""
        return "[Rectangle]" + str (self._width) + "/" + str(self._height)
