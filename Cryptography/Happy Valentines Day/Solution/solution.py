from PIL import Image # Did not really need this
from itertools import cycle

# Function which performs XOR operation using key on every byte of file given to it
def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

# Loading Encrypted File
f = open("../Files/enc.txt", "rb").read()

# key is the first 8 bytes of any intact PNG
key = [137, 80, 78, 71, 13, 10, 26, 10]

# Saving decrypted bytes to a bytearray
dec = bytearray(xor(f,key))

# Writing to a new file the decrypted bytes.
open('recovered.png', 'wb').write(dec)