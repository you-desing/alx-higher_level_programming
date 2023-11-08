#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = my_list.copy()
    for elm in range(len(my_list)):
        if res[elm] == search:
            res[elm] = replace
    return res
