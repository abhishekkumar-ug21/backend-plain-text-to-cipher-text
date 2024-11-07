import sys

def vigenere_encrypt(plain_text, key):
    cipher_text = []
    key = key.upper()
    plain_text = plain_text.upper()
    key_len = len(key)
    key_index = 0
    
    for char in plain_text:
        if char.isalpha():
            # Encrypt the character
            shift = ord(key[key_index]) - ord('A')
            cipher_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            cipher_text.append(cipher_char)
            key_index = (key_index + 1) % key_len
        else:
            # Non-alphabetical characters are added without change
            cipher_text.append(char)

    return ''.join(cipher_text)

if __name__ == "__main__":
    plain_text = sys.argv[1]
    key = sys.argv[2] if len(sys.argv) > 2 else 'ABHI'  # Use 'ABHI' as default if no key is provided
    print("key for encryption is:",key.upper())
    # Call the Vigenère cipher encryption function
    cipher_text = vigenere_encrypt(plain_text, key)
    
    print("\nCipher text:", cipher_text)
