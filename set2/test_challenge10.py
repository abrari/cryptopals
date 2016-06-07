'''
Challenge 10
Implement CBC mode
'''

from set2.challenge9  import pkcs7_pad
from set2.challenge10 import aes_cbc_encrypt, aes_cbc_decrypt
import unittest

class Challenge10TestCase(unittest.TestCase):

    def test_aes_cbc(self):
        key = "YELLOW SUBMARINE"
        iv  = '\x00' * 16
        s = "The quick brown fox jumps over the lazy dog"

        c = aes_cbc_encrypt(s, key, iv)
        p = aes_cbc_decrypt(c, key, iv)

        self.assertEquals(p, pkcs7_pad(s, 16))

    def test_challenge10(self):
        from base64 import b64decode
        ciphertext = b64decode(file('data/data_10.txt').read().replace('\n', ''))
        key = "YELLOW SUBMARINE"
        iv  = '\x00' * 16

        plaintext = aes_cbc_decrypt(ciphertext, key, iv)

        self.assertIn("Supercalafragilisticexpialidocious", plaintext)


if __name__ == '__main__':
    unittest.main()