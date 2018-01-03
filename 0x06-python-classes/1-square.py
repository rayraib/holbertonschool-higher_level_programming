#!/usr/bin/python3
class Square():
    """Represent a square with size"""
    def __init__(self, size):
        """Initializes the data"""
        self.size = size 

    @property
    def size(self):
        """Return the size value"""
        return self._size
    @size.setter
    def size(self, size):
        """Set the private __size attribute to size"""
        self.__size = size

     
