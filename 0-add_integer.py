#!/usr/bin/python3
"""Module for add number"""
def add_integer(a, b=98):
    """Adds two integers.
        Args:
            a: the first integer.
            b: the second integer, default 98.
        Raises:
            TypeError: if a, b are not int, float.
        Returns:
            The sum of the two integers.
    """
    if type(a) not in (int, float):
        raise("a must be an integer")
    if type(b) not in (int, float):
        raise("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
