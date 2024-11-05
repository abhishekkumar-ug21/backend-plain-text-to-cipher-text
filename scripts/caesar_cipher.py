import sys

def encrypt_caesar(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if char.islower() else shift
            result += chr((ord(char) - 65 + shift_amount) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            result += char  # Non-alphabetical characters are unchanged
    return result

if __name__ == "__main__":
    plain_text = sys.argv[1]
    cipher_text = encrypt_caesar(plain_text)  # Default shift is 3
    print(cipher_text)
