#!/usr/bin/python3
"""Rectangle file"""


class BaseGeometry:
    """base class"""
    def area(self):
        """area method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """integer validate"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str (self.__width) + "/" + str(self.__height)
class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        return self.__size * self.__size
