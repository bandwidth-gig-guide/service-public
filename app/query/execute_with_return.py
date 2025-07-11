from app.db.connection import get_db_connection

def execute(query: str, values: tuple = ()) -> tuple:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            result = cursor.fetchone()
            connection.commit()
            return result