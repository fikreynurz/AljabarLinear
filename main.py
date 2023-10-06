import MatrixProgram.matrix as matrix
import iomodule.Display as Display
import operation.advanced as advanced


def getMatrixFromUser() -> matrix.Matrix:
    '''
    Gets a matrix from the user input.
    args:
        None
    
    returns:
        The matrix entered by the user.
    '''
    # Get the dimensions of the matrix.
    row, col = [int(input('Enter the number of rows: ')),
                int(input('Enter the number of columns: '))]
    
    # Get the matrix from the user.
    mat = []
    for i in range(row):
        row_input = []
        for j in range(col):
            while True:
                try:
                    element = float(input(f'Enter the element ({i + 1} {j + 1}): '))    
                    break
                except ValueError:
                    print('Input Invalid!')
                    pass
            row_input.append(element)
        mat.append(row_input)
    
    mat = matrix.Matrix(mat)
    return mat


def getTwoMatrices(matrices: dict) -> tuple[matrix.Matrix, matrix.Matrix]:
    '''
    Gets two matrices from dictionary by the user input.
    
    args:
        matrices: The dictionary of matrices.

    returns:
        The two matrices entered by the user.
    '''
    mat1 = input('Enter the name of the first matrix: ')
    if mat1 not in matrices:
        print(f'Matrix "{mat1}" does not exist. Please try again.')
        return

    mat2 = input('Enter the name of the second matrix: ')
    if mat2 not in matrices:
        print(f'Matrix "{mat2}" does not exist. Please try again.')
        return

    mat1 = matrices[mat1]
    mat2 = matrices[mat2]

    return mat1, mat2


