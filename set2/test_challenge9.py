'''
Challenge 9:
Implement PKCS#7 padding
'''

from set2.challenge9 import *
import unittest

class Challenge9TestCase(unittest.TestCase):

    def test_pkcs7_pad(self):
        s = "YELLOW SUBMARINE"
        p20 = pkcs7_pad(s, 20)
        p16 = pkcs7_pad(s, 16)

        self.assertEquals(p20, "YELLOW SUBMARINE\x04\x04\x04\x04")
        self.assertEquals(p16, "YELLOW SUBMARINE\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10")

if __name__ == '__main__':
    unittest.main()