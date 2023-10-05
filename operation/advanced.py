import MatrixProgram.matrix as matrix
from copy import deepcopy


def minor(mat: matrix.Matrix, row: int, col: int) -> matrix.Matrix:
    '''
    Calculates the minor of a matrix.
    args:
        mat: The matrix to calculate the minor of.
        row: The row of the element.
        col: The column of the element.
    
    returns:
        The minor of the matrix.
    '''

    # Get the size of the matrix.
    m, n = mat.get_size()

    # Check if the matrix is square.
    assert m == n, 'The matrix is not square.'
    
    # Check if the row and column are valid.
    assert row >= 0 and row < m and col >= 0 and col < n, 'The row or column is invalid.'
    
    # Calculate the minor.
    minor = matrix.Matrix([[0 for _ in range(n - 1)] for _ in range(m - 1)])
    for i in range(m):
        for j in range(n):
            if i != row and j != col:
                minor.set_value(i - (i > row) + 1, j - (j > col) + 1, mat.get_value(i + 1, j + 1))
    
    return minor


def cofactor(mat: matrix.Matrix) -> matrix.Matrix:
    '''
    Calculates the cofactor of a matrix.

    args:
        mat: The matrix to calculate the cofactor of.

    returns:
        The cofactor of the matrix.
    '''
    m, n = mat.get_size()

    # Check if the matrix is square.
    assert m == n, 'The matrix is not square.'

    # Calculate the cofactor.
    cofactor = matrix.Matrix([[0 for _ in range(n)] for _ in range(m)])
    for i in range(m):
        for j in range(n):
            cofactor.set_value(i + 1, j + 1, (-1) ** (i + j) * minor(mat, i, j).determinant())
    
    return cofactor


def adjoint(mat: matrix.Matrix) -> matrix.Matrix:
    '''
    Calculates the adjoint of a matrix.

    args:
        mat: The matrix to calculate the adjoint of.

    returns:
        The adjoint of the matrix.
    '''
    m, n = mat.get_size()

    # Check if the matrix is square.
    assert m == n, 'The matrix is not square.'

    # Calculate the adjoint.
    adjoint = cofactor(mat)
    adjoint = adjoint.transpose()

    return adjoint


def inverse(mat: matrix.Matrix) -> matrix.Matrix:
    '''
    Calculates the inverse of a matrix.

    Using the formula:
    A^-1 = 1 / det(A) * adj(A)

    args:
        mat: The matrix to calculate the inverse of.
    
    returns:
        The inverse of the matrix.
    '''
    # Check if the matrix is square.
    m, n = mat.get_size()
    assert m == n, 'The matrix is not square.'
    
    # Check if the matrix is invertible.
    assert mat.determinant() != 0, 'The matrix is not invertible.'
    
    # Calculate the inverse.
    inverse = adjoint(mat)

    for i in range(m):
        for j in range(n):
            inverse.set_value(i + 1, j + 1, inverse.get_value(i + 1, j + 1) / mat.determinant())

    return inverse
    

def swap_rows(mat: matrix.Matrix, row1: int, row2: int) -> matrix.Matrix:
    '''
    Swaps two rows of a matrix.

    args:
        mat: The matrix to swap the rows of.
        row1: The first row to swap.
        row2: The second row to swap.

    returns:
        The matrix with the rows swapped.
    '''
    m, n = mat.get_size()

    # Check if the rows are valid.
    assert row1 >= 0 and row1 < m and row2 >= 0 and row2 < m, 'The rows are invalid.'

    # Swap the rows.
    new_mat = deepcopy(mat)
    for i in range(n):
        new_mat.set_value(row1 + 1, i + 1, mat.get_value(row2 + 1, i + 1))
        new_mat.set_value(row2 + 1, i + 1, mat.get_value(row1 + 1, i + 1))

    return new_mat


def scale_row(mat: matrix.Matrix, row: int, factor: float) -> matrix.Matrix:
    '''
    Scales a row of a matrix by a factor.

    args:
        mat: The matrix to scale the row of.
        row: The row to scale.
        factor: The factor to scale the row by.

    returns:
        The matrix with the row scaled.
    '''
    m, n = mat.get_size()

    # Check if the row is valid.
    assert row >= 0 and row < m, 'The row is invalid.'

    # Scale the row.
    new_mat = deepcopy(mat)
    for i in range(n):
        new_mat.set_value(row + 1, i + 1, mat.get_value(row + 1, i + 1) * factor)

    return new_mat


