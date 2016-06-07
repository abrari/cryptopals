'''
Challenge 6
Break repeating-key XOR
'''

from set1.challenge6 import *
import unittest

class Challenge6TestCase(unittest.TestCase):

    def test_hamming_distance(self):
        d = hamming_distance("this is a test", "wokka wokka!!!")
        self.assertEquals(d, 37)

    def test_rep_xor_break(self):
        from base64 import b64decode
        ciphertext = b64decode(file('data/data_6.txt').read().replace('\n', ''))

        breaker = RepeatingXORBreaker(ciphertext)
        keylen = breaker.guess_keylength(max=40)
        keys = []

        for i in range(3):
            print "========== GUESS %d: KEYLEN = %d ==========" % (i, keylen[i])
            key, plaintext = breaker.try_break(keylen[i])
            keys.append(key)
            print "GUESSED KEY = '" + key + "'\n"
            # print plaintext

        self.assertIn('Terminator X: Bring the noise', keys)

if __name__ == '__main__':
    unittest.main()