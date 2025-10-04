from uuid import UUID
from typing import Optional, List, Tuple
from app.query.fetch_list import execute
from app.util.list_to_array_string import list_to_array_string


def get_all_id(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[List[str]] = None,
    types: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
) -> list[UUID]:
    
    query, params = prepare(
        name=name,
        stateCode=stateCode,
        city=city,
        types=types,
        tags=tags
    )
    rows = execute(query, params)
    return [row[0] for row in rows]


def prepare(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[List[str]] = None,
    types: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
) -> Tuple[str, list]:
    
    query = "SELECT VenueID FROM Venue"

    filters = []
    params = []

    if name:
        filters.append("Venue.Title ILIKE %s")
        params.append(f"%{name}%")

    if stateCode:
        filters.append("Venue.StateCode = %s")
        params.append(stateCode)

    if city:
        filters.append("Venue.City = ANY(%s)")
        params.append(list_to_array_string(city))

    if types:
        filters.append("""
            EXISTS (
                SELECT 1 FROM VenueType
                WHERE VenueType.VenueID = Venue.VenueID
                AND VenueType.Type = ANY(%s::TYPEVENUE[])
            )
        """)
        params.append(list_to_array_string(types))

    if tags:
        filters.append("""
            EXISTS (
                SELECT 1 FROM VenueTag
                WHERE VenueTag.VenueID = Venue.VenueID
                AND VenueTag.Tag = ANY(%s::TAG[])
            )
        """)
        params.append(list_to_array_string(tags))

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY Venue.IsFeatured DESC, Venue.Title ASC;"

    return query, params