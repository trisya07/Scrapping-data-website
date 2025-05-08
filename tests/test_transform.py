from utils.transform import transform_data

def test_price_conversion():
    # Data input dengan harga dalam format string (dengan tanda '$')
    data = [{
        "title": "T-shirt",
        "price": "$100.00",
        "rating": "4.5 / 5",
        "colors": "3 Colors",
        "size": "M",
        "gender": "Men",
        "timestamp": "2024-01-01T00:00:00"
    }]
    
    # Transformasi data menggunakan fungsi transform_data
    df = transform_data(data)
    
    # Memastikan bahwa harga dikonversi dengan benar ke dalam IDR (16000 x 100)
    expected_price = 100.00 * 16000
    assert df["price"].iloc[0] == expected_price, f"Expected price {expected_price}, but got {df['price'].iloc[0]}"
    