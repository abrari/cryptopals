'''
Challenge 3:
Single-byte XOR cipher
'''
from string import ascii_uppercase

def char_frequencies(str):
    count = {}
    freq = {}
    str = str.upper()
    for c in ascii_uppercase:
        count[c] = 0

    alphabet_count = 0
    for c in str:
        if c.isalpha():
            alphabet_count += 1
            count[c] += 1

    for c in count:
        if alphabet_count == 0:
            freq[c] = 99999999
        else:
            freq[c] = float(count[c]) / float(alphabet_count)

    return freq

def score_english(text):
    english_freq = {
        'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015,
        'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749,
        'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758,
        'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074
    }
    freq = char_frequencies(text)

    chisq = 0
    for c in ascii_uppercase:
        obs = freq[c]
        exp = english_freq[c]
        diff = obs - exp
        chisq += diff ** 2 / exp

    return chisq

def xor_string(str, key):
    res = ''
    for c in str:
        res += chr(ord(c) ^ key)
    return res

def break_single_xor(ciphertext, alternatives):
    scores = {}
    for key in range(256):
        xored = xor_string(ciphertext, key)
        score = score_english(xored)
        scores[key] = (score, xored)

    scores_sorted = sorted(scores.items(), key=lambda x: x[1][0])

    decrypted = []
    for i in range(alternatives):
        key = scores_sorted[i][0]
        plain = scores_sorted[i][1][1]
        decrypted.append({"key": key, "plaintext": plain})

    return decrypted
