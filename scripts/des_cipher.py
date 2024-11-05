import sys

def encrypt_des(text):
    # Implement DES encryption logic here
    return f"DES({text})"

if __name__ == "__main__":
    plain_text = sys.argv[1]
    cipher_text = encrypt_des(plain_text)
    print(cipher_text)
