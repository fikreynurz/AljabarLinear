import MatrixProgram.matrix as matrix

def printMatrix(matrix: matrix.Matrix) -> None:
    '''
    Prints the matrix in a readable format.
    args:
        matrix: The matrix to be printed.
    
    returns:
        None
    '''

    format_number = lambda x: round(x, 2) if x % 1 else int(x)
    
    max_digits = [max(len(str(format_number(element))) for element in col) for col in zip(*matrix.values)]
    
    for row in matrix.values:
        print('|', end=' ')
        for i, element in enumerate(row):
            print(str(format_number(element)).rjust(max_digits[i]), end=' ')
        print('|')


def printMenu():
    '''
    Prints the main menu.
    args:
        None
    
    returns:
        None
    '''
    print('1. Check avaible matrices')
    print('2. Create a matrix')
    print('3. Delete a matrix')
    print('4. Basic operations on matrices')
    print('5. Advanced operations on matrices')
    print('6. exit')


def printBasicOperationsMenu():
    '''
    Prints the basic operations menu.
    args:
        None
    
    returns:
        None
    '''
    print('1. Add two matrices')
    print('2. Substract two matrices')
    print('3. Multiply two matrices')
    print('4. Multiply a matrix with a scalar')
    print('5. Go back to the main menu')


def printAdvancedOperationsMenu():
    '''
    Prints the advanced operations menu.
    args:
        None
    
    returns:
        None
    '''
    print('1. Transpose a matrix')
    print('2. Calculate the determinant of a matrix')
    print('3. Calculate the inverse of a matrix')
    print('4. Make it REF')
    print('5. Make it RREF')
    print('6. Calculate solution of a system of linear equations')
    print('7. Go back to the main menu')

