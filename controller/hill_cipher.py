import numpy as np
from tkinter import messagebox

def show_error(message):
    messagebox.showerror("Kesalahan Input", message)

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper()]

def numbers_to_text(numbers):
    return ''.join([chr(num + ord('A')) for num in numbers])

def pad_text(text, block_size=4):
    padding_length = (block_size - len(text) % block_size) % block_size
    return text + ('X' * padding_length)  

def create_key_matrix(key_text):
    key_text = key_text[:16]
    key_numbers = text_to_numbers(key_text)
    key_matrix = np.array(key_numbers).reshape(4, 4)
    return key_matrix

class Hill:
    def hill_cipher(plaintext, key_matrix):
        if not key_matrix[:16] == "SECRETKEY1234567":
            show_error("Key salah! Silahkan masukkan key yang benar")
            return
        plaintext = pad_text(plaintext.replace(" ", ""))
        key_matrix = create_key_matrix(key_matrix)
        plaintext_numbers = text_to_numbers(plaintext)
        plaintext_matrix = np.array(plaintext_numbers).reshape(-1, 4).T
        ciphertext_matrix = np.dot(key_matrix, plaintext_matrix) % 26
        ciphertext_numbers = ciphertext_matrix.T.flatten().astype(int)

        return numbers_to_text(ciphertext_numbers)

    def hill_decipher(ciphertext, key_matrix):
        key_matrix = create_key_matrix(key_matrix)
        ciphertext_numbers = text_to_numbers(ciphertext)
        ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, 4).T
        key_matrix_inv = np.linalg.inv(key_matrix)
        key_matrix_inv = np.round(key_matrix_inv * np.linalg.det(key_matrix)).astype(int) % 26
        det_inv = pow(int(np.round(np.linalg.det(key_matrix))) % 26, -1, 26)
        key_matrix_inv = (det_inv * key_matrix_inv) % 26
        decrypted_matrix = np.dot(key_matrix_inv, ciphertext_matrix) % 26
        decrypted_numbers = decrypted_matrix.T.flatten().astype(int)

        return numbers_to_text(decrypted_numbers)