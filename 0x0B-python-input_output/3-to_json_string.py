#!/usr/bin/python3
"""JSON"""


import json
def to_json_string(my_obj):
    """json to string"""
    json_string = json.dumps(my_obj)
    return json_string
