import sys

def encrypt_rsa(text):
    # Implement RSA encryption logic here
    return f"RSA({text})"

if __name__ == "__main__":
    plain_text = sys.argv[1]
    cipher_text = encrypt_rsa(plain_text)
    print(cipher_text)
