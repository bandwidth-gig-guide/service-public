from app.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
from app.db.connection import get_db_connection

def test_db_connection():
    print("INFO:     Attempting DB connection")
    print(f"INFO:     - host: {DB_HOST}")
    print(f"INFO:     - port: {DB_PORT}")
    print(f"INFO:     - user: {DB_USER}")
    print(f"INFO:     - password: {DB_PASSWORD[:3] + '*' * (len(DB_PASSWORD) - 3) if DB_PASSWORD and len(DB_PASSWORD) > 3 else DB_PASSWORD}")
    print(f"INFO:     - dbname: {DB_NAME}")
    try:
        conn = get_db_connection()
        conn.cursor().execute("SELECT 1")
        print("INFO:     DB connection successful!")
    except Exception as e:
        print(f"ERROR:    DB connection failed: {e}")
    conn.close()