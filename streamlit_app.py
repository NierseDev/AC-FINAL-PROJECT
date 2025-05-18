import streamlit as st

st.title("Applied Cryptography | FP | Group 1")

st.markdown(
    "By: Hamzah Ibarreta Cuadra,\n"
    "Harold Salvador,\n"
    "Jude Fajardo"
)
menu_option = st.sidebar.selectbox("Select Mode", ["Symmetric", "Asymmetric", "hashing"])
if menu_option == "Symmetric":
    st.subheader("Symmetric Encryption")
elif menu_option == "Asymmetric":
    st.subheader("Asymmetric Encryption")
elif menu_option == "hashing":
    st.subheader("Hashing")