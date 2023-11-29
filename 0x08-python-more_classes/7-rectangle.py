#!/usr/bin/python3
"""Rectangle module"""

class Rectangle:
    """Class defines a rectangle."""
    number_of_instances=0
    print_symbol="#"
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with given width and height."""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances+=1
    
    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
    def area(self):
        """Area of the rectangle."""
        Area = self.width * self.height
        return Area
    def perimeter(self):
        """Perimeter of the rectangle."""
        par = 2 * (self.width + self.height)
        return par
    def __str__(self):
        """rectangle #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.height):
                rectangle_str += str(self.print_symbol) * self.width + "\n"
            return rectangle_str[:-1]
            
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances-=1
