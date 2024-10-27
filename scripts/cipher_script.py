# # scripts/cipher_script.py
# import sys

# def generate_cipher(text):
#     # Simple Caesar Cipher with a shift of 3
#     shift = 3
#     cipher_text = "".join(
#         chr((ord(char) + shift - 65) % 26 + 65) if char.isupper() else
#         chr((ord(char) + shift - 97) % 26 + 97) if char.islower() else char
#         for char in text
#     )
#     return cipher_text

# if __name__ == "__main__":
#     plain_text = sys.argv[1]
#     print(generate_cipher(plain_text))

import sys

def generate_cipher(text):
    shift = 3
    cipher_text = ""

    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            cipher_text += new_char
        elif char.islower():
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            cipher_text += new_char
        else:
            cipher_text += char

    return cipher_text

if __name__ == "__main__":
    if len(sys.argv) > 1:
        plain_text = sys.argv[1]
        print(generate_cipher(plain_text))
    else:
        print("Please provide a string to encrypt.")
