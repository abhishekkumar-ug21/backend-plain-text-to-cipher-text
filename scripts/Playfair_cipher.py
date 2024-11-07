# P to p
import os
import sys
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

# Access the CIPHER_KEY variable
keyword = os.getenv("CIPHER_KEY", "KEYWORD").upper()

# Function to create a 5x5 matrix for Playfair Cipher
def create_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J are treated as the same
    key = "".join(sorted(set(key.replace("J", "I")), key=key.index))  # Remove duplicates, replace J with I
    matrix_string = key + "".join([char for char in alphabet if char not in key])
    matrix = [list(matrix_string[i:i + 5]) for i in range(0, 25, 5)]
    # print("Playfair Matrix:")
    # for row in matrix:
    #     print(row)
    return matrix

# Function to format the plaintext for encryption
def format_plaintext(plaintext):
    formatted = plaintext.replace("J", "I").upper().replace(" ", "")
    i = 0
    while i < len(formatted):
        if i + 1 < len(formatted) and formatted[i] == formatted[i + 1]:
            formatted = formatted[:i + 1] + 'X' + formatted[i + 1:]
        i += 2
    return formatted if len(formatted) % 2 == 0 else formatted + 'X'

# Function to find the position of a character in the matrix
def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    print(f"Warning: '{char}' is not in the matrix. Replacing with 'X'.")
    return find_position('X', matrix)  # Replace with 'X' if missing

# Function to encrypt the plaintext using Playfair Cipher
def encrypt(plaintext):
    matrix = create_matrix(keyword)
    formatted_text = format_plaintext(plaintext)
    cipher_text = ""

    for i in range(0, len(formatted_text), 2):
        first, second = formatted_text[i], formatted_text[i + 1]
        first_row, first_col = find_position(first, matrix)
        second_row, second_col = find_position(second, matrix)

        if first_row == second_row:  # Same row
            cipher_text += matrix[first_row][(first_col + 1) % 5]
            cipher_text += matrix[second_row][(second_col + 1) % 5]
        elif first_col == second_col:  # Same column
            cipher_text += matrix[(first_row + 1) % 5][first_col]
            cipher_text += matrix[(second_row + 1) % 5][second_col]
        else:  # Rectangle
            cipher_text += matrix[first_row][second_col]
            cipher_text += matrix[second_row][first_col]

    return cipher_text

# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        plaintext = sys.argv[1]
    else:
        plaintext = input("Enter plaintext to encrypt: ")
    try:
        cipher_text = encrypt(plaintext)
        # print("Cipher text:", cipher_text)
        print(cipher_text)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
