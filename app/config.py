import os

DB_HOST = os.getenv('DB_HOST', 'db-main')
DB_PORT = os.getenv('DB_HOST', '5432')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'db-main')