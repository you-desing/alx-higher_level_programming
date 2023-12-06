#!/usr/bin/python3
"""Save file"""


import json
def save_to_json_file(my_obj, filename):
    """funct save"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
