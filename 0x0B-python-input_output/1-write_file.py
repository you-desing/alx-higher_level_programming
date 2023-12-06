#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """function write"""
    with open(filename,"w", encoding='utf-8') as file:
        file.write(text)
    return len(text)
