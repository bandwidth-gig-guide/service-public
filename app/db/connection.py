from fastapi import HTTPException
import psycopg2
from app.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_db_connection():
    print("INFO:     Attempting DB connection")
    print(f"INFO:     host: {DB_HOST}")
    print(f"INFO:     user: {DB_USER}")
    print(f"INFO:     password: {DB_PASSWORD[:3] + '*' * (len(DB_PASSWORD) - 3) if DB_PASSWORD and len(DB_PASSWORD) > 3 else DB_PASSWORD}")
    print(f"INFO:     dbname: {DB_NAME}")
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )
        print("INFO:     DB connection successful!")
        return connection
    
    except psycopg2.Error as e:
        print(f"ERROR:    DB connection failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error connecting to database: {str(e)}")
