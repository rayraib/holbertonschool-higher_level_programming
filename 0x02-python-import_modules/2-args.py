#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_cnt = len(sys.argv)
    if arg_cnt == 1:
        print("0 arguments.")
    elif arg_cnt == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arg_cnt - 1))
        for i in range(arg_cnt):
            if i == 0:
                continue
            print("{}: {}".format(i, sys.argv[i]))
