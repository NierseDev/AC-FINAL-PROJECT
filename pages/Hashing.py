import streamlit as st
import hashlib

# Using the sidebar for text input
user_input = st.sidebar.text_input("Enter text to hash:")

if user_input:
    # MD5 hash
    md5_hash = hashlib.md5(user_input.encode()).hexdigest()
    # SHA-1 hash
    sha1_hash = hashlib.sha1(user_input.encode()).hexdigest()
    # SHA-256 hash
    sha256_hash = hashlib.sha256(user_input.encode()).hexdigest()
    
    st.subheader("Input Text")
    st.write(user_input)
    
    st.subheader("Hashes")
    st.write("**MD5:**", md5_hash)
    st.write("**SHA-1:**", sha1_hash)
    st.write("**SHA-256:**", sha256_hash)
else:
    st.info("Please enter text in the sidebar to see the hashes.")