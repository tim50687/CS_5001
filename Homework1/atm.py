'''
    CS 5001
    Fall 2022
    HW1 - Program 2

    Jen Ting Huang
'''

'''
Test case #1:
Input: $5
Output: 0 fifties, 0 twenties, 0 tens, 1 fives, 0 ones

Test case #2:
Input: $16
Output: 0 fifties, 0 twenties, 1 tens, 1 fives, 1 ones

Test case #3:
Input: $43
Output: 0 fifties, 2 twenties, 0 tens, 0 fives, 3 ones
'''

def main():
    '''
    Function --
        Make an ATM which can do only one task:
        Determine the numbers of bills for each type dispensed.

        Note: ATM use the fewest number of bills that it can to
              dispense the specified amount of money.
              It only dispenses fifties, tens, fives, and ones.
    :return:
        none
    '''
    # Get the amount of money
    amount_to_withdraw = int(input("Welcome to PDQ Bank!"
                                   " Amount to withdraw? $ "))
    print("Cha-ching! You asked for $ {}".format(amount_to_withdraw))

    # Dispense the money
    # start to devide by 50, then 10, ..., 1
    # to get the fewest numbers of bills
    # 50
    fifties = amount_to_withdraw // 50
    remainder_of_fifties = amount_to_withdraw % 50

    # 20
    twenties = remainder_of_fifties // 20
    remainder_of_twenties = remainder_of_fifties % 20

    # 10
    tens = remainder_of_twenties // 10
    remainder_of_tens = remainder_of_twenties % 10

    # 5
    fives = remainder_of_tens // 5
    remainder_of_fives = remainder_of_tens % 5

    # 1
    ones = remainder_of_fives // 1

    # print out result
    print("That breaks down to:\n {} "
          "fifties\n {} "
          "twenties\n {} "
          "tens\n {} "
          "fives\n {} ones".format(fifties, twenties, tens, fives, ones))


if __name__ == '__main__':
    main()