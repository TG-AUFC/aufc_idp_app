import gspread
import pandas as pd
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Leer las credenciales desde el SECRET cargado en Streamlit
    creds_dict = json.loads(os.environ["GOOGLE_CREDS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

    client = gspread.authorize(creds)

    # Asegurate de que este nombre sea exactamente igual al de tu archivo en Google Drive
    sheet = client.open("AUFC_Streamlit")
    return sheet

def get_users():
    sheet = connect_sheet()
    worksheet = sheet.worksheet("users")
    users_df = pd.DataFrame(worksheet.get_all_records())
    return users_df
