import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font as tkfont
from controller.playfair_cipher import Playfair
from controller.vigenere_cipher import Vigenere
from controller.hill_cipher import Hill

def show_error(message):
    messagebox.showerror("Kesalahan Input", message)

def encrypt():
    plaintext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    if len(key) < 12:
        show_error("Kunci harus minimal 12 karakter")
        return
    if cipher_var.get() == "Vigenere":
        ciphertext = Vigenere.vigenere_cipher(plaintext, key)
    elif cipher_var.get() == "Playfair":
        ciphertext = Playfair.playfair_cipher(plaintext, key)
    elif cipher_var.get() == "Hill":
        ciphertext = Hill.hill_cipher(plaintext, key)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, ciphertext)

def decrypt():
    ciphertext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    if len(key) < 12 and cipher_var.get() != "Hill":
        show_error("Kunci harus minimal 12 karakter")
        return
    if cipher_var.get() == "Vigenere":
        plaintext = Vigenere.vigenere_decipher(ciphertext, key)
    elif cipher_var.get() == "Playfair":
        plaintext = Playfair.playfair_decipher(ciphertext, key)
    elif cipher_var.get() == "Hill":
        plaintext = Hill.hill_decipher(ciphertext, key)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, plaintext)

def upload_file():
    file_path = filedialog.askopenfilename(title="Pilih file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, file.read())

def on_exit():
    if messagebox.askokcancel("Keluar", "Anda yakin ingin keluar?"):
        root.destroy()

root = tk.Tk()
root.title("Kriptografi: Vigenere, Playfair, dan Hill Cipher")
root.geometry("1200x800")
root.config(bg="#ffffff")  

header_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
label_font = tkfont.Font(family="Helvetica", size=12)

header_label = tk.Label(root, text="Kriptografi: Vigenere, Playfair, dan Hill Cipher", font=header_font, bg="#ffffff", fg="#333")
header_label.pack(pady=10)

cipher_label = tk.Label(root, text="Pilih Cipher:", font=label_font, bg="#f2f2f2", fg="#333")
cipher_label.pack(pady=(10, 0))

cipher_var = tk.StringVar()
cipher_var.set("Vigenere")
cipher_option = tk.OptionMenu(root, cipher_var, "Vigenere", "Playfair", "Hill")
cipher_option.config(width=20, font=label_font)
cipher_option.pack(pady=5)

input_label = tk.Label(root, text="Masukkan Teks (Plaintext/Ciphertext):", font=label_font, bg="#f2f2f2", fg="#333")
input_label.pack(pady=(10, 0))

input_text = tk.Text(root, height=6, width=50, font=("Helvetica", 10), wrap="word")
input_text.pack(pady=5)

key_label = tk.Label(root, text="Masukkan Kunci (Minimal 12 karakter):", font=label_font, bg="#f2f2f2", fg="#333")
key_label.pack(pady=(10, 0))

key_entry = tk.Entry(root, width=50, font=("Helvetica", 10))
key_entry.pack(pady=5)

upload_button = tk.Button(root, text="Upload File", command=upload_file, font=label_font, bg="#4CAF50", fg="white")
upload_button.pack(pady=5)

encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt, font=label_font, bg="#2196F3", fg="white", width=15)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Dekripsi", command=decrypt, font=label_font, bg="#FF5722", fg="white", width=15)
decrypt_button.pack(pady=5)

result_label = tk.Label(root, text="Hasil (Ciphertext/Plaintext):", font=label_font, bg="#f2f2f2", fg="#333")
result_label.pack(pady=(10, 0))

result_text = tk.Text(root, height=6, width=50, font=("Helvetica", 10), wrap="word")
result_text.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()
