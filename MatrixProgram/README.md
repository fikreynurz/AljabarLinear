# Matrix in Python

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Example Usage](#example-usage)

## General Info
This repository contains the code for a `Matrix` class in Python, allowing for the creation of, manipulation of, and operation on matrices. All code was created by me, Isaac Joffe, in November of 2021.

## Technologies
All code contained is written in Python 3.8.10, except for the makefile used to run unit tests. I created all the code and files in this repository using my personal virtual machine, which runs the Ubuntu distribution of the Linux operating system, through the Sublime Text text editor and the Linux terminal window.

## Instructions
Currently, the program can only be used directly through a Python interpreter. Upon entering the Python interpreter using `python3` in the Linux terminal window, you can import the class using `from matrix import Matrix` and begin to use the functionality of the class by instantiating objects and operating on them.

Additionally, unit tests are available to test the functionality of the program. The provided makefile allows for the execution of all the available tests at once. To run all the tests, in the Linux terminal type `make` while in the proper directory.

## Example Usage
```python
from matrix import Matrix

my_matrix = Matrix([[1,2,3],[4,5,6]])    # Instantiates a 2 x 3 matrix
print(my_matrix)    # Prints a readable representation of the matrix

my_matrix.add_row([7,8,9])    # Appends another row to the bottom
print(my_matrix)    # Prints a readable representation of the matrix

my_matrix = my_matrix.transpose()    # Transposes matrix
print(my_matrix)    # Prints a readable representation of the matrix
print(my_matrix.determinant())    # Prints the scalar determinant of a matrix
```
