import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from gsheet import get_users
from idp_module import render

# Cargar usuarios desde Google Sheet
users_df = get_users()
usernames = users_df['username'].tolist()
names = users_df['name'].tolist()
passwords = users_df['password'].astype(str).fillna("").tolist()

# Sanitize password column
passwords = users_df["password"].fillna("").astype(str).tolist()

try:
    hashed_passwords = stauth.Hasher(passwords).generate()
except Exception as e:
    st.error("Error processing passwords. Check that all passwords are valid strings.")
    st.stop()

credentials = {
    "usernames": {
        usernames[i]: {
            "name": names[i],
            "password": hashed_passwords[i]
        } for i in range(len(usernames))
    }
}

authenticator = stauth.Authenticate(
    credentials, "idp_app", "abcdef", cookie_expiry_days=30
)

name, auth_status, username = authenticator.login("Login", "main")

if auth_status:
    st.sidebar.success(f"Bienvenido {name}")
    render()
elif auth_status is False:
    st.error("Usuario o contraseña incorrectos")
elif auth_status is None:
    st.warning("Por favor ingresá tus credenciales")
