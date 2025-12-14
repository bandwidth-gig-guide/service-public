from uuid import UUID
from app.query.fetch_list import execute

def get_recommended(event_id: UUID) -> list[UUID]:
    rows = execute(query(), value(event_id))
    result = [row[0] for row in rows]
    
    if len(result) < 8:
        remaining_needed = 8 - len(result)
        random_rows = execute(fallback_query(remaining_needed), fallback_value(event_id, result))
        result.extend([row[0] for row in random_rows])
    
    return result[:8]


def query():
    return """
        WITH SimilarEvents AS (
            SELECT Event.EventID
            FROM Event
            JOIN EventTag ON Event.EventID = EventTag.EventID
            WHERE Event.EventID != %s
            AND Event.StartDateTime > NOW()
            AND EventTag.Tag IN 
            (
                SELECT Tag 
                FROM EventTag 
                WHERE EventID = %s
            )
            GROUP BY Event.EventID
            ORDER BY COUNT(*) DESC, RANDOM()
            LIMIT 8
        ),

        SameDayEvents AS (
            SELECT Event.EventID
            FROM Event
            WHERE Event.EventID != %s
            AND Event.StartDateTime > NOW()
            ORDER BY Event.StartDateTime, RANDOM()
            LIMIT 8
        )

        SELECT EventID
        FROM 
        (
            (
                SELECT EventID
                FROM SimilarEvents
            )
            UNION
            (
                SELECT EventID
                FROM SameDayEvents
                WHERE SameDayEvents.EventID != %s
                AND SameDayEvents.EventID NOT IN (SELECT EventID FROM SimilarEvents)
            )
            UNION
            (
                SELECT Event.EventID
                FROM Event
                WHERE Event.IsFeatured = TRUE
                AND Event.EventID != %s
                AND Event.EventID NOT IN (SELECT EventID FROM SimilarEvents)
                AND Event.EventID NOT IN (SELECT EventID FROM SameDayEvents)
                ORDER BY RANDOM()
                LIMIT 4
            )
        )
        ORDER BY RANDOM()
        LIMIT 8;
    """

def value(event_id: UUID):
    return (str(event_id), str(event_id), str(event_id), str(event_id), str(event_id))


def fallback_query(limit: int):
    return f"""
        SELECT Event.EventID
        FROM Event
        WHERE Event.EventID != %s
        AND Event.StartDateTime > NOW()
        AND Event.EventID NOT IN ({', '.join(['%s'] * len([]))})
        ORDER BY RANDOM()
        LIMIT {limit};
    """

def fallback_value(event_id: UUID, existing_events: list[UUID]):
    return (str(event_id), *[str(eid) for eid in existing_events])
