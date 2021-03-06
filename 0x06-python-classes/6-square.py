#!/usr/bin/python3
class Square():
    '''Represent a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize the data for each instance object'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Getter method - Get __size field value'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method - Sets __size field value'''
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''Getter method - get __position field data'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter method - set __position field data'''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or value[0] < 0 or\
                not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''Calculate area of the instance square'''
        return (self.size * self.size)

    def my_print(self):
        '''prints square with # character'''
        if self.size is 0:
            print()
        else:
            for k in range(self.position[1]):
                print()
            for i in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
