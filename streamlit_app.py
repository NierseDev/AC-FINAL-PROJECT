import streamlit as st

st.title("Applied Cryptography | FP | Group 1")

st.markdown(
    "By: Hamzah Ibarreta Cuadra,\n"
    "Harold Salvador,\n"
    "Jude Fajardo"
)

st.sidebar.markdown("<h2 style='color:#4CAF50;'>🔐 Encryption Mode</h2>", unsafe_allow_html=True)
menu_option = st.sidebar.radio("", ["Symmetric", "Asymmetric", "Hashing"])

if menu_option == "Symmetric":
    st.subheader("Symmetric Encryption")
elif menu_option == "Asymmetric":
    st.subheader("Asymmetric Encryption")
elif menu_option == "Hashing":
    st.subheader("Hashing")