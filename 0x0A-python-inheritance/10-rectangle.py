#!/usr/bin/python3
"""BaseGeometry class definition"""


class BaseGeometry:
    """base class"""
    def area(self):
        """method area"""
        raise Exception("area() is not implement")
    def integer_validator(self, name, value):
        """ Validates that the given value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """ reactangle class"""
    def __init__(self, width, height):
        """Validate width and height using the integer_validator from the base class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """area rectangle"""
        return self.__width * self.__height
    def __str__(self):
        """ str method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
class Square(Rectangle):
    """Constructor with size parameter"""
    def __init__(self, size):
        """Call the constructor of the base class (Rectangle)"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """area square"""
        return self.__size * self.__size
