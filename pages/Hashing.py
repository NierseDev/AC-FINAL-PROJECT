import streamlit as st
import hashlib

st.title("Hashing")

# Sidebar Inputs
with st.sidebar:
    st.title("Input:")    
    hash_type = st.selectbox("Select Hash", ["MD5", "SHA1", "SHA256"])
    user_input = st.text_input("Enter text to hash:")

if user_input:
    if user_input == "MD5":  
        md5_hash = hashlib.md5(user_input.encode()).hexdigest()
        st.subheader("Input Text:")
        st.write(user_input)
        st.subheader("Hashed Text:") 
        st.write("**MD5:**", md5_hash)
    elif user_input == "SHA1":
        sha1_hash = hashlib.sha1(user_input.encode()).hexdigest()
        st.subheader("Input Text:")
        st.write(user_input)
        st.subheader("Hashed Text:") 
        st.write("**SHA-1:**", sha1_hash)
    elif user_input == "SHA256":
        sha256_hash = hashlib.sha256(user_input.encode()).hexdigest()
        st.subheader("Input Text:")
        st.write(user_input)
        st.subheader("Hashed Text:") 
        st.write("**SHA-256:**", sha256_hash)
else:
    st.info("Please enter text in the sidebar to see the hashes.")