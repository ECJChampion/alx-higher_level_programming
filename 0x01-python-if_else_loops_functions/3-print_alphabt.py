#!/usr/bin/python3
# program that prints the ASCII alphabet, in lowercase
# Print all the letters except q and e

for letter in range(97, 123):
    alpha = chr(letter)
    if alpha != 'q' and alpha != 'e':
        print("{}".format(alpha), end="")
