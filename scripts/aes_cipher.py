import sys

def encrypt_aes(text):
    # Implement AES encryption logic here
    return f"AES({text})"

if __name__ == "__main__":
    plain_text = sys.argv[1]
    cipher_text = encrypt_aes(plain_text)
    print(cipher_text)