def main():
    matrices = {}

    while True:
        Display.printMenu()
        try:
            match int(input('Enter your choice: ')):
                case 1:
                    # Check the available matrices.
                    if len(matrices) == 0:
                        print('No matrix available.')
                        continue

                    for name, mat in matrices.items():
                        print(f'{name}:')
                        Display.printMatrix(mat)
                case 2:
                    # Create a matrix.
                    if len(matrices) == 26:
                        print('Cannot create more than 26 matrices.')
                        continue

                    name = input('Enter the name of the matrix: ')

                    if name in matrices:
                        print('Matrix with this name already exists.')
                        continue

                    matrices[name] = getMatrixFromUser()
                    print(f'Matrix {name} created.')
                    Display.printMatrix(matrices[name])
                case 3:
                    # Delete a matrix.
                    if len(matrices) == 0:
                        print('No matrix to delete.')
                        continue

                    name = input('Enter the name of the matrix: ')

                    if name in matrices:
                        del matrices[name]
                        print(f'Matrix {name} deleted.')
                    else:
                        print('Matrix with this name does not exist.')
                case 4:
                    # Basic operations on matrices.
                    if len(matrices) == 0:
                        print('No matrix available.')
                        continue

                    Display.printBasicOperationsMenu()

                    try:
                        match int(input('Enter your choice: ')):
                            case 1:
                                # Add two matrices.
                                mat1, mat2 = getTwoMatrices(matrices)

                                if mat1 is None or mat2 is None:
                                    continue

                                try:
                                    result = mat1.matrix_add(mat2)
                                    print('The sum of the matrices is:')
                                    Display.printMatrix(result)
                                except AssertionError as e:
                                    print(e)
                            case 2:
                                # Subtract two matrices.
                                mat1, mat2 = getTwoMatrices(matrices)

                                if mat1 is None or mat2 is None:
                                    continue

                                try:
                                    result = mat1.matrix_sub(mat2)
                                    print('The difference of the matrices is:')
                                    Display.printMatrix(result)
                                except AssertionError as e:
                                    print(e)
                            case 3:
                                # Multiply two matrices.
                                mat1, mat2 = getTwoMatrices(matrices)

                                if mat1 is None or mat2 is None:
                                    continue

                                try:
                                    result = mat1.matrix_multiply(mat2)
                                    print('The product of the matrices is:')
                                    Display.printMatrix(result)
                                except AssertionError as e:
                                    print(e)
                            case 4:
                                # Multiply a matrix with a scalar.
                                mat = input('Enter the name of the matrix: ')

                                if mat not in matrices:
                                    print(f'Matrix "{mat}" does not exist. Please try again.')
                                    continue

                                scalar = float(input('Enter the scalar: '))
                                result = matrices[mat].scalar_multiply(scalar)
                                print('The product of the matrix with the scalar is:')
                            case 5:
                                # Go back to the main menu.
                                continue
                            case _:
                                print('Invalid choice. Please try again.')
                    except ValueError:
                        print('Invalid choice. Please try again.')
                case 5:
                    # Advanced operations on matrices.
                    if len(matrices) == 0:
                        print('No matrix available.')
                        continue
                        
                    Display.printAdvancedOperationsMenu()

                    try:
                        match int(input('Enter your choice: ')):
                            case 1:
                                # Transpose a matrix.
                                mat = input('Enter the name of the matrix: ')

                                if mat not in matrices:
                                    print(f'Matrix "{mat}" does not exist. Please try again.')
                                    continue

                                result = matrices[mat].transpose()
                                print('The transpose of the matrix is:')
                                Display.printMatrix(result)
                            case 2:
                                # Find the determinant of a matrix.
                                mat = input('Enter the name of the matrix: ')

                                if mat not in matrices:
                                    print(f'Matrix "{mat}" does not exist. Please try again.')
                                    continue

                                try:
                                    result = matrices[mat].determinant()
                                    print(f'The determinant of the matrix is: {result}')
                                except AssertionError as e:
                                    print(e)
                            case 3:
                                # Find the inverse of a matrix.
                                mat = input('Enter the name of the matrix: ')

                                if mat not in matrices:
                                    print(f'Matrix "{mat}" does not exist. Please try again.')
                                    continue

                                try:
                                    result = advanced.inverse(matrices[mat])
                                    print('The inverse of the matrix is:')
                                    Display.printMatrix(result)
                                except AssertionError as e:
                                    print(e)
                            case 4:
                                # Find the row echelon form of a matrix.
                                mat = input('Enter the name of the matrix: ')

                                if mat not in matrices:
                                    print(f'Matrix "{mat}" does not exist. Please try again.')
                                    continue

                                try:
                                    result = advanced.row_echelon(matrices[mat])
                                    print('The row echelon form of the matrix is:')
                                    Display.printMatrix(result)
                                except AssertionError as e:
                                    print(e)
                            case 5:
                                # Find the reduced row echelon form of a matrix.
                                mat = input('Enter the name of the matrix: ')

                                if mat not in matrices:
                                    print(f'Matrix "{mat}" does not exist. Please try again.')
                                    continue

                                try:
                                    result = advanced.reduced_row_echelon(matrices[mat])
                                    print('The reduced row echelon form of the matrix is:')
                                    Display.printMatrix(result)
                                except AssertionError as e:
                                    print(e)
                            case 6:
                                # Calculate solution of a system of linear equations.
                                mat = input('Enter the name of the matrix: ')

                                if mat not in matrices:
                                    print(f'Matrix "{mat}" does not exist. Please try again.')
                                    continue

                                b = input('Enter the name of the vector: ')

                                if b not in matrices:
                                    print(f'Vector "{b}" does not exist. Please try again.')
                                    continue

                                try:
                                    result = advanced.solve(matrices[mat], matrices[b])
                                    print('The solution of the system of linear equations is:')
                                    Display.printMatrix(result)
                                except AssertionError as e:
                                    print(e)
                            case 7:
                                # Go back to the main menu.
                                continue
                            case _:
                                print('Invalid choice. Please try again.')
                    except ValueError:
                        print('Invalid choice. Please try again.')
                case 6:
                    # Exit the program.
                    print('Exiting the program.')
                    exit()
                case _:
                    print('Invalid choice. Please try again.')

        except ValueError:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
