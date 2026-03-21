#!/usr/bin/python3
"""
The module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""

        rows = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rows)

    def __repr__(self):
        """Return string representation to recreate object"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Print message when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
