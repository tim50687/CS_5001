'''
    CS 5001
    Fall 2022
    HW1 - Program 1

    Jen Ting Huang
'''

def main():
    '''
    Function --
        Get the supplier fee per kWh and power fee per kWh for this month,
        and calculate the electric bill this month.
    :return:
        none
    '''
    # Get supplier fee per kWh
    supplier = float(input("What is the supplier fee per kWh? "))
    # Get power fee per kWh
    power = float(input("What is the power fee per kWh? "))
    # Get total kWh used in this month
    total_kWh = float(input("How many kWh were used this month? "))

    # Calculate electric bill of this month
    electric_bill_price = (supplier + power) * total_kWh

    print("Your electric bill this month is "
          "${:.2f}".format(electric_bill_price))


if __name__ == '__main__':
    main()