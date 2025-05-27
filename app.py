
import streamlit as st
import streamlit_authenticator as stauth
from gsheet import get_users
from idp_module import run_idp_module

st.set_page_config(page_title="AUFC IDP Tracker", layout="wide")

# Cargar usuarios desde Google Sheets
users_df = get_users()

# Crear diccionario de credenciales sin hashing (modo testing)
credentials = {
    "usernames": {
        row["username"]: {
            "name": row["name"],
            "password": str(row["password"]),
            "role": row["role"]
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

elif authentication_status is None:
    st.warning("Please enter your username and password")

elif authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name}!")

    st.title("📋 Individual Development Plans")

    run_idp_module(username)
