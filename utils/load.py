import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Fungsi untuk menyimpan DataFrame ke CSV
def load_to_csv(df, filename="products.csv"):
    try:
        # Menyimpan DataFrame ke file CSV
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")  # Menampilkan pesan sukses
    except Exception as e:
        print("Failed to save CSV:", e)  # Menangani error jika terjadi kegagalan dalam menyimpan CSV

# Fungsi untuk memuat DataFrame ke Google Sheets
def load_to_gsheet(df, spreadsheet_name):
    """
    Fungsi untuk memuat DataFrame ke Google Sheets.
    
    Parameters:
    - df: DataFrame yang akan dimuat
    - spreadsheet_name: Nama spreadsheet yang akan dibuat di Google Sheets
    """
    try:
        # Tentukan scope dan kredensial untuk akses Google Sheets API
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("google-sheets-api.json", scope)  # Menggunakan file kredensial
        client = gspread.authorize(creds)  # Mengotorisasi klien untuk mengakses Google Sheets

        # Buat spreadsheet baru dengan nama yang diberikan
        sheet = client.create(spreadsheet_name)

        # Share spreadsheet ke publik (editable)
        sheet.share('', perm_type='anyone', role='writer')

        # (Opsional) Share ke email pribadi kamu supaya spreadsheet muncul di Google Drive kamu
        sheet.share('trisyanurmayanti07@gmail.com', perm_type='user', role='writer')

        # Ambil worksheet pertama (atau buat worksheet baru jika tidak ada)
        worksheet = sheet.get_worksheet(0) or sheet.sheet1

        # Tulis data dari DataFrame ke Google Sheets
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

        # Print link ke spreadsheet yang telah dibuat
        print("Spreadsheet URL: https://docs.google.com/spreadsheets/d/" + sheet.id)
    except Exception as e:
        print("Error loading data to Google Sheets:", e)  # Menangani error yang mungkin terjadi saat mengakses Google Sheets

