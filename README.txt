# AUFC IDP Streamlit App

This app allows coaches to:
- Log in securely (using usernames from the Google Sheet)
- View player information
- Submit and track Individual Development Plans (IDPs)

## 🔗 Connected to
- Google Sheet: `AUFC_Streamlit`
  - Tabs: `users`, `Players`, `IDP`

## 🛠 Setup (Streamlit Cloud)
1. Upload all `.py` files to a private GitHub repo
2. Go to https://streamlit.io/cloud and deploy the app
3. Add `GOOGLE_CREDS` as a secret in Settings > Secrets (paste your credentials.json content)
4. Share the Google Sheet with your service account (as editor)

## 📄 Dependencies
See `requirements.txt`
