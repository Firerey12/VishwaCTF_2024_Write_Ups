import numpy as np
import random
import sympy

# Opening encoded key
encrypted = open("../Files/encoded_key.txt", "r", encoding="utf-8").read()

# Setting up an array to store decoded characters
dec = []

# Setting up symbols for sympy
x = sympy.symbols('x')

# For each character in encrypted solve the equation for that characters ASCII code and append it to dec
for char in encrypted:
    dec_code = sympy.solveset(sympy.Eq(4*x**2+3*x+7, ord(char)), x).args[1] # args[1] since the positive answer is stored in index 1
    dec.append(chr(dec_code))

# Finally write the decoded key to file
decrypted = open("decoded_key.txt", "w").write(''.join(dec))