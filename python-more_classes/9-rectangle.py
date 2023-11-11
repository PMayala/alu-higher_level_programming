#!/usr/bin/python3
"""Module 9-rectangle"""


class Rectangle:
    """Creates a Rectangle instance

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization method"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width getter method that returns the width (private attribute)"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Height getter method that returns the height (private attribute)"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area method that returns area value"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter method that returns perimeter value"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height*2)

    def __str__(self):
        """string representation method that prints a rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        sw, sh = self.width, self.height
        return "\n".join([f"{self.print_symbol}" * sw for i in range(sh)])

    def __repr__(self):
        """string representation that returns new instance of class """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """The rectangle's delete method. Deletes instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle of the two based on the area"""
        if isinstance(rect_1, Rectangle) == 0:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) == 0:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns new rectangle instance with width == height == size """
        return cls(size, size)
