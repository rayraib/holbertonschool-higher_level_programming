#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for idx, c in enumerate(roman_string):
        tmp = my_dict[c]
        try:
            if tmp < my_dict[roman_string[idx + 1]]:
                tmp *= -1
        except IndexError:
            pass
        result += tmp
    return result
