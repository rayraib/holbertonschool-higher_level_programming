#!/usr/bin/python3
'''
    a function that finds a peak in a list of unsorted integers
'''


def find_peak(list_of_integers):
    '''
        find the peak
    '''
    length = len(list_of_integers)
    for i in range(1, length - 1):
        if (list_of_integers[i - 1] < list_of_integers[i]
                > list_of_integers[i + 1]):
            return(list_of_integers[i])
    if list_of_integers[0] > list_of_integers[1]:
        return(list_of_integers[0])
    elif list_of_integers[length - 1] > list_of_integers[length - 2]:
        return(list_of_integers[length - 1])
    else:
        return list_of_integers[0]
