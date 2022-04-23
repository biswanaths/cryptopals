# https://cryptopals.com/sets/1/challenges/3

from pprint import pprint 

key = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
key = bytes.fromhex(key)

def frequency(phrase):
    length = len(phrase)
    f = {}
    for c in phrase:
        f[c] = f.get(c,0) + 1
    for k,v in f.items():
        pass
        # print(k, v*100/length)
    return f


for k in range(0, 255):
    original = bytes((k^ki for ki in key))
    # print(original)
    # pprint(frequency(original))
    print(original.decode('utf-8'))


