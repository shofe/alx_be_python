import unittest    #importing the in-built unittest module from python

from simple_calculator import SimpleCalculator   #importing the simpleClculator from simple_calculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self): 
        """Set up the SimpleCalculator instance before each test."""

        self.calc = SimpleCalculator()

    def test_addition(self):

        """Test the addition method."""

        self.assertEqual(self.calc.add(2, 3), 5)

        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):

        #Testing the subtraction method

        self.assertEqual(self.calc.subtract(2, 3), -1)

        self.assertEqual(self.calc.subtract(70, 3), 67)


    def test_multiplication(self):

        self.assertEqual(self.calc.multiply(4, 5), 20)

        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_division(self):
            
            
            self.assertEqual(self.calc.divide(2, 0), None)

            self.assertEqual(self.calc.divide(6, 2), 3)
            
                 
        





