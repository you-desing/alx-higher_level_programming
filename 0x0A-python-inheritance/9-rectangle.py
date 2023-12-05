#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        return self.__width * self.__height
    def __str__(self):
        return "[Rectangle]" + str (self._width) + "/" + str(self._height)
