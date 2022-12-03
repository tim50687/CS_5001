"""
    CS 5001
    Fall 2022
    Jen Ting Huang
    Homework4: Programming #1
"""
from hw4data import *


def decode(encoded_list):
    """
    Function --
        Take a list of RLE-encoded values, and decode it.
    Parameter --
        encoded list: list of RLE-encoded values
    Return --
        Decoded list
    """
    decoded_list = []
    # Go through every value
    for i in range(0, len(encoded_list), 2):
        # Append each value nth times
        # Based on count of occurences for the run
        for j in range(encoded_list[i + 1]):
            decoded_list.append(encoded_list[i])
    return decoded_list


def practice(decoded_list):
    """
    Function --
        Convert the decoded list into one string value
    Parameter --
        decoded_list: decoded RLE list
    Return --
        String value of decoded RLE list
    """
    string = "".join(decoded_list)
    return string


print(decode(DATA4))
# print(practice(decode(DATA5)))
