#!/usr/bin/python3

# function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):

    sorted_items = sorted(a_dictionary.items())

    for key, value in sorted_items:
        print("{}: {}".format(key, value))
