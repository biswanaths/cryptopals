# https://cryptopals.com/sets/1/challenges/1
import sys
import base64

key_in_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

key_in_hex = sys.argv[1] if len(sys.argv) > 1 else key_in_hex
key_in_bytes = bytes.fromhex(key_in_hex)
key_in_base64 = base64.b64encode(key_in_bytes)

print(key_in_base64)
