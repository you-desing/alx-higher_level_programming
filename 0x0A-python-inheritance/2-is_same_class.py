#!/usr/bin/python3
""" Exact same object"""


def is_same_class(obj, a_class):
    """class is same"""
    if type(obj) is a_class:
        return True
    else:
        return False
