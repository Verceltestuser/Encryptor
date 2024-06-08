# File Encryption and Decryption

This project contains two Python scripts for encrypting and decrypting files using AES-256 encryption. The encryption key is generated randomly and ends with a specific string. The key is also Base64-encoded for easy handling.

## Files

1. `main.py`: Script to encrypt a file.
2. `decryptor.py`: Script to decrypt an encrypted file.

## Requirements

- Python 3.x
- `pycryptodome` library
- `ctypes` library (built-in with Python)

## Installation

Install the `pycryptodome` library if you haven't already:

```bash
pip install pycryptodome
```
## Usage

### Encryptor

The `encryptor.py` script encrypts a specified file and performs the following actions:

- Encrypts the file content using AES-256 in CBC mode.
- Base64-encodes the encrypted content.
- Deletes the original file.
- Saves the encrypted content to a new file with the `.locked_by_RANSOM_Y` extension.
- Creates a notification file named `HOW_TO_RECOVER_YOUR_FILES.txt` with instructions.
- Changes the desktop background to a specified image.
- Displays the Base64-encoded encryption key.

#### Running the Encryptor

```bash
python encryptor.py
```

Follow the prompt to enter the file name to encrypt. The script will generate a random encryption key and contact.


## Decryptor

The `decryptor.py` script decrypts a file that was encrypted by the `encryptor.py` script using the provided Base64-encoded encryption key.

#### Running the Decryptor

```bash
python decryptor.py
```

This will decrypt the encrypted files

## Example

### Encrypt a File

1. Run `encryptor.py`:
    ```bash
    python encryptor.py
    ```
2. Enter the file name to encrypt (e.g., `example.txt`).
3. Note the Base64-encoded encryption key displayed by the script.

### Decrypt the File

1. Run `decryptor.py`:
    ```bash
    python decryptor.py
    ```
2. Enter the encrypted file name (e.g., `example.txt.locked_by_RANSOM_Y`).
3. Enter the Base64-encoded encryption key provided by the encryptor script.
4. The decrypted file will be saved with its original name (e.g., `example.txt`).

## Note

- Ensure `wallpaper.jpg` is present in the same directory as `encryptor.py` for the desktop background change to work.
- The `encryptor.py` script deletes the original file after encryption, so make sure to keep a backup if needed.

## License

This project is licensed under the Apache License 2.0.
