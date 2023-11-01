#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            uppercase_char = chr(ord(str[i]) - 32)
            print("{}".format(uppercase_char), end='')
        else:
            print("{}".format(str[i]), end='')
