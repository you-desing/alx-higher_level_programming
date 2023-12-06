#!/usr/bin/python3
"""load json"""


import json
def load_from_json_file(filename):
    """funct load"""
    with open(filename, "r") as file:
       return json.load(file)
