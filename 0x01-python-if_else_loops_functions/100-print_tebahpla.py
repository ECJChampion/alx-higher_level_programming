#!/usr/bin/python3
# prints the ASCII alphabet, in reverse order

for i in range(25, -1, -1):
    if i % 2 == 0:
        letter = chr(65 + i)
        print("{}".format(letter), end="")
    else:
        letter = chr(65 + i).lower()
        print("{}".format(letter), end="")
