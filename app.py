import streamlit as st
import streamlit_authenticator as stauth
from gsheet import get_users
from idp_module import run_idp_module

# Configuración de la página
st.set_page_config(page_title="AUFC IDP Tracker", layout="wide")

# Cargar usuarios desde la hoja de cálculo
users_df = get_users()

# Preparar diccionario de credenciales (sin hashing)
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

# Inicializar autenticador
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="idp_app",
    key="abcdef",
    cookie_expiry_days=1
)

# Mostrar formulario de login
authenticator.login()

# Verificación de estado de sesión
if st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")

elif st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {st.session_state['name']}!")

    st.title("📋 Individual Development Plans")

    # Ejecutar el módulo principal
    run_idp_module(st.session_state["username"])
