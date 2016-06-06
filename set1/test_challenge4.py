'''
Challenge 4:
Detect single-character XOR
'''

from set1.challenge4 import *
import unittest

class Challenge4TestCase(unittest.TestCase):

    def test_detect_single_xor(self):
        with open('../data/data_4.txt') as f:
            strings = f.readlines()
        ciphertexts = [str.rstrip('\n').decode('hex') for str in strings]
        plaintexts = detect_single_xor(ciphertexts)

        target = 'Now that the party is jumping\n'
        i = 0
        for plaintext, score in plaintexts:
            if plaintext == target:
                print "Found at rank %d with score of %f" % (i, score)
                break
            i += 1

        self.assertLess(i, len(plaintexts))

if __name__ == '__main__':
    unittest.main()
