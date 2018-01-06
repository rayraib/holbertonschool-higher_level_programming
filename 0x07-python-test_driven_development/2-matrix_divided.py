#!/usr/bin/python3 def matrix_divided(matrix, div):
'''
    Divide all elements of a matrix by an int ``div``
'''
def matrix_divided(matrix, div):
    new_list = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise TypeError("division by zero")
    for idx, row in enumerate(matrix):
        new_row = []
        if idx != 0:
            if len(row) != len(matrix[idx - 1]):
                raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if isinstance(element, float) or isinstance(element, int):
                new_row.append(float(round(element / div, 2)))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_list.append(new_row)
    return new_list

