#!/usr/bin/python3
'''Check whether the file is being executed directly or imported
   as module in another file and only if executed directly continue
   with the rest of the code'''
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    '''Check if there are exactly 4 arguments: filename, number, operand
    and second number'''
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    '''Check if the operand is one of the four options and if yes,
    call the respective imported function and print the returned
    result'''
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        '''If the input operand is not one of the four valid options
        print an error mesasge'''
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
