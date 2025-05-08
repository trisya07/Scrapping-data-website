from utils.extract import extract_products

def test_extract_not_empty():
    # Cobalah untuk mengambil data dari halaman pertama
    data = extract_products(pages=1)
    
    # Memastikan data tidak kosong
    assert len(data) > 0, "Data yang diambil kosong, pastikan scraping berhasil"

    # Memastikan setiap produk memiliki informasi penting (seperti 'title' dan 'price')
    for product in data:
        assert "title" in product, f"Produk tidak memiliki title: {product}"
        assert "price" in product, f"Produk tidak memiliki price: {product}"

    # Cek tipe data untuk memastikan data yang diambil sesuai
    assert isinstance(data, list), "Data yang diambil bukan dalam bentuk list"
    assert isinstance(data[0], dict), "Setiap item dalam data harus berupa dictionary"
    
    # Opsional: memeriksa data pertama sebagai contoh
    first_product = data[0]
    assert "rating" in first_product, f"Produk pertama tidak memiliki rating: {first_product}"

