#!/usr/bin/env python3

from random import seed, randint



hex_string = input("Enter given ciphered hex string: ")
ciphertext = [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

seeds = int(input("Enter the discovered random seed: "))
seed(seeds)  # Set the same seed as the encryption program
randoms = [randint(1, 100) for _ in range(len(ciphertext))]  # Generate the list

key = int(input("Enter the found key: ")) # Enter the cracked key used to generate the encrypted message
plaintext = "".join(chr(ciphertext[n] - randoms[n] - key) for n in range(len(ciphertext)))

print(plaintext) # prints the decoded message in plain

