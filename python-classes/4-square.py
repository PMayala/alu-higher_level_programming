#!/usr/bin/python3
"""
Module 4-square
Defines a class 'Square'

"""


class Square:
    """
    Defines a Square instance.

    Args:
            size (int): size of the square

    """

    def __init__(self, size=0):
        """The Square __init__ method initializes the attribute 'size'.

        Args:
            size (int): size of the square

        """
        self.size = size

    @property
    def size(self):
        """Square getter method.

        Returns:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Square setter method.

        Args:
            value (int): sets size to value

        Raises:
            TypeError: If value is not integer
            ValueError: If value is less than 0

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Square area method.

        Returns:
            Area of square
        """
        return (self.__size ** 2)
