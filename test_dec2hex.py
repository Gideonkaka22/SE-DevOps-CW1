import unittest
from unittest.mock import patch
import sys
from Dec2Hex import decimal_to_hex  # Adjust import based on your file structure

class TestDecimalToHex(unittest.TestCase):

    @patch('sys.argv', ['Dec2Hex.py', '255'])  # Test for a valid positive integer
    def test_valid_input(self):
        result = decimal_to_hex(sys.argv[1])
        self.assertEqual(result, 'FF')  # Expected output for 255 in hex

    @patch('sys.argv', ['Dec2Hex.py', 'invalid'])  # Test for invalid input
    def test_invalid_input(self):
        result = decimal_to_hex(sys.argv[1])
        self.assertEqual(result, "Error: Invalid input. Please enter a valid integer.")

    @patch('sys.argv', ['Dec2Hex.py'])  # Test for no input
    def test_no_input(self):
        with self.assertRaises(IndexError):
            decimal_to_hex(sys.argv[1])  # This should raise an IndexError due to missing argument

    @patch('sys.argv', ['Dec2Hex.py', '0'])  # Test for zero input
    def test_zero_input(self):
        result = decimal_to_hex(sys.argv[1])
        self.assertEqual(result, '0')  # Expected output for 0 in hex

if __name__ == '__main__':
    unittest.main()

