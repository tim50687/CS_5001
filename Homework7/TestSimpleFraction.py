import unittest
from SimpleFraction import SimpleFraction


class TestSimpleFraction(unittest.TestCase):
    """Unit test for SimpleFraction class"""

    @classmethod
    def setUpClass(cls):
        print("Setup Class!!!")
        print("--------------")

    @classmethod
    def tearDownClass(cls):
        print("----------------")
        print("Test finished!!!")

    def setUp(self):
        """Create a SimpleFractions object before every test"""
        self.frac = SimpleFraction(3, 5)

    def test_init(self):
        """Make sure SimlpeFraction's instance have correct attributes value."""
        default_frac = SimpleFraction()

        # Default value be passed in -> 1 to denominator, 1 to numerator
        self.assertEqual(default_frac.get_denominator(), 1)
        self.assertEqual(default_frac.get_numerator(), 1)
        # If user supply parameter
        self.assertEqual(self.frac.get_denominator(), 5)
        self.assertEqual(self.frac.get_numerator(), 3)

    def test_get_numerator(self):
        """Should return object's numerator"""
        self.assertEqual(self.frac.get_numerator(), 3)

    def test_get_denominator(self):
        """Should return object's denominator"""
        self.assertEqual(self.frac.get_denominator(), 5)

    def test_make_reciprocal(self):
        """Should returns new SimpleFraction instance's reciprocal"""
        reciprocal = SimpleFraction(5, 3)
        self.assertEqual(self.frac.make_reciprocal(), reciprocal)

    def test_validate(self):
        """Make sure SimpleFraction's object has valid input data type"""
        # Both denominator and numerator should be integer
        with self.assertRaises(ValueError):
            frac2 = SimpleFraction("test", 1)
        with self.assertRaises(ValueError):
            frac3 = SimpleFraction(2, [123])
        # Denominator should not be 0, if so, raise ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            frac4 = SimpleFraction(2, 0)

    def test_multiply(self):
        """Should return correct multiplication number"""
        # If argument == integer
        x5Frac = SimpleFraction(15, 5)
        self.assertEqual(self.frac.multiply(5), x5Frac)
        # If argument == SimpleFraction's object
        new_frac = SimpleFraction(2, 2)
        ans = SimpleFraction(6, 10)
        self.assertEqual(self.frac.multiply(new_frac), ans)
        # If user supply data other than ineger and SimpleFraction's oobject,
        # should raise ValueError
        with self.assertRaises(ValueError):
            frac = self.frac.multiply("test")

    def test_divide(self):
        """Should return correct number after division"""
        # If argument == integer
        Div5Frac = SimpleFraction(3, 25)
        self.assertEqual(self.frac.divide(5), Div5Frac)
        # If argument == SimpleFraction's object
        new_frac = SimpleFraction(3, 2)
        ans = SimpleFraction(6, 15)
        self.assertEqual(self.frac.divide(new_frac), ans)
        # If user supply data other than ineger and SimpleFraction's oobject,
        # should raise ValueError
        with self.assertRaises(ValueError):
            frac = self.frac.divide("test")

    def test_str(self):
        """Should Return string representation of the SimpleFraction's object"""
        self.assertEqual(self.frac.__str__(), "3/5")
        # If numerator of SimpleFraction's object == 0, should return 0
        new_frac = SimpleFraction(0, 3)
        self.assertEqual(new_frac, 0)

    def test_eq(self):
        """Return True if SimpleFraction's object is equal to target fraction, False otherwise"""
        # Should return True if target fraction is equal.
        compare_frac = SimpleFraction(3, 5)  # Compare to object
        self.assertEqual(self.frac.__eq__(compare_frac), True)
        # Should return False if target fraction is not equal
        not_equal_frac = SimpleFraction(2, 7)
        self.assertEqual(self.frac.__eq__(not_equal_frac), False)


def main():
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
