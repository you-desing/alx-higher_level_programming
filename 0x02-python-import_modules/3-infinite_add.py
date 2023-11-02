#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    length = len(sys.argv)
    s = 0
    for i in range(1, length):
        s += int(sys.argv[i])
    print("{}".format(s))
