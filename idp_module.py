import streamlit as st
import pandas as pd
from gsheet import connect_sheet
from datetime import date

def render():
    sheet = connect_sheet("AUFC_Streamlit")
    players_df = pd.DataFrame(sheet.worksheet("Players").get_all_records())
    idp_df = pd.DataFrame(sheet.worksheet("IDP").get_all_records())

    st.title("📋 Individual Development Plans")

    player_names = players_df["Full Name"].tolist()
    selected_player = st.selectbox("Seleccioná un jugador", player_names)

    st.subheader("🔍 Ficha del Jugador")
    st.write(players_df[players_df["Full Name"] == selected_player])

    st.subheader("📊 Planes anteriores")
    st.dataframe(idp_df[idp_df["Player Name"] == selected_player])

    st.subheader("➕ Nuevo Plan")
    with st.form("new_idp"):
        dev_area = st.text_input("Área de desarrollo")
        component = st.text_input("Componente")
        intervention = st.text_input("Intervención")
        responsibility = st.text_input("Responsabilidad")
        timeframe = st.text_input("Duración")
        success = st.text_input("Medidas de éxito")
        goals = st.text_input("Meta")
        reality = st.text_input("Realidad")
        opportunity = st.text_input("Oportunidad")
        fecha = st.date_input("Fecha", value=date.today())

        submitted = st.form_submit_button("Guardar")

        if submitted:
            new_row = [selected_player, str(fecha), dev_area, component, intervention,
                       responsibility, timeframe, success, goals, reality, opportunity]
            sheet.worksheet("IDP").append_row(new_row)
            st.success("✅ Plan guardado correctamente.")
