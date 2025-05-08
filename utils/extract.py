import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_page_html(url):
    """Ambil HTML mentah dari satu halaman produk."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_products_from_html(html):
    """Parse HTML dan ambil elemen produk."""
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("div", class_="collection-card")

def extract_product_info(product):
    """Ekstrak informasi dari satu produk. Return dict atau None jika tidak valid."""
    try:
        title = product.find("h3", class_="product-title").text.strip()
        if title == "Unknown Product":
            return None

        price_tag = product.find("span", class_="price") or product.find("p", class_="price")
        price = price_tag.text.strip() if price_tag else None
        if price in [None, "Price Unavailable"]:
            return None

        p_tags = product.find_all("p", style=True)
        if len(p_tags) < 4:
            return None

        rating = p_tags[0].text.replace("Rating: ", "").strip()
        if "Invalid" in rating:
            return None

        colors = p_tags[1].text.replace("Colors", "").strip()
        size = p_tags[2].text.replace("Size: ", "").strip()
        gender = p_tags[3].text.replace("Gender: ", "").strip()

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "colors": colors,
            "size": size,
            "gender": gender,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        print("Error extracting a product:", e)
        return None

def extract_products(base_url="https://fashion-studio.dicoding.dev/", pages=50):
    """
    Fungsi utama untuk mengekstrak produk dari beberapa halaman situs.
    """
    all_data = []
    for page in range(1, pages + 1):
        try:
            print(f"Scraping page {page}...")
            url = base_url if page == 1 else f"{base_url}page{page}"
            html = fetch_page_html(url)
            products = parse_products_from_html(html)

            for product in products:
                data = extract_product_info(product)
                if data:
                    all_data.append(data)
                if len(all_data) >= 1000:
                    return all_data
        except Exception as e:
            print(f"Error scraping page {page}:", e)
            continue
    return all_data
