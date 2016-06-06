'''
Challenge 2:
Fixed XOR
'''

def xor_char(char1, char2):
    return chr(ord(char1) ^ ord(char2))

def xor_hex_string(hexstr1, hexstr2):
    hex1 = hexstr1.decode('hex')
    hex2 = hexstr2.decode('hex')
    hex_result = ''

    n = len(hex1)
    assert n == len(hex2)

    for i in range(n):
        hex_result += xor_char(hex1[i], hex2[i])

    return hex_result.encode('hex')
