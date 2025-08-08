import unittest
from test_simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various scenarios"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test adding zero
        self.assertEqual(self.calc.add(5, 0), 5)
        # Test commutative property
        self.assertEqual(self.calc.add(3, 2), self.calc.add(2, 3))
        # Test with floats
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction(self):
        """Test the subtract method with various scenarios"""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test subtracting zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        # Test subtracting from zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Test with floats
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    def test_multiply(self):
        """Test the multiply method with various scenarios"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test multiplying by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        # Test commutative property
        self.assertEqual(self.calc.multiply(3, 2), self.calc.multiply(2, 3))
        # Test with floats
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)
        # Test identity property
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_divide(self):
        """Test the divide method with various scenarios"""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test division resulting in float
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        # Test division by one
        self.assertEqual(self.calc.divide(5, 1), 5)
        # Test division of zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test with floats
        self.assertAlmostEqual(self.calc.divide(0.3, 0.1), 3, places=7)
        # Test negative division
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)

if __name__ == '__main__':
    unittest.main()