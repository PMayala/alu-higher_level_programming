#!/usr/bin/python3
"""Module 11-square"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Area method (not implemented)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle inherited from BaseGeometry"""
    def __init__(self, width, height):
        """Initializer with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square inherited from Rectangle"""
    def __init__(self, size):
        """Initializer with size"""
        super().__init__(size, size)
        self.integer_validator("size", size)

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
