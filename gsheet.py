import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    return sheet

def get_users():
    sheet = connect_sheet("AUFC_Streamlit")
    worksheet = sheet.worksheet("users")
    users_df = pd.DataFrame(worksheet.get_all_records())
    return users_df
