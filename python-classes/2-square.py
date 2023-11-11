#!/usr/bin/python3
"""
Module 2-square
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

        Attribute:
            __size (int): size of the square - private attribute

        Raises:
            TypeError: If size is not integer
            ValueError: If size is less than 0

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
