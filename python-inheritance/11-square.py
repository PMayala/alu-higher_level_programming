#!/usr/bin/python3
"""Defines class Square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with width"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return description of the square"""
        return str("[Square] {}/{}".format(self.__size, self.__size))

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.integer_validator("size", value)
        self.__size = value
        self.width = value
        self.height = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size  # Corrected the area calculation

if __name__ == "__main__":
    s = Square(5)
    print(s)
    print(s.area())
    print(s.width)
    print(s.height)
    print(s.size)

    # Additional cases
    try:
        s = Square()
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        s = Square([12, 52])
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        s = Square(-35)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        s = Square(0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
