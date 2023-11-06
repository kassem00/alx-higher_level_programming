#!/usr/bin/python3
'''function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''function that divides all elements of a matrix.'''
    if (not type(matrix) == list or matrix == [] or
            not all(type(row) == list for row in matrix) or
            not all((type(ele) == int or type(ele) == float)
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not (type(div) == int or type(div) == float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
