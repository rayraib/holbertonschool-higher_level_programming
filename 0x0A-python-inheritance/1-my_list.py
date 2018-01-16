#!/usr/bin/python3
''' subclass of list'''


class MyList(list):
    '''subclass of list'''
    def print_sorted(self):
        '''print the list in ascending order sorted'''
        print(sorted(self))
