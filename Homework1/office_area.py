'''
    CS 5001
    Fall 2022
    HW1 - Program 3

    Jen Ting Huang
'''

def main():
    '''
    Function --
        Display the area in square-feet and square-meters,
        by input length and width.
        Calculate the cost of the office in Eurodollars.
    :return:
        none
    '''

    # Get the length of the office
    length = float(input("Enter the length of the office (in feet) "))
    # Get the width of the office
    width = float(input("Enter the width of the office (in feet) "))
    # Calculate the area in square-feet
    area_square_feets = length * width
    # Turn area in to square-meters
    area_square_meters = area_square_feets * 0.092903
    # Calculate the cost of the office in Euros
    cost = area_square_meters * 21.10

    print("The area of the office is {:.2f}"
          " square feet".format(area_square_feets))
    print("...which is {:.2f} square meters".format(area_square_meters))
    print("......and you will pay €{:.2f} per month".format(cost))

if __name__ == '__main__':
    main()