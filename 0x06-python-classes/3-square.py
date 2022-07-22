#!/usr/bin/python3
"""Square class"""

class Square:
	"""The size of the square initialization method"""
	def __init__(self, size=0):
		"""Square class initialization

		Args:
			size (int): The size of the new square set to 0
		"""
		if not isinstance(size, int):
			raise TypeError("size must be an intger")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size
	
	def area(self):
		"""Return the current area of the square"""
		return (self.__size * self.__size)
