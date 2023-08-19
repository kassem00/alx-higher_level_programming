#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    c_mat = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] * matrix[i][j])
        c_mat.append(row)

    return c_mat
