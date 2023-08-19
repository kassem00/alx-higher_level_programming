#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    c_mat = matrix

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            c_mat[i][j] = c_mat[i][j] * c_mat[i][j]
    return c_mat
