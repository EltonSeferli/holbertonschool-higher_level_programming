#!/usr/bin/python3
def matrix_divided(matrix,div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if(
        not isinstance(matrix, list) or
        len(matrix) == 0 or 
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size") 
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    new_matrix=[]
    for row in matrix:
        new_row=[]
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix
