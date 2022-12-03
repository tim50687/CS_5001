from chessboard import *


def black_or_white(row, column):
    """
    Function --
        Return Black/ White based on the row and column passed in
    Parameters --
        row: row number of chessboard
        column: column number of chessboard
    Return --
        "BLACK" or "WHITE": if the column and row are valid input
        False: if the column or row is invalid input
    """
    # Precondition: row and column need to be valid input
    if not check_valid_column(column) or not check_valid_row(int(row)):
        return False
    # if ord(chr) is odd or row number is odd return BLACK
    elif ord(column.lower()) % 2 != 0 and int(row) % 2 != 0:
        return "BLACK"
    # if ord(chr) is even or row number is even return BLACK
    elif ord(column.lower()) % 2 == 0 and int(row) % 2 == 0:
        return "BLACK"
    # else return "WHITE"
    else:
        return "WHITE"


if __name__ == "__main__":
    print(black_or_white(8, "H"))
