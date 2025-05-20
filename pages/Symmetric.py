import streamlit as st
import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# ---------- Fernet Functions ----------
def encrypt_fernet(message: str, key_input: str = ""):
    if not key_input:
        key = Fernet.generate_key()
        generated = True
    else:
        key = key_input.encode()
        generated = False
    f = Fernet(key)
    token = f.encrypt(message.encode())
    return token.decode(), key.decode(), generated

def decrypt_fernet(token: str, key_input: str):
    try:
        f = Fernet(key_input.encode())
        message = f.decrypt(token.encode())
        return message.decode()
    except (InvalidToken, Exception) as e:
        return f"Decryption failed: {e}"

# ---------- AES (CBC) Functions ----------
def pkcs7_pad(data: bytes, block_size: int = 128):
    padder = padding.PKCS7(block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def pkcs7_unpad(padded_data: bytes, block_size: int = 128):
    unpadder = padding.PKCS7(block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def derive_key(password: str, salt: bytes, length: int = 32):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode())

def encrypt_aes(message: str, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padded_msg = pkcs7_pad(message.encode(), 128)
    ct = encryptor.update(padded_msg) + encryptor.finalize()
    # Concatenate salt, iv, ciphertext and encode in base64
    encrypted = base64.b64encode(salt + iv + ct).decode()
    return encrypted

def decrypt_aes(token: str, password: str):
    try:
        data = base64.b64decode(token)
        salt = data[:16]
        iv = data[16:32]
        ct = data[32:]
        key = derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_msg = decryptor.update(ct) + decryptor.finalize()
        message = pkcs7_unpad(padded_msg, 128)
        return message.decode()
    except Exception as e:
        return f"Decryption failed: {e}"

# ---------- ChaCha20 Functions ----------
def encrypt_chacha20(message: str, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt, length=32)
    nonce = os.urandom(16)  # ChaCha20 expects a 16-byte nonce
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    encryptor = cipher.encryptor()
    ct = encryptor.update(message.encode())
    # Concatenate salt, nonce, ciphertext and encode in base64
    encrypted = base64.b64encode(salt + nonce + ct).decode()
    return encrypted

def decrypt_chacha20(token: str, password: str):
    try:
        data = base64.b64decode(token)
        salt = data[:16]
        nonce = data[16:32]
        ct = data[32:]
        key = derive_key(password, salt, length=32)
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
        decryptor = cipher.decryptor()
        message = decryptor.update(ct)
        return message.decode()
    except Exception as e:
        return f"Decryption failed: {e}"

# ---------- Streamlit Sidebar Inputs and Main App ----------
st.title("Symmetric Encryption/Decryption")

# Sidebar Inputs
with st.sidebar:
    st.header("Inputs")
    operation = st.selectbox("Operation", ["Encrypt", "Decrypt"])
    algorithm = st.selectbox("Algorithm", ["Fernet", "AES (CBC)", "ChaCha20"])
    text_input = st.text_area("Text")
    key_input = ""
    password = ""
    if algorithm == "Fernet":
        key_input = st.text_input("Fernet Key (leave empty to generate new key)")        
    else:
        password = st.text_input("Password", type="password")
    execute = st.button("Execute")

if execute:
    if not text_input:
        st.error("Please enter text.")
    else:
        if operation == "Encrypt":
            if algorithm == "Fernet":
                token, used_key, generated = encrypt_fernet(text_input, key_input if key_input else "")
                st.subheader("Encrypted Token")
                st.code(token)
                if generated:
                    st.info(f"Generated Key: {used_key}")
            elif algorithm == "AES (CBC)":
                if not password:
                    st.error("Password required for AES encryption.")
                else:
                    encrypted = encrypt_aes(text_input, password)
                    st.subheader("Encrypted Data (Base64 Encoded)")
                    st.code(encrypted)
            elif algorithm == "ChaCha20":
                if not password:
                    st.error("Password required for ChaCha20 encryption.")
                else:
                    encrypted = encrypt_chacha20(text_input, password)
                    st.subheader("Encrypted Data (Base64 Encoded)")
                    st.code(encrypted)
        elif operation == "Decrypt":
            if algorithm == "Fernet":
                if not key_input:
                    st.error("Fernet key required for decryption.")
                else:
                    decrypted = decrypt_fernet(text_input, key_input)
                    st.subheader("Decrypted Message")
                    st.code(decrypted)
            elif algorithm == "AES (CBC)":
                if not password:
                    st.error("Password required for AES decryption.")
                else:
                    decrypted = decrypt_aes(text_input, password)
                    st.subheader("Decrypted Message")
                    st.code(decrypted)
            elif algorithm == "ChaCha20":
                if not password:
                    st.error("Password required for ChaCha20 decryption.")
                else:
                    decrypted = decrypt_chacha20(text_input, password)
                    st.subheader("Decrypted Message")
                    st.code(decrypted)