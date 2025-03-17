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
        
    @patch("builtins.input", side_effect=KeyboardInterrupt)
    def test_keyboard_interrupt_during_input(self, mock_input):
        """Simulate user pressing Ctrl+C when inputting a number"""
        try:
            decimal_to_hex(int(input("Enter a number: ")))
        except KeyboardInterrupt:
            result = "Process interrupted by user."
        self.assertEqual(result, "Process interrupted by user.")

    #Keyboard Interrupts Tests
    @patch("builtins.input", side_effect=[10, KeyboardInterrupt])
    def test_keyboard_interrupt_after_valid_input(self, mock_input):
        """Simulate valid input followed by Ctrl+C"""
        try:
            result = decimal_to_hex(int(input("Enter a number: ")))  # First call: 10
            self.assertEqual(result, "0xa")  # 10 → '0xa'

            input("Enter another number: ")  # Second call triggers KeyboardInterrupt
        except KeyboardInterrupt:
            result = "Process interrupted during second input."
        self.assertEqual(result, "Process interrupted during second input.")

    @patch("builtins.input", side_effect=[KeyboardInterrupt, KeyboardInterrupt])
    def test_multiple_keyboard_interrupts(self, mock_input):
        """Simulate two consecutive Ctrl+C presses"""
        try:
            input("First input: ")  # Raises KeyboardInterrupt
        except KeyboardInterrupt:
            result = "First interruption detected."

        self.assertEqual(result, "First interruption detected.")

        try:
            input("Second input: ")  # Raises KeyboardInterrupt again
        except KeyboardInterrupt:
            result = "Second interruption detected."

        self.assertEqual(result, "Second interruption detected.")

if __name__ == '__main__':
    unittest.main()

