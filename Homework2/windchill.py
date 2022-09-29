'''
    CS5001
    Fall 2022
    Jen Ting Huang
    Homework 2: Programming #2
'''
from temperature_conversion import *

# 1mph = 1.609344kmh
MPH2KMH = 1.609344


def calculate_windchill(temperature, speed):
    '''
    Function: calculate_windchill
        Calculates windchill based on international formula (Metric)
    Parameters:
        temperature: in Fahrenheit
        speed: in miles per hour
    Returns: windchill index (floating point value) based on applied formula
    Require: temp/speed in metric units
    Ensure: metric -> imperial unit conversions prior to calculation
    '''
    # convert the Fahrenheit to Celcius
    temperature = convert_fahrenheit_to_celsius(temperature)

    # convert miles-per-hour to kilometers-per-hour
    speed *= MPH2KMH

    # calculate the windchill index
    windchill_index = 13.12 + (0.6215 * temperature) - 11.37 * \
        (speed ** 0.16) + 0.3965 * \
        temperature * (speed ** 0.16)

    # return the result (turn Celcius to Fahrenheit)
    return convert_celsius_to_fahrenheit(windchill_index)


if __name__ == "__main__":
    print(calculate_windchill(45, 15.5))
