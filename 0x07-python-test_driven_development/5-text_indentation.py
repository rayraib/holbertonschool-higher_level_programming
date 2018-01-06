#!/usr/bin/python3
def text_indentation(text):
    '''
        Prints text with 2 new lines after the character ``.``, ``?`` and ``:``
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        flag = 0
        for idx, c in enumerate(text):
            if c is '\n':
                continue
            if c is '.' or c is '?' or c is ':':
                flag = 1
                print(c)
                print()
            else:
                if c is " ":
                    if flag == 1:
                        continue
                    i = 1
                    while (text[idx + i] == " "):
                        i += 1
                    x = text[idx + i]
                    if x == '.' or x == '?' or x == ':':
                        continue
                    else:
                        print(c, end="")
                        flag = 0
                else:
                    print(c, end="")
                    flag = 0
