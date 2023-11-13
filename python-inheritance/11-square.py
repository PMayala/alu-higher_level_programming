#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

if __name__ == "__main__":
    # Testing
    print(dir(Square))
    s = Square(4)
    print(s.area())
    s = Square(1411)
    print(s.area())
    s = Square(5)
    print(s.area())
    s = Square(781)
    print(s)
    s = Square(4)
    print(s)
    s = Square(5)
    print(s)
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
    try:
        s = Square(5)
        print(s.size)
        print(s.width)
        print(s.height)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
