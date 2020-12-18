from numpy import *


def two_dimensional_Array():
    while True:
        try:
            rows = int(input("Enter the number of rows:"))
            columns = int(input("Enter the number of columns:"))
            print("Enter the entries in a single line (separated by space): ")
            entries = list(map(int, input().split()))
            matrix = array(entries).reshape(rows, columns)
            print(matrix)
        except ValueError:
            print("Enter appropriate values matching Rows and columns ")


two_dimensional_Array()
