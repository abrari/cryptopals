'''
Challenge 7:
Detect AES in ECB mode
'''

def has_repeat(str, blocksize):
    blocks = []
    for i in range(0, len(str) - blocksize, blocksize):
        blocks.append(str[i:i+blocksize])

    # check some repeats
    if len(set(blocks)) == len(blocks):
        return False
    else:
        return True

def is_probably_aes_ecb(ciphertext):
    return has_repeat(ciphertext, 16)