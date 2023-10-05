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
    for i in range(m):
        # Find the first non-zero element in the row.
        pivot = None
        for j in range(n):
            if ref.get_value(i + 1, j + 1) != 0:
                pivot = j
                break

        # If no non-zero element is found, skip the row.
        if pivot is None:
            ref = swap_rows(ref, i, m - 1)
            m -= 1
            i -= 1
            continue

        # Swap the rows if necessary to bring the pivot to the diagonal.
        if pivot != i:
            ref = swap_rows(ref, i, pivot)

        # Scale the row to make the pivot element 1.
        pivot_value = ref.get_value(pivot + 1, pivot + 1)
        if pivot_value != 1:
            ref = scale_row(ref, pivot, 1 / pivot_value)

        # Eliminate the pivot element from the rows below it.
        for j in range(i + 1, m):
            factor = ref.get_value(j + 1, pivot + 1)
            if factor != 0:
                ref = add_multiple_times_row(ref, j, i, -factor)

    # Return the row echelon form.
    return ref

