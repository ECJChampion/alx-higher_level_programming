#!/usr/bin/python3

# function that prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    if type(matrix) == list:
        for row in matrix:
            separator = ""
            for item in row:
                if separator:
                    print(separator, end="")
                print("{:d}".format(item), end="")
                separator = " "
            print()
