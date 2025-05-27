
import streamlit as st
from gsheet import get_players, get_idp, add_idp_entry
from datetime import datetime

def run_idp_module(username):
    players_df = get_players()
    idp_df = get_idp()

    player_list = players_df["Player Name"].dropna().unique().tolist()
    selected_player = st.selectbox("Select a player", player_list)

    player_data = players_df[players_df["Player Name"] == selected_player].iloc[0]
    st.subheader("Player Info")
    st.write(player_data.to_frame())

    st.markdown("---")
    st.subheader("Add New Development Plan")

    with st.form("idp_form"):
        today = datetime.today().strftime("%Y-%m-%d")
        date = st.date_input("Date", value=datetime.today())
        dev_area = st.selectbox("Development Area", ["Tactical", "Technical", "Physical", "Mental", "Other"])
        component = st.text_input("Component")
        intervention = st.text_input("Intervention")
        responsibility = st.text_input("Responsibility", value=username)
        time_frame = st.text_input("Time Frame")
        success_measures = st.text_input("Success Measures")
        goals = st.text_area("Goals")
        reality = st.text_area("Reality")
        opportunity = st.text_area("Opportunity")
        submit = st.form_submit_button("Save Plan")

        if submit:
            new_row = [
                selected_player,
                date.strftime("%Y-%m-%d"),
                dev_area,
                component,
                intervention,
                responsibility,
                time_frame,
                success_measures,
                goals,
                reality,
                opportunity,
            ]
            add_idp_entry(new_row)
            st.success("Development plan saved successfully.")
