#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_cnt = len(sys.argv)
    sum = 0
    for i in range(arg_cnt):
        if i == 0:
            continue
        num = int(sys.argv[i])
        sum += num
    print("{}".format(sum))
