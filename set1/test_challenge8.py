'''
Challenge 8:
Detect AES in ECB mode
'''

from set1.challenge8 import *
import unittest

class Challenge8TestCase(unittest.TestCase):

    def test_is_probably_aes_ecb(self):
        with open('data/data_8.txt') as f:
            strings = f.readlines()
        ciphertexts = [str.rstrip('\n').decode('hex') for str in strings]

        for i in range(len(ciphertexts)):
            if is_probably_aes_ecb(ciphertexts[i]):
                print "Probably AES ECB at ciphertext %d" % i
                break

        self.assertLess(i, len(ciphertexts) - 1)

if __name__ == '__main__':
    unittest.main()