def add_multiple_times_row(mat: matrix.Matrix, row1: int, row2: int, factor: float) -> matrix.Matrix:
    '''
    Adds a multiple of a row to another row of a matrix.

    args:
        mat: The matrix to add the multiple of a row to another row of.
        row1: The row to add the multiple of a row to.
        row2: The row to add the multiple of a row.
        factor: The factor to multiply the row by.

    returns:
        The matrix with the multiple of a row added to another row.
    '''
    m, n = mat.get_size()

    # Check if the rows are valid.
    assert row1 >= 0 and row1 < m and row2 >= 0 and row2 < m, 'The rows are invalid.'

    # Add the multiple of a row to another row.
    new_mat = deepcopy(mat)
    for i in range(n):
        new_mat.set_value(row1 + 1, i + 1, mat.get_value(row1 + 1, i + 1) + mat.get_value(row2 + 1, i + 1) * factor)

    return new_mat


def row_echelon(mat: matrix.Matrix) -> matrix.Matrix:
    '''
    Calculates the row echelon form of a matrix.

    args:
        mat: The matrix to calculate the row echelon form of.

    returns:
        The row echelon form of the matrix.
    '''
    m, n = mat.get_size()

    # Create a copy of the matrix.
    ref = deepcopy(mat)

    # Iterate through the rows.
    last_nonzero_row = m
    for i in range(min(m, n)):
        if last_nonzero_row == i:
            break

        # Find the first row with a nonzero entry in the current column.
        pivot_row = next((r for r in range(i, m) if ref.get_value(r + 1, i + 1) != 0), None)

        # If no nonzero entry is found, move to the next column.
        if pivot_row is None:
            last_nonzero_row -= 1
            ref = swap_rows(ref, i, last_nonzero_row)
            continue

        # Swap the current row with the pivot row.
        if pivot_row != i:
            ref = swap_rows(ref, i, pivot_row)

        # Add multiples of the current row to lower rows to eliminate entries in the current column.
        pivot_value = ref.get_value(i + 1, i + 1)
        for r in range(i + 1, m):
            factor = ref.get_value(r + 1, i + 1)
            if factor != 0:
                ref = add_multiple_times_row(ref, r, i, -factor / pivot_value)

    # Return the row echelon form.
    return ref


def reduced_row_echelon(mat: matrix.Matrix) -> matrix.Matrix:
    '''
    Calculates the reduced row echelon form of a matrix.

    args:
        mat: The matrix to calculate the reduced row echelon form of.

    returns:
        The reduced row echelon form of the matrix.
    '''
    m, n = mat.get_size()

    # Create a copy of the matrix.
    rref = deepcopy(mat)

    rref = row_echelon(rref)

    # Scale the pivot rows to have a leading coefficient of 1.
    for i in range(min(m, n)):
        pivot_col = next((c for c in range(i, n) if rref.get_value(i + 1, c + 1) != 0), None)
        if pivot_col is not None:
            pivot_value = rref.get_value(i + 1, pivot_col + 1)
            rref = scale_row(rref, i, 1 / pivot_value)

    # Convert the matrix to reduced row echelon form.
    for i in range(min(m, n) - 1, -1, -1):
        pivot_col = next((c for c in range(i, n) if rref.get_value(i + 1, c + 1) != 0), None)
        if pivot_col is not None:
            for row in range(i):
                rref = add_multiple_times_row(rref, row, i, -rref.get_value(row + 1, pivot_col + 1))

    # Return the reduced row echelon form.
    return rref


def solve(mat: matrix.Matrix, b: matrix.Matrix) -> matrix.Matrix:
    '''
    Solves a system of linear equations.

    args:
        mat: The matrix of coefficients.
        b: The matrix of constants.

    returns:
        The solution of the system of linear equations.
    '''
    m, n = mat.get_size()

    # Check if the matrix is square.
    assert m == n, 'The matrix is not square.'

    # Check if the matrix is invertible.
    assert mat.determinant() != 0, 'The matrix is not invertible.'

    # Check if the matrix and the vector have the same number of rows.
    assert m == b.get_size()[0], 'The matrix and the vector do not have the same number of rows.'
    assert b.get_size()[1] == 1, 'The vector is not a column vector.'

    # Solve the system of linear equations.
    solution = inverse(mat).matrix_multiply(b)

    return solution
