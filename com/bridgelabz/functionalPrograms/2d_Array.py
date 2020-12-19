from numpy import *


def two_dimensional_Array():
    """

    :rtype: matrix in 2d arrays
    """
    while True:
        try:
            rows = int(input("Enter the number of rows:"))
            columns = int(input("Enter the number of columns:"))
            print("Enter the entries in a single line (separated by space): ")
            entries = list(map(int, input().split()))  # User input of entries in a single line separated by space
            matrix = array(entries).reshape(rows, columns)  # Logic
            print(matrix)  # prints matrix
        except ValueError:
            print("Enter appropriate values matching Rows and columns ")


two_dimensional_Array()
