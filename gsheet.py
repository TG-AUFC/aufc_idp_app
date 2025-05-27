import gspread
import pandas as pd
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Cargar credenciales desde los secrets
    creds_dict = json.loads(os.environ["GOOGLE_CREDS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    return sheet

def get_users():
    sheet = connect_sheet("AUFC_Streamlit")
    worksheet = sheet.worksheet("users")
    users_df = pd.DataFrame(worksheet.get_all_records())
    return users_df