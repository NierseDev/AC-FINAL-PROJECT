import os
import hashlib
import streamlit as st
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import dh, dsa
from cryptography.hazmat.backends import default_backend

st.title("Applied Cryptography | FP | Group 1")
st.subheader("By: Hamzah Ibarreta Cuadra, Harold Salvador, Jude Fajardo")

st.sidebar.markdown("<h2 style='color:#4CAF50;'>🔐 Encryption Mode</h2>", unsafe_allow_html=True)
menu_option = st.sidebar.radio("", ["Symmetric", "Asymmetric", "Hashing"])

if menu_option == "Symmetric":
    st.subheader("Symmetric Encryption")
    tabs = st.tabs(["AES", "RC4"])

    with tabs[0]:
        st.subheader("AES Encryption (CBC Mode)")
        key_input = st.text_input("Enter 32-byte key in hex (or leave blank to generate one):")
        plaintext = st.text_area("Enter plaintext to encrypt:")
        if st.button("Encrypt with AES"):
            try:
                if not key_input:
                    key = os.urandom(32)
                    st.info(f"Generated Key (hex): {key.hex()}")
                else:
                    key = bytes.fromhex(key_input)
                    if len(key) != 32:
                        st.error("Key must be 32 bytes (64 hex characters).")
                        raise ValueError("Invalid key length.")
                iv = os.urandom(16)
                cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
                encryptor = cipher.encryptor()
                padder = padding.PKCS7(128).padder()
                padded_data = padder.update(plaintext.encode()) + padder.finalize()
                ciphertext = encryptor.update(padded_data) + encryptor.finalize()
                st.success(f"Ciphertext (hex): {ciphertext.hex()}")
                if st.button("Decrypt with AES"):
                    decryptor = cipher.decryptor()
                    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
                    unpadder = padding.PKCS7(128).unpadder()
                    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
                    st.success(f"Decrypted text: {decrypted.decode()}")
            except Exception as e:
                st.error(f"AES error: {e}")

    with tabs[1]:
        st.subheader("RC4 Encryption")
        key_input_rc4 = st.text_input(
            "Enter key for RC4 (or leave blank to generate a 16-byte key):", key="rc4_key"
        )
        plaintext_rc4 = st.text_area("Enter plaintext to encrypt with RC4:", key="rc4_plaintext")
        if st.button("Encrypt with RC4"):
            try:
                if not key_input_rc4:
                    key_rc4 = os.urandom(16)
                    st.info(f"Generated RC4 Key (hex): {key_rc4.hex()}")
                else:
                    key_rc4 = key_input_rc4.encode()
                cipher_rc4 = Cipher(algorithms.ARC4(key_rc4), mode=None, backend=default_backend())
                encryptor_rc4 = cipher_rc4.encryptor()
                ciphertext_rc4 = encryptor_rc4.update(plaintext_rc4.encode())
                st.success(f"Ciphertext (hex): {ciphertext_rc4.hex()}")
                if st.button("Decrypt with RC4"):
                    cipher_rc4 = Cipher(algorithms.ARC4(key_rc4), mode=None, backend=default_backend())
                    decryptor_rc4 = cipher_rc4.encryptor()
                    decrypted_rc4 = decryptor_rc4.update(ciphertext_rc4)
                    st.success(f"Decrypted text: {decrypted_rc4.decode()}")
            except Exception as e:
                st.error(f"RC4 error: {e}")

elif menu_option == "Asymmetric":
    st.subheader("Asymmetric Encryption")
    tabs = st.tabs(["Diffie-Hellman", "DSS Signature"])

    with tabs[0]:
        st.subheader("Diffie-Hellman Key Exchange")
        if st.button("Generate DH Key Exchange"):
            try:
                parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
                private_key_a = parameters.generate_private_key()
                private_key_b = parameters.generate_private_key()
                public_key_a = private_key_a.public_key()
                public_key_b = private_key_b.public_key()
                shared_key_a = private_key_a.exchange(public_key_b)
                shared_key_b = private_key_b.exchange(public_key_a)
                st.success("Diffie-Hellman key exchange completed.")
                st.info(f"Shared Key A (hex): {shared_key_a.hex()}")
                st.info(f"Shared Key B (hex): {shared_key_b.hex()}")
                if shared_key_a == shared_key_b:
                    st.success("Shared keys match!")
                else:
                    st.error("Shared keys do not match!")
            except Exception as e:
                st.error(f"DH error: {e}")

    with tabs[1]:
        st.subheader("DSS Digital Signature")
        message = st.text_area("Enter message to sign:")
        if st.button("Generate DSA Keys and Sign"):
            try:
                private_key_dsa = dsa.generate_private_key(key_size=2048)
                public_key_dsa = private_key_dsa.public_key()
                signature = private_key_dsa.sign(message.encode(), hashes.SHA256())
                st.success(f"Signature (hex): {signature.hex()}")
                if st.button("Verify Signature"):
                    try:
                        public_key_dsa.verify(signature, message.encode(), hashes.SHA256())
                        st.success("Signature verified successfully!")
                    except Exception as ve:
                        st.error(f"Verification failed: {ve}")
            except Exception as e:
                st.error(f"DSS error: {e}")

elif menu_option == "Hashing":
    st.subheader("Hashing")
    tabs = st.tabs(["MD5", "SHA256", "SHA512"])
    text_to_hash = st.text_area("Enter text to hash:")
    if text_to_hash:
        with tabs[0]:
            if st.button("Compute MD5 Hash"):
                hasher = hashlib.md5()
                hasher.update(text_to_hash.encode())
                st.success(f"MD5 Hash: {hasher.hexdigest()}")
        with tabs[1]:
            if st.button("Compute SHA256 Hash"):
                hasher = hashlib.sha256()
                hasher.update(text_to_hash.encode())
                st.success(f"SHA256 Hash: {hasher.hexdigest()}")
        with tabs[2]:
            if st.button("Compute SHA512 Hash"):
                hasher = hashlib.sha512()
                hasher.update(text_to_hash.encode())
                st.success(f"SHA512 Hash: {hasher.hexdigest()}")
