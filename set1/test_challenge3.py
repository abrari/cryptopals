'''
Challenge 3:
Single-byte XOR cipher
'''

from set1.challenge3 import *
import unittest

class Challenge3TestCase(unittest.TestCase):

    text = "There is much more to it than you think. Consider the defaults to be static (=constant reference pointing to one object) and stored somewhere in the definition; evaluated at method definition time; as part of the class, not the instance. As they are constant, they cannot depend on self."

    def test_char_frequencies(self):
        freq = char_frequencies(self.text)
        #print freq
        self.assertTrue(True)

    def test_score_english(self):
        score = score_english(self.text)
        score2 = score_english("kyaxvakxvakyxakakakxayxyzxvayxkavxkayv")
        #print score, score2
        self.assertLess(score, score2)

    def test_xor_string(self):
        str = "hello world"
        xor = xor_string(str, 1)
        #print xor
        self.assertEquals(xor, "idmmn!vnsme")

    def test_break_single_xor(self):
        ciph = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')
        xors = break_single_xor(ciph, alternatives=5)
        #import pprint
        #pprint.pprint(xors)
        self.assertEquals(xors[0]['plaintext'], "Cooking MC's like a pound of bacon")

if __name__ == '__main__':
    unittest.main()
