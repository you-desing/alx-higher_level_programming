#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = set()
    for elm in my_list:
        res.add(elm)
    return sum(res)
