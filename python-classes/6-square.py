#!/usr/bin/python3
"""
Module 6-square
Defines a class 'Square'

"""


class Square:
    """
    Defines a Square instance.

    Args:
            size (int): size of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """The Square __init__ method initializes the attribute 'size'.

        Args:
            size (int): size of the square
            position (tuple):  coordinates of the square

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Square getter method for size.

        Returns:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Square setter method for size.

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

    @property
    def position(self):
        """Square getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Square setter method for position

        Args:
            value (int): sets position to value

        Raises:
            TypeError: If tuple is not of 2 positive ints

        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Square area method.

        Returns:
            Area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
