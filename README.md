Quick Start Roadmap
Follow these 9 steps to run the project on your local machine.

git clone <repo-url> — Repository download করুন
cd ajks — Folder-এ ঢুকুন
python -m venv venv — Virtual environment তৈরি করুন
venv\Scripts\Activate.ps1 (Windows) — Activate করুন Mac/Linux: source venv/bin/activate
pip install -r requirements.txt — সব package ইনস্টল
python manage.py migrate — Database setup
python manage.py createsuperuser — Admin account তৈরি (username/password মনে রাখুন)
python manage.py runserver — Server চালু
Browser → http://127.0.0.1:8000/ — Website দেখুন

python --version , Python 3.14.7
