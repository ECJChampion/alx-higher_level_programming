#!/usr/bin/python3

# function that returns a set of common elements in two sets.

def common_elements(set_1, set_2):
    common_element = []

    for item in set_1:
        for element in set_2:
            if element == item:
                common_element.append(element)

    return (common_element)
