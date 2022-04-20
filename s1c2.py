key_1 = '1c0111001f010100061a024b53535009181c'
key_1 = bytes.fromhex(key_1)

key_2 = '686974207468652062756c6c277320657965'
key_2 = bytes.fromhex(key_2)


key = bytes(a ^ b for (a,b) in zip(key_1, key_2))

print(key)
print(key.hex())

