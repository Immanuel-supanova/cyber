import secrets
from system.settings import PRIVATE_KEY_FILE, PUBLIC_KEY_FILE

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

with open(PRIVATE_KEY_FILE, "rb") as key_file:
    private_pem = key_file.read()
    private_key = serialization.load_pem_private_key(
        private_pem,
        password=None,  
        backend=default_backend()
    )

# Load public key from file
with open(PUBLIC_KEY_FILE, "rb") as key_file:
    public_pem = key_file.read()
    public_key = serialization.load_pem_public_key(
        public_pem,
        backend=default_backend()
    )

def generate_aes_key():
    key = secrets.token_bytes(32)
    return key

def encrypt_data(data: bytes, key):
    # Create an AES cipher with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Add padding if necessary
    if len(data) % 16 != 0:
        data += b'\x00' * (16 - len(data) % 16)
    
    # Encrypt the data
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return ciphertext

def decrypt_data(ciphertext: bytes, key):
    # Create an AES cipher with CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the data
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def remove_padding(data):
    # Find the index of the first non-padding byte
    index = len(data)
    for i in range(len(data) - 1, -1, -1):
        if data[i] != 0:
            index = i + 1
            break
    
    # Remove the padding
    unpadded_data = data[:index]
    return unpadded_data