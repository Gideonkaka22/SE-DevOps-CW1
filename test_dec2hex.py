import unittest
from unittest.mock import patch
import sys
from Dec2Hex import decimal_to_hex  # Import your actual function here

class TestDecimalToHex(unittest.TestCase):
    
    @patch('sys.argv', ['Dec2Hex.py', '255'])  # Mock sys.argv to simulate input argument
    def test_valid_input(self):
        result = decimal_to_hex(sys.argv[1])
        self.assertEqual(result, 'FF')  # Hex value for 255 is 'FF'

    @patch('sys.argv', ['Dec2Hex.py', 'invalid'])  # Mock invalid input
    def test_invalid_input(self):
        result = decimal_to_hex(sys.argv[1])
        self.assertEqual(result, "Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    unittest.main()

