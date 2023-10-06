import MatrixProgram.matrix as matrix
import iomodule.Display as Display
import operation.advanced as advanced

# crate a matrix 8x8 with random values make sure the value are random and not the same and doen't have a pattern
mat = matrix.Matrix([[1, 2, 3, 4, 5, 6, 7, 8],
                     [2, 3, 4, 5, 6, 7, 8, 1],
                     [3, 4, 5, 6, 7, 8, 1, 2],
                     [4, 5, 6, 7, 8, 1, 2, 3],
                     [5, 6, 7, 8, 1, 2, 3, 4],
                     [6, 7, 8, 1, 2, 3, 4, 5],
                     [7, 8, 1, 2, 3, 4, 5, 6],
                     [8, 1, 2, 3, 4, 5, 6, 7]])


Display.printMatrix(advanced.cofactor(mat))
