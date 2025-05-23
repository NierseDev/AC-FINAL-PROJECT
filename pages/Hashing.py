import streamlit as st
import hashlib

st.title("Hashing")

# Sidebar Inputs
with st.sidebar:
    st.title("Input:")    
    hash_type = st.selectbox("Select Hash", ["MD5", "SHA1", "SHA256"])
    user_input = st.text_input("Enter text to hash:")
    generate_hash = st.button("Generate Hash")
   
if generate_hash and user_input:
    if hash_type == "MD5":  
        hashed = hashlib.md5(user_input.encode()).hexdigest()
        hash_label = "**MD5:**"
    elif hash_type == "SHA1":
        hashed = hashlib.sha1(user_input.encode()).hexdigest()
        hash_label = "**SHA-1:**"
    elif hash_type == "SHA256":
        hashed = hashlib.sha256(user_input.encode()).hexdigest()
        hash_label = "**SHA-256:**"
    else:
        hashed = ""
        hash_label = f"Unknown hash type: {hash_type}"

    st.subheader("Input Text:")
    st.write(user_input)
    st.subheader("Hashed Text:") 
    st.write(hash_label, hashed)
elif not user_input:
    st.info("Please enter text in the sidebar to see the hashes.")

