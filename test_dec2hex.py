import unittest
from Dec2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(0), "0")

    def test_non_integer_input(self):
        self.assertEqual(decimal_to_hex("abc"), "Error: Invalid input. Please enter a valid integer.")
        self.assertEqual(decimal_to_hex("12.3"), "Error: Invalid input. Please enter a valid integer.")

    def test_no_input(self):
        with self.assertRaises(TypeError):
            decimal_to_hex()

if __name__ == "__main__":
    unittest.main()
