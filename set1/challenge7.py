'''
Challenge 7:
AES in ECB mode
'''

from Crypto.Cipher import AES

def aes_ecb_decrypt(ciphertext, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(ciphertext)


