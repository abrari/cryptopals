'''
Challenge 10
Implement CBC mode
'''

from set2.challenge9 import pkcs7_pad
from set1.challenge7 import aes_ecb_encrypt, aes_ecb_decrypt

def xor_string(str1, str2):
    result = ''
    n = len(str1)
    assert n == len(str2)
    for i in range(n):
        result += chr(ord(str1[i]) ^ ord(str2[i]))
    return result

def aes_cbc_encrypt(plaintext, key, iv):
    padded = pkcs7_pad(plaintext, 16)
    plaintext_blocks = [padded[i:i+16] for i in range(0, len(padded), 16)]
    ciphertext = ''

    c = iv
    for p in plaintext_blocks:
        x = xor_string(p, c)
        e = aes_ecb_encrypt(x, key)
        ciphertext += e
        c = e

    return ciphertext

def aes_cbc_decrypt(ciphertext, key, iv):
    ciphertext_blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plaintext = ''

    p = iv
    for c in ciphertext_blocks:
        d = aes_ecb_decrypt(c, key)
        plaintext += xor_string(p, d)
        p = c

    return plaintext

