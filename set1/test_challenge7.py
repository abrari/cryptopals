'''
Challenge 7:
AES in ECB mode
'''

from set1.challenge7 import *
import unittest

class Challenge7TestCase(unittest.TestCase):

    def test_aes_ecb_decrypt(self):
        from base64 import b64decode
        ciphertext = b64decode(file('data/data_7.txt').read().replace('\n', ''))
        key = "YELLOW SUBMARINE"
        plaintext = aes_ecb_decrypt(ciphertext, key)

        self.assertIn("Supercalafragilisticexpialidocious", plaintext)


if __name__ == '__main__':
    unittest.main()