#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and number ==0:
    num = number * (-1)  % 10
    print(f"Last digit of {number} is {num * (-1)}", end=' ')
    if number % 10 > 5:
        print("and is greater than 5", end=' ')
    if number % 10 == 0:
        print("and is 0", end=' ')
    if number % 10 < 6 and number % 10 != 0:
        print("and is less than 6 and not 0")
elif number > 0 and number == 0:
    print(f"Last digit of {number} is {number % 10}", end=' ')
    if number % 10 > 5:
        print("and is greater than 5")
    if number % 10 == 0:
        print("and is 0")
    if number % 10 < 6 and number % 10 != 0:
        print("and is less than 6 and not 0")

