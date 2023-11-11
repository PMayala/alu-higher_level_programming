#!/usr/bin/python3
"""
Module 8-rectangle
Defines a class Rectangle

"""


class Rectangle:
    """Defines a Rectangle instance"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The Rectangle __init__ method

        Args:
            width (int): rectangle's width
            height (int): rectangle's height

        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """The Rectangle's width getter method

        Returns:
            rectangle's width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """The Rectangle's width setter method

        Args:
            value (int): rectangle's width

        Raises:
            TypeError: if value is not a number
            ValueError: if value is a negative

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """The Rectangle's height getter method

        Returns:
            rectangle's height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """The Rectangle's height setter method

        Args:
            value (int): rectangle's height

        Raises:
            TypeError: if value is not a number
            ValueError: if value is a negative

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """The rectangle's area method

        Returns:
            is_area: area
        """
        is_area = self.__width * self.__height
        return is_area

    def perimeter(self):
        """The rectangle's perimeter method

        Returns:
            is_perimeter: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            is_perimeter = (self.__width * 2) + (self.__height*2)
            return is_perimeter

    def __str__(self):
        """The rectangle's string representation method for users"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            sw = self.__width
            sh = self.__height
            return "\n".join([f"{self.print_symbol}" * sw for i in range(sh)])

    def __repr__(self):
        """The rectangle's string representation method"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """The rectangle's delete method. Deletes instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that compares two rectangles

        Returns:
            the bigger triangle based on the area

        Raises:
            TypeError: if either rect_1 or rect_2 is not instance of Rectangle
        """
        if isinstance(rect_1, Rectangle) == 0:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) == 0:
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            else:
                if rect_1.area() > rect_2.area():
                    return rect_1
                else:
                    return rect_2
