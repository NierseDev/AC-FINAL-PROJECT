import streamlit as st

st.title("CryptoGadget")
st.subheader("By: Hamzah Ibarreta Cuadra, Harold Salvador, Jude Fajardo")

st.sidebar.markdown("<h2 style='color:#4CAF50;'>🏠 Home</h2>", unsafe_allow_html=True)
if st.sidebar.button("Home"):
    menu_option = "Home"
else:
    st.sidebar.markdown("<h2 style='color:#4CAF50;'>🔐 Encryption Mode</h2>", unsafe_allow_html=True)
    menu_option = st.sidebar.radio("Select Mode", ["Symmetric", "Asymmetric", "Hashing"])

if menu_option == "Home":
    # Redirect to Home (index/main page)
    st.experimental_set_query_params(page="index")
    st.write("Redirecting to Home...")
    st.stop()

elif menu_option == "Symmetric":
    # Redirect to the Symmetric page (e.g., Symmetric.py)
    st.experimental_set_query_params(page="Symmetric")
    st.write("Redirecting to Symmetric...")
    st.stop()

elif menu_option == "Asymmetric":
    # Redirect to the Asymmetric page (e.g., Asymmetric.py)
    st.experimental_set_query_params(page="Asymmetric")
    st.write("Redirecting to Asymmetric...")
    st.stop()

elif menu_option == "Hashing":
    # Redirect to the Hashing page (e.g., Hashing.py)
    st.experimental_set_query_params(page="Hashing")
    st.write("Redirecting to Hashing...")
    st.stop()
