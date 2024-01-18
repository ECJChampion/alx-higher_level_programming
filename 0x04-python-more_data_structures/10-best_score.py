#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = None
    max_value = float('-inf')  # Start with negative infinity as the initial max_value

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key