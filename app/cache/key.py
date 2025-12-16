class RECORD:
    ARTIST = "artist"
    EVENT = "event"
    VENUE = "venue"

class ARTIST:
    DETAILED = f"{RECORD.ARTIST}:detailed"
    BRIEF = f"{RECORD.ARTIST}:brief"
    RECOMMENDED = f"{RECORD.ARTIST}:recommended"
    IDS = f"{RECORD.ARTIST}:ids"


class EVENT:
    DETAILED = f"{RECORD.EVENT}:detailed"
    BRIEF = f"{RECORD.EVENT}:brief"
    RECOMMENDED = f"{RECORD.EVENT}:recommended"
    IDS = f"{RECORD.EVENT}:ids"
    IDS_BY_DATE = f"{RECORD.EVENT}:ids_by_date"


class VENUE:
    DETAILED = f"{RECORD.VENUE}:detailed"
    BRIEF = f"{RECORD.VENUE}:brief"
    RECOMMENDED = f"{RECORD.VENUE}:recommended"
    IDS = f"{RECORD.VENUE}:ids"
    CITIES = f"{RECORD.VENUE}:cities"
