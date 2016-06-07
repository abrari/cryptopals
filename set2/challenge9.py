'''
Challenge 9:
Implement PKCS#7 padding
'''

def pkcs7_pad(str, blocksize):
    pad = blocksize - (len(str) % blocksize)
    return str + (chr(pad) * pad)
