# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Access the CIPHER_KEY variable
# keyword = os.getenv("CIPHER_KEY")

# # Function to create a 5x5 matrix for Playfair Cipher
# def create_matrix(key):
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J are treated as the same
#     key = "".join(sorted(set(key), key=key.index))  # Remove duplicates, maintain order
#     matrix_string = key + "".join(filter(lambda x: x not in key, alphabet))
#     return [list(matrix_string[i:i + 5]) for i in range(0, 25, 5)]

# # Function to format the plaintext for encryption
# def format_plaintext(plaintext):
#     formatted = plaintext.replace("J", "I").upper().replace(" ", "")
#     i = 0
#     while i < len(formatted):
#         if i + 1 < len(formatted) and formatted[i] == formatted[i + 1]:
#             formatted = formatted[:i + 1] + 'X' + formatted[i + 1:]
#         i += 2
#     return formatted if len(formatted) % 2 == 0 else formatted + 'X'

# # Function to find the position of a character in the matrix
# def find_position(char, matrix):
#     for row_idx, row in enumerate(matrix):
#         if char in row:
#             return row_idx, row.index(char)
#     raise ValueError(f"{char} is not in the matrix")

# # Function to encrypt the plaintext using Playfair Cipher
# def encrypt(plaintext):
#     matrix = create_matrix(keyword)
#     formatted_text = format_plaintext(plaintext)
#     cipher_text = ""

#     for i in range(0, len(formatted_text), 2):
#         first = formatted_text[i]
#         second = formatted_text[i + 1]
#         first_row, first_col = find_position(first, matrix)
#         second_row, second_col = find_position(second, matrix)

#         if first_row == second_row:  # Same row
#             cipher_text += matrix[first_row][(first_col + 1) % 5]
#             cipher_text += matrix[second_row][(second_col + 1) % 5]
#         elif first_col == second_col:  # Same column
#             cipher_text += matrix[(first_row + 1) % 5][first_col]
#             cipher_text += matrix[(second_row + 1) % 5][second_col]
#         else:  # Rectangle
#             cipher_text += matrix[first_row][second_col]
#             cipher_text += matrix[second_row][first_col]

#     return cipher_text

# # Example usage
# if __name__ == "__main__":
#     plaintext = input("Enter plaintext to encrypt: ")
#     cipher_text = encrypt(plaintext)
#     print("Cipher text:", cipher_text)


# ##################################################################

# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Access the CIPHER_KEY variable
# keyword = os.getenv("CIPHER_KEY")

# # Function to create a 5x5 matrix for Playfair Cipher
# def create_matrix(key):
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J are treated as the same
#     key = "".join(sorted(set(key), key=key.index))  # Remove duplicates, maintain order
#     # Include 'X' to the matrix
#     if 'X' not in key:
#         key += 'X'
#     matrix_string = key + "".join(filter(lambda x: x not in key, alphabet))
#     return [matrix_string[i:i + 5] for i in range(0, 25, 5)]

# # Function to format the plaintext for encryption
# def format_plaintext(plaintext):
#     formatted = plaintext.replace("J", "I").upper().replace(" ", "")
#     i = 0
#     while i < len(formatted):
#         if i + 1 < len(formatted) and formatted[i] == formatted[i + 1]:
#             formatted = formatted[:i + 1] + 'X' + formatted[i + 1:]
#         i += 2
#     return formatted if len(formatted) % 2 == 0 else formatted + 'X'

# # Function to find the position of a character in the matrix
# def find_position(char, matrix):
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if matrix[row][col] == char:
#                 return row, col
#     raise ValueError(f"{char} is not in the matrix")

# # Function to encrypt the plaintext using Playfair Cipher
# def encrypt(plaintext):
#     matrix = create_matrix(keyword)
#     formatted_text = format_plaintext(plaintext)
#     cipher_text = ""

#     for i in range(0, len(formatted_text), 2):
#         first = formatted_text[i]
#         second = formatted_text[i + 1]
#         first_row, first_col = find_position(first, matrix)
#         second_row, second_col = find_position(second, matrix)

#         if first_row == second_row:  # Same row
#             cipher_text += matrix[first_row][(first_col + 1) % 5]
#             cipher_text += matrix[second_row][(second_col + 1) % 5]
#         elif first_col == second_col:  # Same column
#             cipher_text += matrix[(first_row + 1) % 5][first_col]
#             cipher_text += matrix[(second_row + 1) % 5][second_col]
#         else:  # Rectangle
#             cipher_text += matrix[first_row][second_col]
#             cipher_text += matrix[second_row][first_col]

#     return cipher_text

# # Example usage
# if __name__ == "__main__":
#     plaintext = input("Enter plaintext to encrypt: ")
#     cipher_text = encrypt(plaintext)
#     print("Cipher text:", cipher_text)



##################################################################


import sys
import string

# Define the Playfair cipher encryption function
def generate_playfair_square(keyword):
    alphabet = string.ascii_uppercase.replace("J", "")  # Playfair traditionally excludes "J"
    keyword = "".join(dict.fromkeys(keyword.upper()))  # Remove duplicate letters from keyword
    square = []
    for char in keyword + alphabet:
        if char not in square:
            square.append(char)
    return [square[i:i+5] for i in range(0, 25, 5)]

def format_plaintext(plaintext):
    formatted_text = ""
    plaintext = plaintext.upper().replace("J", "I")  # Replace "J" with "I"
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            formatted_text += plaintext[i] + 'X'
            i += 1
        else:
            formatted_text += plaintext[i:i+2]
            i += 2
    if len(formatted_text) % 2 != 0:
        formatted_text += 'X'
    return formatted_text

def find_position(square, char):
    for row in range(5):
        for col in range(5):
            if square[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, square):
    formatted_text = format_plaintext(plaintext)
    ciphertext = ""
    for i in range(0, len(formatted_text), 2):
        a, b = formatted_text[i], formatted_text[i+1]
        row_a, col_a = find_position(square, a)
        row_b, col_b = find_position(square, b)
        if row_a == row_b:
            ciphertext += square[row_a][(col_a + 1) % 5]
            ciphertext += square[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += square[(row_a + 1) % 5][col_a]
            ciphertext += square[(row_b + 1) % 5][col_b]
        else:
            ciphertext += square[row_a][col_b]
            ciphertext += square[row_b][col_a]
    return ciphertext

# Get the plainText and keyword from command-line arguments
if len(sys.argv) < 2:
    print("Error: Missing arguments. Usage: python Playfair_cipher.py <plainText>")
    sys.exit(1)

plainText = sys.argv[1]
keyword = "KEYWORD"  # You could use an environment variable for this if needed

# Generate Playfair square and encrypt the plainText
playfair_square = generate_playfair_square(keyword)
cipherText = playfair_encrypt(plainText, playfair_square)

# Output the cipher text
print(cipherText)
