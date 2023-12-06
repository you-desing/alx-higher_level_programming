#!/usr/bin/python3
"""Class to JSON"""

class Student:
    """ class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            return {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                }
