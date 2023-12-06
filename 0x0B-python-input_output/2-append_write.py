#!/usr/bin/python3
"""Append file"""


def append_write(filename="", text=""):
    """append function"""
    with open(filename,"a", encoding='utf-8') as file:
        file.write(text)
    return len(text)
