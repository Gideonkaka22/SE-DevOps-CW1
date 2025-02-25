import unittest
from Dec2Hex import decimal_to_hex  # Import the function you want to test

class TestDecimalToHex(unittest.TestCase):
    
    def test_valid_input(self):
        self.assertEqual(decimal_to_hex(10), 'A')  # Decimal 10 should return 'A'
        self.assertEqual(decimal_to_hex(255), 'FF')  # Decimal 255 should return 'FF'
        self.assertEqual(decimal_to_hex(0), '0')  # Decimal 0 should return '0'
    
    def test_invalid_input(self):
        # Test for invalid inputs (non-integer)
        self.assertEqual(decimal_to_hex("invalid"), "Error: Invalid input. Please enter a valid integer.")
        self.assertEqual(decimal_to_hex("123abc"), "Error: Invalid input. Please enter a valid integer.")
    
    def test_no_input(self):
        # Test for no input provided
        self.assertEqual(decimal_to_hex(""), "Error: Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    unittest.main()
