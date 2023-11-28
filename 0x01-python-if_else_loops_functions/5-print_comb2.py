#!/usr/bin/python3
# program that prints numbers from 0 to 99

for number in range(0, 100):
    if number < 99:
        print("{:02d}".format(number), end=", ")
    else:
        print("{:02d}".format(number))
