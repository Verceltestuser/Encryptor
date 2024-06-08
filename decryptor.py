from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os
import secrets

def unpad(data):
    """Removes padding from the data."""
    return data.rstrip(b"\0")

def decrypt(file_name, key):
    """Decrypts the file content encoded with Base64 and AES-256."""
    with open(file_name, 'rb') as f:
        encrypted_data = base64.b64decode(f.read())
    iv = encrypted_data[:AES.block_size]
    encrypted_text = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text))
    return decrypted_text

def save_decrypted_file(file_name, data):
    """Saves the decrypted data to a new file with the original extension."""
    original_file_name = file_name.replace(".locked_by_RANSOM_Y", "")
    with open(original_file_name, 'wb') as f:
        f.write(data)

def create_notification_file():
    """Creates a notification text file to inform the user about the encryption."""
    with open("RECOVER_COMPLETED.txt", 'w') as f:
        f.write("!ATTENTION!\nYOUR FILES ARE DECRYPTED\nYOU ARE FREE TO UE\nTHIS WAS A GOOD CHOICE\n\nThank you for using our product")

def main():
    file_name = input("Enter the encrypted file name to decrypt: ")
    key = input("Your key:")
    decrypted_data = decrypt(file_name, key)
    save_decrypted_file(file_name, decrypted_data)

if __name__ == "__main__":
    main()
