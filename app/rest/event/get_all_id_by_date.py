from uuid import UUID
from datetime import date
from typing import Optional, List, Dict
from app.query.fetch_list import execute
from app.util.list_to_array_string import list_to_array_string


def get_all_id_by_date(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[List[str]] = None,
    maxPrice: Optional[int] = None,
    types: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
    dates: Optional[List[date]] = None
) -> Dict[date, List[UUID]]:
    
    query, params = prepare(
        name=name,
        stateCode=stateCode,
        city=city,
        maxPrice=maxPrice,
        types=types,
        tags=tags,
        dates=dates
    )
    rows = execute(query, params)
    result = {}
    for start_datetime, event_id in rows:
        event_date = start_datetime.date()
        if event_date not in result:
            result[event_date] = []
        result[event_date].append(UUID(str(event_id)))

    return result


def prepare(
    name: Optional[str] = None,
    stateCode: Optional[str] = None,
    city: Optional[List[str]] = None,
    maxPrice: Optional[int] = None,
    types: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
    dates: Optional[List[date]] = None
) -> tuple[str, list]:
    
    query = """
        SELECT 
            StartDateTime,
            EventID
        FROM Event
        WHERE StartDateTime > NOW()
    """

    filters = []
    params = []

    if name:
        filters.append("Event.Title ILIKE %s")
        params.append(f"%{name}%")

    if stateCode:
        filters.append("""
            EXISTS (
                SELECT 1 FROM Venue
                WHERE Venue.StateCode = %s
                AND Venue.VenueID = Event.VenueID
            )
        """)
        params.append(stateCode)

    if city:
        filters.append("""
            EXISTS (
                SELECT 1 FROM Venue
                WHERE Venue.City = ANY(%s)
                AND Venue.VenueID = Event.VenueID
            )
        """)
        params.append(list_to_array_string(city))

    if maxPrice is not None:
        filters.append("""
            EXISTS (
                SELECT 1 FROM EventPrice
                WHERE EventPrice.EventID = Event.EventID
                AND EventPrice.Price <= %s
            )
        """)
        params.append(maxPrice)

    if types:
        filters.append("""
            EXISTS (
                SELECT 1 FROM EventType
                WHERE EventType.EventID = Event.EventID
                AND EventType.Type = ANY(%s::TYPEEVENT[])
            )
        """)
        params.append(list_to_array_string(types))

    if tags:
        filters.append("""
            EXISTS (
                SELECT 1 FROM EventTag
                WHERE EventTag.EventID = Event.EventID
                AND EventTag.Tag = ANY(%s::TAG[])
            )
        """)
        params.append(list_to_array_string(tags))

    if dates:
        filters.append("DATE(StartDateTime) = ANY(%s::DATE[])")
        params.append(dates)

    if filters:
        query += " AND " + " AND ".join(filters)

    query += " ORDER BY Event.IsFeatured DESC, Event.StartDateTime ASC;"

    return query, params
