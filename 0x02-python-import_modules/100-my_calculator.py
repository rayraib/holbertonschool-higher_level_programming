#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    arg = sys.argv
    arg_cnt = len(sys.argv)
    if arg_cnt != 4:
        print("Usage: {} <a> <operator> <b>".format(arg[0]))
        exit(1)
    if arg[2] == '+':
        print("{} + {} = {}".format(arg[1], arg[3], calculator_1.add(arg[1], arg[3])))
    elif arg[2] == '-':
        print("{} - {} = {}".format(arg[1], arg[3],
                                    calculator_1.sub(arg[1], arg[3])))
    elif arg[2] == '*':
        print("{} * {} = {}".format(arg[1], arg[3],
                                    calculator_1.mul(arg[1], arg[3])))
    elif arg[2] == '/':
        print("{} / {} = {}".format(arg[1], arg[3],
                                    calculator_1.div(arg[1], arg[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
