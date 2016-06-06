'''
Challenge 1:
Convert hex to base64
'''

def hex_to_base64(hexstr):
    from base64 import b64encode
    return b64encode(hexstr.decode('hex'))

