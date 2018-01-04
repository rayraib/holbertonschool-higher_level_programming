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
            print("size must be an integer")
            raise TypeError
        elif value < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        '''Getter method - get __position field data'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter method - set __position field data'''
        if (isinstance(value, tuple) is False or len(value) != 2):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        for element in value:
            if (isinstance(element, int) is False) or element < 0:
                print("position must be a tuple of 2 positive integers")
                raise TypeError
            else:
                self.__position = value

    def area(self):
        '''Calculate area of the instance square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''prints square with # character'''
        if self.__size is 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print('#', end="")
                print()
