#!/usr/bin/python3

def uppercase(str):
    result = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            uppercase_char = chr(ord(str[i]) - 32)
            result += uppercase_char
        else:
            result += str[i]
    print("{}\n".format(result), end='')
