import streamlit as st

st.title("CryptoGadget")
st.subheader("By: Hamzah Ibarreta Cuadra, Harold Salvador, Jude Fajardo")

st.sidebar.markdown("<h2 style='color:#4CAF50;'>🏠 Home</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='color:#4CAF50;'>🔐 Encryption Mode</h2>", unsafe_allow_html=True)
st.sidebar.page_links()  # This will automatically show all pages in the sidebar

st.write("Welcome to CryptoGadget! Use the sidebar to navigate between Symmetric, Asymmetric, and Hashing modes.")
