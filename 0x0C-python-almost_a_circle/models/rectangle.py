#!/usr/bin/python3
"""task 2 3 4 5 et 6"""

class Rectangle(base):
    """Rectangle base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        @property
        def width(self):
            return self.__width
        @width.setter
        def width(self, value):
            
            if not isinstance(value, int):
                raise TypeError(f"{name of the attribute} must be an integer",value)
            if value <= 0 :
                raise ValueError(f"{name of the attribute} must be > 0",value)
            self.__width = value
        
        @property
        def height(self):
            return self.__height
        @height.setter
        def height(self, value):
            self.__height = value
            if not isinstance(value, int):
                raise TypeError(f"{name of the attribute} must be an integer",value)
            if value <= 0 :
                raise ValueError(f"{name of the attribute} must be > 0",value)
            self.__height = value
        @property
        def x(self):
            return self.__x
        @x.setter
        def x(self, value):
            
            if not isinstance(value, int):
                raise TypeError(f"{name of the attribute} must be an integer",value)
            if value <= 0 :
                raise ValueError(f"{name of the attribute} must be > 0",value)
            self.__x = value

            
            
        @property
        def y(self):
            return self.__y
        @y.setter
        def y(self, value):
            
            if not isinstance(value, int):
                raise TypeError(f"{name of the attribute} must be an integer",value)
            if value <= 0 :
                raise ValueError(f"{name of the attribute} must be > 0",value)
            self.__y = value
            
        def area(self):
            return self.__height * self.__width
        
        def display(self):
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                print()

        def __str__(self):
            return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
