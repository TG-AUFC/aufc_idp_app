
import gspread
import pandas as pd
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(os.environ["GOOGLE_CREDS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("AUFC_Streamlit")
    return sheet

def get_users():
    sheet = connect_sheet()
    worksheet = sheet.worksheet("users")
    return pd.DataFrame(worksheet.get_all_records())

def get_players():
    sheet = connect_sheet()
    worksheet = sheet.worksheet("Players")
    return pd.DataFrame(worksheet.get_all_records())

def get_idp():
    sheet = connect_sheet()
    worksheet = sheet.worksheet("IDP")
    return pd.DataFrame(worksheet.get_all_records())

def add_idp_entry(entry):
    sheet = connect_sheet()
    worksheet = sheet.worksheet("IDP")
    worksheet.append_row(entry)
