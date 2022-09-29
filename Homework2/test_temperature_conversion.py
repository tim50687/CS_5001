'''
    CS5001
    Fall 2022
    Jen Ting Huang
    Homework 2: Programming #1
'''

from temperature_conversion import convert_fahrenheit_to_celsius, convert_celsius_to_fahrenheit

def test_convert_fahrenheit_to_celcius(x, expect):
    '''
    Function --
        To show if the result of the function equals to expected answer
    :param x: The original temperature of the Fahrenheit
    :param expect: expected answer
    :return: void
    '''
    result = convert_fahrenheit_to_celsius(x)
    print("Converting {} F to Celcius --".format(x))
    print(">> result = {:.1f}  expected = {:.1f}\n".format(result, expect))
def test_convert_celsius_to_fahrenheit(x, expect):
    '''
    Function --
        To show if the result of the function equals to expected answer
    :param x: The original temperature of the Celcius
    :param expect: expected answer
    :return: void
    '''
    result = convert_celsius_to_fahrenheit(x)
    print("Converting {} C to Fahrenheit --".format(x))
    print(">> result = {:.1f}  expected = {:.1f}\n".format(result, expect))

def test_driver():
    '''
        Test Cases (F -> C):
        Test 1: Input (23) --> Expected result: -5
        Test 2: Input (-53) --> Expected result: -47.2
        Test 3: Input (0) --> Expected result: -17.8

        Test Cases (C -> F):
        Test 4: Input (-21) --> Expected result: -5.8
        Test 5: Input (1) --> Expected result: 33.8
        Test 6: Input (92) --> Expected result: 197.6

        '''
    # Test F -> C
    test_convert_fahrenheit_to_celcius(23, -5)
    test_convert_fahrenheit_to_celcius(-53, -47.2)
    test_convert_fahrenheit_to_celcius(0, -17.8)
    # Test C -> F
    test_convert_celsius_to_fahrenheit(-21, -5.8)
    test_convert_celsius_to_fahrenheit(1, 33.8)
    test_convert_celsius_to_fahrenheit(92, 197.6)

def main():
    test_driver()

if __name__ == "__main__":
    main()