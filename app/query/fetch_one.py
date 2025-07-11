from app.db.connection import get_db_connection
from typing import Optional

def execute(query: str, values: tuple = ()) -> Optional[tuple]:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            result = cursor.fetchone()
            return result