"""
    CS 5001
    Fall 2022
    Jen Ting Huang
    Homework4: Programming #3
"""


def is_valid_upc(list_of_integers):
    """
    Function --
        Pass in the upc number and check if it's valid
    Parameter --
        list_of_intergers: list of possible UPC number
    Return --
        boolean: True if it's valid, otherwise False
    """
    # Precondition
    if len(list_of_integers) < 2:
        return False
    # Need to iterate backwards in a list,
    # because UPC code start from right to left
    result = 0
    for i in range(len(list_of_integers) - 1, -1, -1):
        # Do upc calculation based on the right index of two numbers.
        # ex. [2, 3, 5, 1]
        # Do the upc calculation only by index 3 and 1
        if (len(list_of_integers) % 2 == 0 and i % 2 == 0) or (
            len(list_of_integers) % 2 != 0 and i % 2 != 0
        ):
            continue
        # Because I calculate UPC by right index of two numbers,
        # for odd amount of input numbers,
        # if i == 0, since there's no number in the left,
        # therefore, only need to add value of index 0 to result
        if len(list_of_integers) % 2 != 0 and i == 0:
            result += list_of_integers[i]
        else:
            result += list_of_integers[i] + (list_of_integers[i - 1] * 3)
    # Check if result is valid by divided by 10
    # True = valid, False = invalid
    # print(result)
    if result == 0:
        return False
    else:
        return result % 10 == 0


print(is_valid_upc([0, 0, 0, 0, 0]))
