#!/usr/bin/python3
"""BaseGeometry class definition"""


class BaseGeometry:
    """base class"""
    def area(self):
        """method area"""
        raise Exception("area() is not implemented")

    # Validates that the given value is an integer greater than 0
    def integer_validator(self, name, value):
        """ Validates that the given value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Rectangle class definition, inherits from BaseGeometry
class Rectangle(BaseGeometry):
    """ reactangle class"""
    def __init__(self, width, height):
        """Validate width and height using the integer_validator from the base class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        # Private attributes for width and height
        self.__width = width
        self.__height = height

    # Method to calculate the area of the rectangle
    def area(self):
        """area rectangle"""
        return self.__width * self.__height

    # Method to provide a string representation of the rectangle
    def __str__(self):
        """ str method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

# Square class definition, inherits from Rectangle
class Square(Rectangle):
    """Constructor with size parameter"""
    def __init__(self, size):
        """Call the constructor of the base class (Rectangle)"""
        super().__init__(size, size)

        # Validate size using the integer_validator from the base class
        super().integer_validator("size", size)

        # Private attribute for size
        self.__size = size

    # Method to calculate the area of the square
    def area(self):
        """area square"""
        return self.__size * self.__size

    # Method to provide a string representation of the square
    def __str__(self):
        """str method"""
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)

