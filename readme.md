# membuat Venv 
python -m venv .env
lalu tambahkan sintak (karena saya pakai bash): source .env/Scripts/activate

# install semua depedencies di file requirements.txt
pip install -r requirements.txt

# Menjalankan skrip
python main.py

# Menjalankan unit test pada folder tests
python -m pytest tests

# Menjalankan test coverage pada folder tests
python -m pytest --cov=tests tests

# Url Google Sheets:
https://docs.google.com/spreadsheets/d/1tcg-tzEODzDEdQeawT6FD3oVgpYCEDqV4_Rf_MR-aT4/edit?usp=sharing
