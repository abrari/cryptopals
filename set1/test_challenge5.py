'''
Challenge 5:
Implement repeating-key XOR
'''

from set1.challenge5 import encrypt_repeated_xor
import unittest

class Challenge5TestCase(unittest.TestCase):

    def test_encrypt_repeated_xor(self):
        input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        output = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f".decode('hex')
        key = 'ICE'

        ciphertext = encrypt_repeated_xor(input, key)

        self.assertEquals(ciphertext, output)

if __name__ == '__main__':
    unittest.main()