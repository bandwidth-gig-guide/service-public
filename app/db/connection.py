from fastapi import HTTPException
import psycopg2
from app.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_SSL_MODE

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            sslmode=DB_SSL_MODE
        )
        return connection
    
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error connecting to database: {str(e)}")
