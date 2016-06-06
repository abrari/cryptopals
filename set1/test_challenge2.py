'''
Challenge 2:
Fixed XOR
'''

from set1.challenge2 import xor_hex_string
import unittest

class Challenge2TestCase(unittest.TestCase):

    def test_xor_hex_string(self):
        hstr1 = "1c0111001f010100061a024b53535009181c"
        hstr2 = "686974207468652062756c6c277320657965"
        hstr_result = "746865206b696420646f6e277420706c6179"

        self.assertEquals(xor_hex_string(hstr1, hstr2), hstr_result)

if __name__ == '__main__':
    unittest.main()
