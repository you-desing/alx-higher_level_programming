#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """function read"""
    with open(filename,"r") as file:
        file_cont = file.read()
    print(file_cont)
