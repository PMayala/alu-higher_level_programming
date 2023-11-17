#!/usr/bin/python3
"""
Module 11-square
Contains the Square class
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A representation of a square
    """
    def __init__(self, size):
        """
        Initializes a new instance of Square

        Parameters:
        - size (int): the size of the square
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the square description

        Returns:
        str: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
