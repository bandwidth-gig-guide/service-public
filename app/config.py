from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'db-main')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'db-main')
