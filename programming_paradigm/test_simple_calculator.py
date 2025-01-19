import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a SimpleCalculator instance for testing."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative + positive
        self.assertEqual(self.calc.add(0, 0), 0)  # Edge case: zeros

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Negative result
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Edge case: zeros

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)  # Positive numbers
        self.assertEqual(self.calc.multiply(-4, 5), -20)  # Negative * positive
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplication by zero

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # Normal division
        self.assertEqual(self.calc.divide(5, 2), 2.5)  # Division resulting in float
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero

# Run the tests
if __name__ == "__main__":
    unittest.main()
