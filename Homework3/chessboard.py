def check_valid_row(row):
    """
    Function --
        Check if it is valid row number
    Parameter --
        row: row number
    Return --
        True if row number is valid, otherwise False
    """
    number = 1
    while number < 9:
        if number == int(row):
            return True
        number += 1
    return False


def check_valid_column(column):
    """
    Function --
        Check if it is valid column character
    Parameter --
        column: column character
    Return --
        True if column character is valid, otherwise False
    """
    chr_dec = 97  # chr "a" to decimal
    column = ord(column.lower())
    while chr_dec < 105:
        if chr_dec == int(column):
            return True
        chr_dec += 1
    return False


if __name__ == "__main__":
    print(check_valid_row(4))
    print(check_valid_column("E"))
