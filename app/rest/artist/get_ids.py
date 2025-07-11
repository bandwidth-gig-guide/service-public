from app.query.fetch_list import execute
from uuid import UUID

def get_ids() -> list[UUID]:
    rows = execute(query())
    return [row[0] for row in rows]


def query():
    return "SELECT ArtistID FROM Artist"