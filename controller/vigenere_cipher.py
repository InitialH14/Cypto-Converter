def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

class Vigenere:
    def vigenere_decipher(ciphertext, key):
        decrypted_text = []
        key = generate_key(ciphertext.replace(" ", ""), key)  
        key_index = 0 
        for char in ciphertext:
            if char.isalpha():  
                if char.isupper():
                    decrypted_char = chr((ord(char) - ord(key[key_index]) + 26) % 26 + ord('A'))
                elif char.islower():
                    decrypted_char = chr((ord(char) - ord(key[key_index]) + 26) % 26 + ord('a'))
                decrypted_text.append(decrypted_char)
                key_index += 1  
            else:
                decrypted_text.append(char)  
        return "".join(decrypted_text)

    def vigenere_cipher(plaintext, key):
        encrypted_text = []
        key = generate_key(plaintext.replace(" ", ""), key)  
        key_index = 0  
        for char in plaintext.replace(" ", ""):
            if char.isalpha():  
                if char.isupper():
                    encrypted_char = chr((ord(char) + ord(key[key_index]) - 2 * ord('A')) % 26 + ord('A'))
                elif char.islower():
                    encrypted_char = chr((ord(char) + ord(key[key_index]) - 2 * ord('a')) % 26 + ord('a'))
                encrypted_text.append(encrypted_char)
                key_index += 1  
            else:
                encrypted_text.append(char)  
        return "".join(encrypted_text)
