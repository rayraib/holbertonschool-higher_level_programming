#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    ''' return a list of list of ints'''
    main_list = []
    if n <= 0:
        return []
    j = 1
    while j <= n:
        tri_list = []
        for i in range(0, j):
            if i == 0 or i == j - 1:
                tri_list.append(1)
            else:
                tri_list.append(main_list[j - 2][i] + main_list[j - 2][i - 1])
        main_list.append(tri_list)
        j += 1
    return main_list
