#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except IndexError as e:
        sys.stderr.write("Exception: %s" % e)
        sys.stderr.write('\n')
    except ZeroDivisionError as e:
        sys.stderr.write("Exception: %s" % e)
        sys.stderr.write('\n')
