#!/usr/bin/python3
# function that prints a string in uppercase followed by a new line

def uppercase(str):
    letter = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            letter += chr(ord(i) - 32)
        else:
            letter += i
    print("{}".format(letter))
