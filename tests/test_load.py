import pandas as pd
from utils.load import load_to_csv

def test_load_csv(tmp_path):
    # Membuat DataFrame dengan data contoh
    df = pd.DataFrame({
        "title": ["T-shirt"],
        "price": [1600000],
        "rating": [4.5],
        "colors": [3],
        "size": ["M"],
        "gender": ["Men"],
        "timestamp": ["2024-01-01T00:00:00"]
    })

    # Tentukan nama file untuk CSV yang akan disimpan
    filename = tmp_path / "test_output.csv"
    
    # Panggil fungsi load_to_csv untuk menyimpan data
    load_to_csv(df, filename)
    
    # Memastikan file CSV berhasil dibuat
    assert filename.exists(), f"File {filename} tidak ditemukan!"
    
    # Memverifikasi isi file CSV untuk memastikan datanya benar
    df_loaded = pd.read_csv(filename)
    
    # Memastikan bahwa DataFrame yang dibaca memiliki data yang sama dengan DataFrame yang diuji
    pd.testing.assert_frame_equal(df, df_loaded), "Data dalam CSV tidak sesuai dengan DataFrame asli"
