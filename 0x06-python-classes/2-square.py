#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("sum must be greater than or equal to 0")
        self.__size = size
