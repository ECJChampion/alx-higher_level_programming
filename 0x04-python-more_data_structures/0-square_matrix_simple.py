#!/usr/bin/python3

# function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        squared_row = []

        for item in row:
            squared = item * item
            squared_row.append(squared)

        result.append(squared_row)

    return (result)
