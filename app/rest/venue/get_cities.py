from app.query.fetch_list import execute

def get_cities() -> list[str]:
    rows = execute(query)
    return [row[0] for row in rows]

query = "SELECT DISTINCT City FROM Venue ORDER BY City ASC;"


