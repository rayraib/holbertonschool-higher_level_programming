#!/usr/bin/python3
class Square():
    '''Represent a square'''
    def __init__(self, size=0):
        '''Initialize data'''
        self.size = size

    @property
    def size(self):
        '''Getter method - Get the __size field value'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method - Set the __size field value'''
        if (isinstance(value, int) is False):
            print("size must be an integer")
            raise TypeError
        elif value < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        '''Calculate area from the __size field'''
        area = (self.__size * self.__size)
        return area

    def my_print(self):
        '''Print the square with the character # '''
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.size):
                    print('#', end="")
                print()
