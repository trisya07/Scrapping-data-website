from utils.extract import extract_products
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_gsheet
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    
    try:
        logging.info("Starting the extraction process...")
        raw_data = extract_products()
        
        logging.info("Starting data transformation...")
        clean_data = transform_data(raw_data)
        
        logging.info("Saving data to CSV...")
        load_to_csv(clean_data)
        
        logging.info("Loading data to Google Sheets...")
        load_to_gsheet(clean_data, "Data Produk Fashion")
        
        logging.info("Process completed successfully.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        # Jika ada error, pastikan untuk memberikan feedback tentang masalah yang terjadi
        print(f"Process failed: {e}")

if __name__ == "__main__":
    main()
