import re
from chessboard import *


def test_valid_row(row, expect):
    """
    Function --
        To should if the return value of the function 
        is equal to expected value
    Parameters --
        row: row number of chessboard
        expect: expected answer
    Return --
        void
    """
    result = check_valid_row(row)
    print(f"Check if row {row} is valid.")
    print(f"Expected: {expect}, Actual: {result}")


def test_valid_column(column, expect):
    """
    Function --
        To should if the return value of the function 
        is equal to expected value
    Parameters --
        column: column character of chessboard
        expect: expected answer
    Return --
        void
    """
    result = check_valid_column(column)
    print(f"Check if column {column} is valid.")
    print(f"Expected: {expect}, Actual: {result}")


def test_squares():
    """
    Test Driver --
        Test Case 1 (column)
        Test 1: column: B --> Expected value: True
        Test 2: column: G --> Expected value: True
        Test 3: column: c --> Expected value: True
        Test 4: column: X --> Expected value: False

        Test Case 2 (row)
        Test 1: row: 0 --> Expected value: False
        Test 2: row: 4 --> Expected value: True
        Test 3: row: 97 --> Expected value: False
        Test 4: row: -22 --> Expected value: False
    """
    # Test column
    print("Test column")
    print("----------------------------------")
    test_valid_column("B", "True")
    test_valid_column("G", "True")
    test_valid_column("c", "True")
    test_valid_column("X", "False")
    print("\n")

    # Test row
    print("Test row")
    print("----------------------------------")
    test_valid_row(0, "False")
    test_valid_row(4, "True")
    test_valid_row(97, "False")
    test_valid_row(-22, "False")


if __name__ == "__main__":
    test_square()
