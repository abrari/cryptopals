'''
Challenge 6
Break repeating-key XOR
'''

def hamming_weight(num):
    ''' Calculate number of set bit '''
    return bin(num).count('1')

def hamming_distance(str1, str2):
    ''' Calculate number of differing bits '''
    count = 0
    len_diff = abs(len(str1) - len(str2))
    for i in range(min(len(str1), len(str2))):
        count += hamming_weight(ord(str1[i]) ^ ord(str2[i]))

    count += (len_diff * 8)
    return count

class RepeatingXORBreaker:

    def __init__(self, c):
        self.ciphertext = c

    def guess_keylength(self, max):
        distances = {}
        for i in range(2, max+1):
            # more blocks = more accuracy
            block1 = self.ciphertext[i*0:i*1]
            block2 = self.ciphertext[i*1:i*2]
            block3 = self.ciphertext[i*2:i*3]
            block4 = self.ciphertext[i*3:i*4]
            d12 = hamming_distance(block1, block2) / float(i)
            d13 = hamming_distance(block1, block3) / float(i)
            d14 = hamming_distance(block1, block4) / float(i)
            d23 = hamming_distance(block2, block3) / float(i)
            d24 = hamming_distance(block2, block4) / float(i)
            d34 = hamming_distance(block3, block4) / float(i)
            distances[i] = (d12 + d13 + d14 + d23 + d24 + d34) / 6.0

        distances_sorted = sorted(distances.items(), key=lambda x: x[1])
        probable_keylengths = [x[0] for x in distances_sorted]

        return probable_keylengths

    def try_break(self, keylength):
        # break cipher into blocks of keylength size
        blocks = []
        for i in range(0, len(self.ciphertext) - keylength, keylength):
            blocks.append(self.ciphertext[i:i+keylength])

        # take column from each blocks
        columns = [''] * keylength
        for i in range(keylength):
            for block in blocks:
                columns[i] += block[i]

        # freq analysis each column
        guessed_key = ''
        from set1.challenge3 import break_single_xor
        for column in columns:
            dec = break_single_xor(column, alternatives=1)
            key = dec[0]['key']
            #print dec[0]['plaintext']
            guessed_key += chr(key)

        # try decrypt (= encrypt) using the guessed key
        from set1.challenge5 import encrypt_repeated_xor
        plaintext = encrypt_repeated_xor(self.ciphertext, guessed_key)

        return guessed_key, plaintext