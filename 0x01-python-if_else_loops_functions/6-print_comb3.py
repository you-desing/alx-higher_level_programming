#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i == 0 and j == 1:
            print("{}".format(i), end='')
        else:
            print(", {}".format(i), end='')
        print("{}".format(j), end='')
