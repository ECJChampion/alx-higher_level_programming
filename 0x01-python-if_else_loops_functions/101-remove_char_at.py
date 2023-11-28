#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return "Index out of range"

    return s[:n] + s[n+1:]

# Example usage:
original_string = "example"
index_to_remove = 3
result = remove_char_at(original_string, index_to_remove)
print(result)  # Output: "exaple"

