from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

KEY = get_random_bytes(32)  # AES-256

def encrypt_file(filename):
    cipher = AES.new(KEY, AES.MODE_EAX)
    with open(filename, "rb") as f:
        data = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(filename + ".enc", "wb") as f:
        f.write(cipher.nonce + tag + ciphertext)

    print("[+] File Encrypted")

def decrypt_file(filename):
    with open(filename, "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    output = filename.replace(".enc", "")
    with open(output, "wb") as f:
        f.write(data)

    print("[+] File Decrypted")

if __name__ == "__main__":
    choice = input("Encrypt or Decrypt (e/d): ")
    file = input("Enter filename: ")

    if choice.lower() == "e":
        encrypt_file(file)
    else:
        decrypt_file(file)
