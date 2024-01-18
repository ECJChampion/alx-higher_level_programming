#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a copy of the dictionary to avoid modifying the original while iterating
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]

    # Delete keys with the specified value
    for key in keys_to_delete:
        del a_dictionary[key]
