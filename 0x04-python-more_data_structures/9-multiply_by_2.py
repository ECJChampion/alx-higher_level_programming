#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multiplied_dict = {}

    # Iterate through the items in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply each value by 2 and store it in the new dictionary
        multiplied_dict[key] = value * 2

    # Return the new dictionary with multiplied values
    return multiplied_dict
