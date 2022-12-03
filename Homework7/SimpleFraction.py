"""
    CS 5001
    Fall 2022
    Jen Ting Huang
    Homework 7: Simple Fraction
"""


class SimpleFraction:
    """
    A class to represent fraction.

    Attributes
    ----------
    numerator : int
        Numerator of the fraction.
    denominator : int
        Denominator of the fraction.

    Method
    ------
    get_numerator():
        Returns the value of the SimpleFraction's numerator.
    get_denominator():
        Returns the value of the SimpleFraction's denominator.
    make_reciprocal():
        Returns a new SimpleFraction instance that has the current
        instance’s numerator as its denominator, and the current
        instance’s denominator as its numerator. This is a NON-MUTATING
        method, so the current instance is not modified. A new
        SimpleFraction instance is returned.
    validate():
        Checks to ensure that the numerator and denominator
        are integers. If either of the values are NOT integers,
        this method raises a ValueError.
    multiply(other):
        Multiplies the current instance with another SimpleFraction OR
        a whole number (scalar). Returns the result.This is a NON-MUTATING
        method, so the current instance is not modified.
        A new SimpleFraction instance is returned.
    divide(other):
        Divides the current instance with another SimpleFraction OR
        a whole number (scalar). Returns the result. This is a
        NON-MUTATING method, so the current instance is not modified.
        A new SimpleFraction instance is returned.
    __str__():
        Returns a string representation of SimpleFraction instances.
    __eq__():
        Compares current SimpleFraction instance to another one.
        Returns True if they are equal, False otherwise.
    """

    def __init__(self, numerator=1, denominator=1):
        """
        Construct all necessary attributes for the
        Simplefraction object.

        If both numerator and denominator are not integers, raise ValueError.
        If denominator == 0, raise ZeroDivisionError.

        Parameters
        ----------
        numerator : int
            Numerator of the fraction.
        denominator : int
            Denominator of the fraction.
        """
        self.numerator = numerator
        self.denominator = denominator
        # Check if object's has valid input data type
        self.validate()

    def get_numerator(self):
        """
        Returns the value of the Fraction's numerator.

        Parameter
        ---------
        None

        Returns
        -------
        The SimpleFraction's numerator
        """
        return self.numerator

    def get_denominator(self):
        """
        Returns the value of the Fraction's denominator.

        Parameter
        ---------
        None

        Returns
        -------
        The SimpleFraction's denominator
        """
        return self.denominator

    def make_reciprocal(self):
        """
        Returns a new SimpleFraction instance that has the current instance's
        numerator as its denominator, and the current instance's denominator
        as its numerator.

        This is a NON-MUTATING method.

        Parameter
        ---------
        None

        Returns
        -------
        New SimpleFraction instance that has the current instance's
        numerator as its denominator, ans the current instance's denominator
        as its numerator.
        """
        return SimpleFraction(self.denominator, self.numerator)

    def validate(self):
        """
        Check to ensure that the numerator and denominator are
        integers.

        Denominator cannot be 0

        Parameter
        ---------
        None

        Returns
        -------
        None
        """
        numerator_int_bool = isinstance(self.numerator, (int))
        denominator_int_bool = isinstance(self.denominator, (int))
        # Raise ValueError if numerator and denominator are not integer.
        if (numerator_int_bool and denominator_int_bool) is False:
            raise ValueError("Both number should be integer!!!")
        elif self.denominator == 0:
            raise ZeroDivisionError
        return None

    def multiply(self, other):
        """
        Multiplies the current instance with another SimpleFraction OR
        a whole number.

        This is a NON-MUTATION method

        Parameter
        ---------
        other : int, Simple Fraction's instance
            Another SimpleFraction OR a whole number.

        Return
        ------
        New SimpleFraction instance of current instance
        multiplies integer pass in other.
        """
        # If other == integer
        if isinstance(other, (int)):
            return SimpleFraction(self.numerator * other, self.denominator)
        # If other == SimpleFraction's instance
        elif isinstance(other, SimpleFraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return SimpleFraction(new_numerator, new_denominator)
        else:
            raise ValueError("Enter integer or SimpleFraction's instance")

    def divide(self, other):
        """
        Divides the current instance with another SimpleFraction OR
        a whole number.

        This is a NON-MUTATION method

        Parameter
        ---------
        other : int, Simple Fraction's instance
            Another SimpleFraction OR a whole number.

        Return
        ------
        New SimpleFraction instance of current instance
        divided by integer pass in other.
        """
        # If other == integer
        if isinstance(other, (int)):
            return SimpleFraction(self.numerator, self.denominator * other)
        # If other == SimpleFraction's instance
        elif isinstance(other, SimpleFraction):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return SimpleFraction(new_numerator, new_denominator)
        else:
            raise ValueError("Enter integer or SimpleFraction's instance")

    def __str__(self):
        """
        Returns a string representation of SimpleFraction instances.

        Parameter
        ---------
        None

        Return
        ------
        None
        """
        if self.numerator == 0:
            return "0"
        else:
            return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        """
        Compares current SimpleFraction instance to another one.

        Will returns ValueError
        if pass non-SimpleFraction's object to other.

        Parameter
        ---------
        other : SimpleFration's instance
            Another SimpleFraction's instance

        Return
        ------
        True if they are equal, False otherwise.
        """
        if isinstance(other, SimpleFraction):
            return (self.numerator / self.denominator) == (
                other.numerator / other.denominator
            )
        # If other is not SimpleFraction's instance, then
        # raise ValueError
        else:
            raise ValueError("Enter SimpleFraction's instance")
