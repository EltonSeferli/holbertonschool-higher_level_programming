#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """
    Rectangle functions and data
    """

    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # ❗ düzəldildi
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Functions
    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return rectangle using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""

        res = []
        for _ in range(self.__height):
            res.append("#" * self.__width)
        return "\n".join(res)

    def __repr__(self):
        """Return string representation"""
        return f"Rectangle({self.__width}, {self.__height})"
