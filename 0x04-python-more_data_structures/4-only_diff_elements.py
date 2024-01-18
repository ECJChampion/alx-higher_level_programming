#!/usr/bin/python3

# function that returns a set of all elements present in only one set

def only_diff_elements(set_1, set_2):
    common_list = []

    for item in set_1:
        if item not in set_2:
            common_list.append(item)

    for element in set_2:
        if element not in set_1:
            common_list.append(element)

    return (common_list)
