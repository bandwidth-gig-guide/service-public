from uuid import UUID
from typing import Optional, List, Tuple
from app.query.fetch_list import execute
from app.util.list_to_array_string import list_to_array_string


def get_all_id(
    name: Optional[str] = None,
    country: Optional[str] = None,
    city: Optional[str] = None,
    types: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
    hasUpcomingPerformance: Optional[bool] = None
) -> list[UUID]:

    query, params = prepare(
        name=name,
        country=country,
        city=city,
        types=types,
        tags=tags,
        hasUpcomingPerformance=hasUpcomingPerformance
    )
    rows = execute(query, params)
    return [row[0] for row in rows]


def prepare(
    name: Optional[str] = None,
    country: Optional[str] = None,
    city: Optional[str] = None,
    types: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
    hasUpcomingPerformance: Optional[bool] = None
) -> Tuple[str, list]:

    query = "SELECT Artist.ArtistID FROM Artist"

    filters = []
    params = []

    if name:
        filters.append("Artist.Title ILIKE %s")
        params.append(f"%{name}%")

    if country:
        filters.append("Artist.Country = %s")
        params.append(country)

    if city:
        filters.append("Artist.City = %s")
        params.append(city)

    if types:
        filters.append("""
            EXISTS (
                SELECT 1 FROM ArtistType
                WHERE ArtistType.ArtistID = Artist.ArtistID
                AND ArtistType.Type = ANY(%s::TYPEARTIST[])
            )
        """)
        params.append(list_to_array_string(types))

    if tags:
        filters.append("""
            EXISTS (
                SELECT 1 FROM ArtistTag
                WHERE ArtistTag.ArtistID = Artist.ArtistID
                AND ArtistTag.Tag = ANY(%s::TAG[])
            )
        """)
        params.append(list_to_array_string(tags))

    if hasUpcomingPerformance is not None:
        filters.append(f"""
            EXISTS (
                SELECT 1 FROM EventPerformance
                WHERE EventPerformance.ArtistID = Artist.ArtistID
                AND EventPerformance.StartDateTime > NOW()
            ) = %s
        """)
        params.append(hasUpcomingPerformance)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    return query, params