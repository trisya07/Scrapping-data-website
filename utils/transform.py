import pandas as pd

def transform_data(data):
    """
    Fungsi untuk membersihkan dan mentransformasi data produk yang di-scrape.
    
    Parameter:
    - data: List of dictionaries yang berisi data produk (hasil dari ekstraksi).
    
    Returns:
    - df: DataFrame yang telah dibersihkan dan ditransformasi.
    """
    
    # Mengubah data list menjadi DataFrame
    df = pd.DataFrame(data)

    # Clean and transform data
    # Menghapus simbol dolar dari harga dan mengkonversi harga ke IDR (dengan kurs 1 USD = 16,000 IDR)
    df["price"] = df["price"].str.replace("$", "").astype(float) * 16000

    # Membersihkan rating, menghapus karakter non-digit dan mengkonversinya menjadi float
    df["rating"] = df["rating"].str.replace(r"[^\d\.]", "", regex=True).astype(float)

    # Mengekstrak angka dari kolom 'colors' (misalnya warna yang tersedia) dan mengkonversinya ke integer
    df["colors"] = df["colors"].str.extract(r"(\d+)").astype(int)
    
    # Menghapus duplikat dari DataFrame
    df = df.drop_duplicates()
    # Menghapus baris yang memiliki nilai null
    df = df.dropna()
    # Menghapus produk dengan judul 'Unknown Product'
    df = df[df["title"] != "Unknown Product"]
    
    return df  # Mengembalikan DataFrame yang telah dibersihkan dan ditransformasi
