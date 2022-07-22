#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class representation"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
                size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the current square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the equality(==) to a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the not equal(!=) comparison to a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a square"""
        return self.area() >= other.area()
