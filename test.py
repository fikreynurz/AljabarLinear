import MatrixProgram.matrix as matrix
import iomodule.Display as Display
import operation.advanced as advanced

mat = matrix.Matrix([[0, -14, -8],
                     [1, 3, 2],
                     [-2, 0, 6]])

Display.printMatrix(advanced.row_echelon(mat))
