#!/usr/bin/python3
""" kind of class """


def inherits_from(obj, a_class):
    """class is same"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
