# Made by Isaac Joffe
from copy import deepcopy


class Matrix:
    """
    A class to represent a matrix, a two-dimensional array of numbers.

    Attributes
    ----------
        values : list of lists of integer/floating point numbers
            all the elements of the matrix, where each list inside the list
            contains all the elements of a row of the matrix
        m : integer
            numbers of rows in the matrix (for an m x n matrix)
        n : integer
            number of columns in the matrix (for an m x n matrix)

    Methods
    -------
        get_size() :
            gives the size of the matrix (for an m x n matrix)
        get_value() :
            gives the value of a specified element of the matrix
        set_value() :
            changes the value of a specified element of the matrix
        check_validity() :
            determines if the matrix's elements are numbers and if each row
            has the same number of elements (number of columns is constant)
        add_row(row) :
            adds a row of numbers to the matrix
        add_rows(rows) :
            adds a list of rows to the matrix
        delete_row(row) :
            deletes a specified row of the matrix
        add_column(column) :
            adds a column of numbers to the matrix
        add_columns(columns) :
            adds a list of columns to the matrix
        delete_column(column) :
            deletes a specified column of the matrix
        scalar_add(number) :
            adds a specified number to every element of the matrix
        scalar_multiply(number) :
            multiplies each element of the matrix by a specified number
        matrix_add(otherMatrix) :
            adds two matrices together, producing a new matrix
        matrix_multiply(otherMatrix) :
            multiplies two matrices together, producing a new matrix
        transpose() :
            transposes the matrix, producing a new matrix
        determinant() :
            gives the value of the determinant of the matrix

    Example Usage
    -------------
        A = Matrix([[1,2,3],[4,5,6],[7,8,9]])    # 3 x 3 matrix
        B = Matrix([[1,2,3]])    # Row vector
        C = Matrix([[1],[2],[3]])    # Column vector
    """

    def __init__(self, values):
        """
        Instantiates the matrix, assigning all the attributes of the matrix
        either as an empty matrix or based on the inputted values.

        Parameters
        ----------
        values : list of lists of integer/floating point numbers
            elements to be placed in the matrix in the form of row vectors

        Returns
        -------
            None, but creates the matrix
        """

        # Ensure argument passed in is valid
        assert values and isinstance(values, list), \
            "Argument must be a list of lists of numbers."
        for i in values:
            assert i and isinstance(i, list), \
                "Argument must be a list of lists of numbers."
            for j in i:
                assert isinstance(j, int) or isinstance(j, float), \
                    "Argument must be a list of lists of numbers."

        # Instantiate an empty matrix
        self.values = []
        self.__m = 0
        self.__n = 0
        self.add_rows(values)    # Add rows
        self.check_validity()    # Ensure matrix is valid

        return

    def __str__(self):
        """
        Gives a string representation of the matrix as a grid of numbers.

        Parameters
        ----------
            None

        Returns
        -------
            matrixString : string
                elements of the matrix represented in an easily printable and
                human-readable form
        """

        # Determine the largest number of characters among all the elements
        maxLength = 0
        for i in self.values:
            for j in i:
                if len(str(j)) > maxLength:    # Check if longest number
                    maxLength = len(str(j))    # Mark a new maximum length

        # Pad each element with necessary whitespace for readablity
        stringValues = []
        for i in self.values:
            rowValues = []
            for j in i:
                # Create a right-justified string representation of element
                # according to the largest length seen
                rowValues.append(str(j).rjust(maxLength))
            stringValues.append(rowValues)

        # Join strings representing each element into one single string
        matrixString = []
        for i in stringValues:
            # Join elements of each row into a space-separated string
            matrixString.append(" ".join(i))
        # Join each row into a newline-separated string
        matrixString = "\n".join(matrixString)

        return(matrixString)

    def __repr__(self):
        """
        Gives an official string representation of the matrix.

        Parameters
        ----------
            None

        Returns
        -------
            matrixString : string
                official string representation of the matrix, contaning the
                size of the matrix and the object's id
        """

        m, n = self.get_size()
        matrixString = "{} x {} Matrix object with id of {}.".format(
            m, n, str(id(self)))    # Set up message

        return(matrixString)

    def get_size(self):
        """
        Gives the size of the matrix.

        Parameters
        ----------
            None

        Returns
        -------
            m : integer
                number of rows in the matrix
            n : integer
                number of columns in the matrix
        """

        m, n = self.__m, self.__n    # Get info from private attributes

        return(m, n)

    def get_value(self, row, column):
        """
        Gives the value of a specified element of the matrix.

        Parameters
        ----------
            row : integer
                row number of desired element
            column : integer
                column number of desired element

        Returns
        -------
            value : integer/floating point number
                value of the element at the given location
        """

        # Ensure arguments passed in are valid
        assert isinstance(row, int) and isinstance(column, int), \
            "Location must be an integer value."
        m, n = self.get_size()
        assert row > 0 and column > 0 and row <= m and column <= n, \
            "Matrix must be defined at the given location."

        value = self.values[row-1][column-1]    # Index into matrix

        return(value)

    def set_value(self, row, column, value):
        """
        Changes the value of a specified element of the matrix.

        Parameters
        ----------
            row : integer
                row number of element to be changed
            column : integer
                column number of element to be changed
            value : integer/floating point number
                new value for the specified element to take

        Returns
        -------
            None, but updates the matrix elements
        """

        # Ensure arguments passed in are valid
        assert isinstance(row, int) and isinstance(column, int), \
            "Location must be an integer value."
        assert isinstance(value, int) or isinstance(value, float), \
            "Value must be a number."
        m, n = self.get_size()
        assert row > 0 and column > 0 and row <= m and column <= n, \
            "Matrix must be defined at the given location."

        self.values[row-1][column-1] = value    # Update value in matrix
        self.check_validity()    # Double check that matrix is still valid

        return

    def check_validity(self):
        """
        Checks if the existing matrix is valid, meaning the matrix has
        elements which are exclusively integer/floating point numbers and has
        all its rows of the same length.

        Paramters
        ---------
            None

        Returns
        -------
            None, but terminates if the matrix is invalid
        """

        m, n = self.get_size()
        for i in self.values:
            assert i, "Matrix must not be empty."
            # Terminate if the rows are of different length
            assert len(i) == n, "Rows must be of same length."
            for j in i:
                # Terminate if any element is not a number
                assert isinstance(j, float) or isinstance(j, int), \
                    "Elements must be numbers."

        return

    def add_row(self, row):
        """
        Appends a single row to the bottom of the existing matrix.

        Parameters
        ----------
            row : list of integer/floating point numbers
                elements of the row to be added to the matrix

        Returns
        -------
            None, but updates the existing matrix

        See Also
        --------
            add_rows(rows) :
                wrapper function that appends multiple rows at once by calling
                this function repeatedly
        """

        # Ensure argument passed in is valid
        assert row and isinstance(row, list), \
            "Argument must be a list of numbers."
        for i in row:
            assert isinstance(i, int) or isinstance(i, float), \
                "Argument must be a list of numbers."
        m, n = self.get_size()
        if self.values:    # Since it may be the first row
            assert len(row) == n, "Rows must be of same length."

        self.values.append(row)    # Add the new row
        self.__m += 1    # Update number of rows
        self.__n = len(row)    # Update number of columns
        self.check_validity()    # Double check that matrix is still valid

        return

    def add_rows(self, rows):
        """
        Appends multiple rows to the bottom of the existing matrix.

        Parameters
        ----------
            rows : list of lists of integer/floating point numbers
                elements of the rows to be added to the matrix

        Returns
        -------
            None, but updates the existing matrix

        See Also
        --------
            add_row(row) :
                adds each individual row from the rows variable
        """

        # Ensure argument is valid
        assert rows and isinstance(rows, list), \
            "Argument must be a list of lists of numbers."
        for i in rows:
            assert i and isinstance(i, list), \
                "Argument must be a list of lists of numbers."
            for j in i:
                assert isinstance(j, int) or isinstance(j, float), \
                    "Argument must be a list of lists of numbers."

        for i in rows:
            self.add_row(i)    # Add row by row
        self.check_validity()    # Double check that matrix is still valid

        return

    def delete_row(self, row):
        """
        Removes a specified row of the matrix, moving all rows below up one.

        Parameters
        ----------
            row : integer
                the number of the row to be removed

        Returns
        -------
            None, but updates the existing matrix
        """

        # Ensure argument is valid
        assert isinstance(row, int), "Row index must be an integer."
        m, n = self.get_size()
        assert row > 0 and row <= m, \
            "Matrix must be defined at the given location."
        assert m != 1, "Matrix must have more than one row."

        del self.values[row-1]    # Remove the list for that row
        self.__m -= 1
        self.check_validity()    # Double check that matrix is still valid

        return

    def add_column(self, column):
        """
        Appends a single column to the end of the matrix.

        Parameters
        ----------
            column : list of integer/floating point numbers
                elements of the column to be added to the matrix

        Returns
        -------
            None, but updates the existing matrix

        See Also
        --------
            add_columns(columns) :
                wrapper function that appends multiple columns at once by
                calling this function repeatedly
        """

        # Ensure argument passed in is valid
        assert column and isinstance(column, list), \
            "Argument must be a list of numbers."
        for i in column:
            assert isinstance(i, int) or isinstance(i, float), \
                "Argument must be a list of numbers."
        m, n = self.get_size()
        assert len(column) == m, "Columns must be of same length."

        for i in range(len(self.values)):
            self.values[i].append(column[i])    # Add the new column
        self.__m = len(column)    # Update number of rows
        self.__n += 1    # Update number of columns
        self.check_validity()    # Double check that matrix is still valid

        return

    def add_columns(self, columns):
        """
        Appends multiple columns to the end of the matrix.

        Parameters
        ----------
            columns : list of lists of integer/floating point numbers
                elements of the columnss to be added to the matrix

        Returns
        -------
            None, but updates the existing matrix

        See Also
        --------
            add_column(column) :
                adds each individual column from the columns variable
        """

        # Ensure argument is valid
        assert columns and isinstance(columns, list), \
            "Argument must be a list of lists of numbers."
        for i in columns:
            assert i and isinstance(i, list), \
                "Argument must be a list of lists of numbers."
            for j in i:
                assert isinstance(j, int) or isinstance(j, float), \
                    "Argument must be a list of lists of numbers."

        for i in columns:
            self.add_column(i)    # Add column by column
        self.check_validity()    # Double check that matrix is still valid

        return

    def delete_column(self, column):
        """
        Removes a specified column of the matrix, moving all columns to the
        right to the left by one.

        Parameters
        ----------
            column : integer
                the number of the column to be removed

        Returns
        -------
            None, but updates the existing matrix
        """

        # Ensure argument is valid
        assert isinstance(column, int), "Column index must be an integer."
        m, n = self.get_size()
        assert column > 0 and column <= n, \
            "Matrix must be defined at the given location."
        assert n != 1, "Matrix must have more than one column."

        for i in range(len(self.values)):
            del self.values[i][column-1]
        self.__n -= 1
        self.check_validity()    # Double check that matrix is still valid

        return

    def scalar_add(self, number):
        """
        Adds a scalar number to each element of the matrix.

        Parameters
        ----------
            number : integer/floating point number
                the scalar number to be added to the matrix

        Returns
        -------
            None, but updates the existing matrix
        """

        assert isinstance(number, int) or isinstance(number, float), \
            "Argument must be a number."

        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                self.values[i][j] += number    # Increase each value by number
        self.check_validity()

        return

    def scalar_multiply(self, number):
        """
        Multiplies each element of the matrix by some scalar number.

        Parameters
        ----------
            number : integer/floating point number
                the scalar number for the matrix to be mutiplied by

        Returns
        -------
            None, but updates the existing matrix
        """

        # Ensure argument is valid
        assert isinstance(number, int) or isinstance(number, float), \
            "Argument must be a number."

        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                self.values[i][j] *= number    # Multiply each value by number
        self.check_validity()

        return

    def matrix_add(self, otherMatrix):
        """
        Produces the resultant matrix from adding two matrices together.

        Parameters
        ----------
            otherMatrix : object of class Matrix
                the other matrix to be added to the active matrix

        Returns
        -------
            newMatrix : object of class Matrix
                the resultant matrix from the addition of the other matrices
        """

        # Ensure argument is valid
        assert isinstance(otherMatrix, Matrix), \
            "Argument must be a matrix."
        m1, n1 = self.get_size()
        m2, n2 = otherMatrix.get_size()
        assert m1 == m2 and n1 == n2, "Matrices must be the same size."

        # Instantiate the zero matrix of the right size as a placeholder
        newMatrix = Matrix([[0 for i in range(n1)] for j in range(m1)])

        for i in range(m1):
            for j in range(n1):
                # New element value is sum of the value of the elements in the
                # same location in each input matrix
                newMatrix.values[i][j] = self.values[i][j] + \
                    otherMatrix.values[i][j]

        return(newMatrix)

    def matrix_multiply(self, otherMatrix):
        """
        Produces the resultant matrix from multiplying two matrices together.
        To be clear, this method outputs the result of (self * otherMatrix),
        not (otherMatrix * self).

        Parameters
        ----------
            otherMatrix : object of class Matrix
                the other matrix to be multiplied with the active matrix

        Returns
        -------
            newMatrix : object of class Matrix
                the resultant matrix from the multiplication of the other
                matrices
        """

        # Ensure argument is valid
        assert isinstance(otherMatrix, Matrix), \
            "Argument must be a matrix."
        m1, n1 = self.get_size()
        m2, n2 = otherMatrix.get_size()
        assert n1 == m2, "Matrices must be of compatible size."

        # Instantiate the zero matrix of the right size as a placeholder
        newMatrix = Matrix([[0 for i in range(n2)] for j in range(m1)])

        for i in range(m1):
            for j in range(n2):
                # New element value is sum of products of corresponding row
                # and column vectors of the matrices
                value = 0    # Initially set to zero
                for k in range(n1):
                    # Add the value of each relevant product to the cumulative
                    # value of the new element
                    value += self.values[i][k] * otherMatrix.values[k][j]
                newMatrix.values[i][j] = value    # Assign final value

        return(newMatrix)

    def transpose(self):
        """
        Produces the a matrix equivalent to the transpose of the existing
        matrix.

        Parameters
        ----------
            None

        Returns
        -------
            newMatrix : object of class Matrix
                the transpose of the original matrix
        """

        # Instantiate the zero matrix of the right size as a placeholder
        m, n = self.get_size()
        newMatrix = Matrix([[0 for i in range(m)] for j in range(n)])

        for i in range(m):
            for j in range(n):
                # Map each element from the existing matrix to the new location
                # on the resultant matrix
                newMatrix.values[j][i] = self.values[i][j]

        return(newMatrix)

    def determinant(self):
        """
        Computes the determinant of a square matrix.

        Parameters
        ----------
            None

        Returns
        -------
            value : integer/floating point number
                the scalar number representing the value of the determinant
        """

        # Ensure matrix is valid for determinant operation
        m, n = self.get_size()
        assert m == n, "Matrix must be square."

        if m == 1:    # Base case of recursion
            value = self.get_value(1, 1)    # Determinant is just only value
        else:    # Apply method of cofactor expansion
            value = 0
            for i in range(m):
                subMatrix = deepcopy(self)
                # Consider the sub matrix without the row and column that the
                # present element is in
                subMatrix.delete_row(1)
                subMatrix.delete_column(i+1)
                # Formula applies negative as needed, includes factor of
                # present element, and makes recursive call for the sub matrix
                value += (-1)**i*self.get_value(1, i+1)*subMatrix.determinant()

        return(value)
