#!/usr/bin/python3
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
arg_list = []
for i, arg in enumerate(sys.argv):
    if i != 0:
        arg_list.append(arg)
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
    for i, arg in enumerate(sys.argv):
        if i != 0:
            my_list.append(arg)
    save_to_json_file(my_list, filename)
else:
    save_to_json_file(arg_list, filename)
