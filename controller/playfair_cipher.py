import re

def prepare_text(text):
    text = text.upper().replace('J', 'I') 
    text = re.sub(r'[^A-Z]', '', text)   
    return text

def generate_key_matrix(key):
    key = prepare_text(key)
    matrix = []
    used_chars = set()

    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
    
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def split_pairs(text):
    text = prepare_text(text)
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

class Playfair:
    def playfair_cipher(plaintext, key):
        matrix = generate_key_matrix(key)
        pairs = split_pairs(plaintext)
        ciphertext = []

        for a, b in pairs:
            row1, col1 = find_position(matrix, a)
            row2, col2 = find_position(matrix, b)

            if row1 == row2:
                ciphertext.append(matrix[row1][(col1 + 1) % 5])
                ciphertext.append(matrix[row2][(col2 + 1) % 5])
            elif col1 == col2:
                ciphertext.append(matrix[(row1 + 1) % 5][col1])
                ciphertext.append(matrix[(row2 + 1) % 5][col2])
            else:
                ciphertext.append(matrix[row1][col2])
                ciphertext.append(matrix[row2][col1])

        return ''.join(ciphertext)

    def playfair_decipher(ciphertext, key):
        matrix = generate_key_matrix(key)
        pairs = split_pairs(ciphertext)
        plaintext = []

        for a, b in pairs:
            row1, col1 = find_position(matrix, a)
            row2, col2 = find_position(matrix, b)

            if row1 == row2:
                plaintext.append(matrix[row1][(col1 - 1) % 5])
                plaintext.append(matrix[row2][(col2 - 1) % 5])
            elif col1 == col2:
                plaintext.append(matrix[(row1 - 1) % 5][col1])
                plaintext.append(matrix[(row2 - 1) % 5][col2])
            else:
                plaintext.append(matrix[row1][col2])
                plaintext.append(matrix[row2][col1])

        return ''.join(plaintext)


