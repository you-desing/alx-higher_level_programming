#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i is not x:
            print("{}".format(my_list[i]), end = '')
            i = i + 1
    except IndexError:
        None
    print()
    return i
