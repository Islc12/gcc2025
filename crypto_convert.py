#!/usr/bin/env python3

import base64
import unicodedata

# Function to decode Base64
def b64decrypt():
    input_data = input("Enter Base64 encoded data: ")
    try:
        decoded = base64.b64decode(input_data).decode('utf-8')
        print(f"\nDecoded Base64 Data: {decoded}")
        decoded_url = base64.urlsafe_b64decode(input_data).decode('utf-8')
        print(f"\nDecoded Base64_url data: {decoded_url}")
    except Exception as e:
        print(f"Error in Base64 decoding: {e}")

# Function to decode Base32
def b32decrypt():
    input_data = input("Enter Base32 encoded data: ")
    try:
        decoded = base64.b32decode(input_data).decode('utf-8')
        print(f"\nDecoded Base32 Data: {decoded}")
    except Exception as e:
        print(f"Error in Base32 decoding: {e}")

# Function to decode Base85
def b85decrypt():
    input_data = input("Enter Base85 encoded data: ")
    try:
        decoded = base64.b85decode(input_data).decode('utf-8')
        print(f"\nDecoded Base85 Data: {decoded}")
    except Exception as e:
        print(f"Error in Base85 decoding: {e}")

# Function to decode Base16
def b16decrypt():
    input_data = input("Enter Base16 encoded data: ")
    try:
        decoded = base64.b16decode(input_data).decode('utf-8')
        print(f"\nDecoded Base16 Data: {decoded}")
    except Exception as e:
        print(f"Error in Base16 decoding: {e}")

# Function to decrypt using a shift cipher (Caesar cipher)
def shift_decrypt():
    input_data = input("Enter encrypted text for Shift Cipher: ")
    try:
        print("Attempting all possible shifts (0 to 25):")
        for shift in range(26):
            decrypted_text = ''.join(
                [shift_character(char, shift) for char in input_data]
            )
            print(f"Shift {shift}: {decrypted_text}\n")
    except Exception as e:
        print(f"Error in shift cipher decryption: {e}")

# Helper function for shifting each character in the string
def shift_character(char, shift):
    if char.isalpha():
        base = 65 if char.isupper() else 97
        return chr((ord(char) - base + shift) % 26 + base)
    return char

def unicode():
    char_input = input("Enter character\n")
    print(unicodedata.name(char_input))

def hexcode():
    hex_data = input("Enter hex data \n")
    ascii_output = bytes.fromhex(hex_data).decode('ascii', errors='ignore')
    print(ascii_output)



# Menu for selecting decryption type
print("\nSelect an option to decode (enter '99' to exit):")
print("1. Decode Base64")
print("2. Decode Base32")
print("3. Decode Base85")
print("4. Decode Base16")
print("5. Shift Cipher Decryption")
print("6. Unicode")
print("7. Hexcode")
print("99. Exit")

while True:
    choice = input("Enter your choice: ")

    if choice == '1':
        b64decrypt()
    elif choice == '2':
        b32decrypt()
    elif choice == '3':
        b85decrypt()
    elif choice == '4':
        b16decrypt()
    elif choice == '5':
        shift_decrypt()
    elif choice == '6':
        unicode()
    elif choice == '7':
        hexcode()
    elif choice == '99':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please select again.")

