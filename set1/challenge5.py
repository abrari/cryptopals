'''
Challenge 5:
Implement repeating-key XOR
'''

def encrypt_repeated_xor(plaintext, key):
    ciphertext = ''
    keylen = len(key)
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % keylen]))

    return ciphertext

