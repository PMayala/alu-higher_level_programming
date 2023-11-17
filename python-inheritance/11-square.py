#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Method for initializing a square"""
        super().__init__(size, size)

    def __str__(self):
        """Method that returns a string"""
        return "[Square] {}/{}".format(self.__width, self.__height)
