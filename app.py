
import streamlit as st
import streamlit_authenticator as stauth
from gsheet import get_users
from idp_module import run_idp_module

st.set_page_config(page_title="AUFC IDP Tracker", layout="wide")

# Obtener usuarios desde Google Sheet
users_df = get_users()

# Crear credenciales directamente sin hasheo
credentials = {
    "usernames": {
        row["username"]: {
            "name": row["name"],
            "password": str(row["password"]),
            "role": row["role"],
        }
        for _, row in users_df.iterrows()
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "idp_app",
    "abcdef",
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("Username/password is incorrect")

if authentication_status is None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.write(f"Welcome {name}!")

    st.title("📋 Individual Development Plans")

    # Módulo principal de IDPs
    run_idp_module(username)
