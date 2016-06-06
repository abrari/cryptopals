'''
Challenge 3:
Detect single-character XOR
'''

from set1.challenge3 import break_single_xor, score_english

def detect_single_xor(strings):
    plaintexts = {}
    for str in strings:
        decs = break_single_xor(str, alternatives=1)
        for dec in decs:
            plain = dec['plaintext']
            score = score_english(plain)
            plaintexts[plain] = score

    plaintexts_sorted = sorted(plaintexts.items(), key=lambda x: x[1])
    return plaintexts_sorted

