from app.query.fetch_one import execute
from app.format.venue_complete import format
from app.model.venue_complete import VenueComplete
from uuid import UUID

def get(venue_id: UUID) -> VenueComplete:
    response = execute(query(), value(venue_id))
    return format(response)

def query():
    return """
        SELECT 
            Venue.VenueID,
            Venue.Title,
            Venue.City,
            Venue.StateCode,
            Venue.StreetAddress,
            Venue.PostCode,
            Venue.Description,
            Venue.WebsiteURL,
            Venue.PhoneNumber,
            ('http://www.googlemaps.com') AS GoogleMapsEmbedURL,

            EXISTS(
                SELECT 1 
                FROM VenueFeatured 
                WHERE VenueID = Venue.VenueID
            ) AS isFeatured,

            (
                SELECT json_agg(Image.URL ORDER BY VenueImage.DisplayOrder ASC)
                FROM Image
                JOIN VenueImage ON Image.ImageID = VenueImage.ImageID
                WHERE VenueImage.VenueID = Venue.VenueID
            ) AS ImageURLs,

            (
                SELECT json_agg(json_build_object(
                    'SocialPlatform', SocialPlatform,
                    'Handle', Handle,
                    'URL', URL
                ))
                FROM VenueSocial
                WHERE VenueSocial.VenueID = Venue.VenueID
            ) AS Socials,

            (
                SELECT json_agg(Type)
                FROM VenueType
                WHERE VenueType.VenueID = Venue.VenueID
            ) AS Types,

            (
                SELECT json_agg(Tag)
                FROM VenueTag
                WHERE VenueTag.VenueID = Venue.VenueID
            ) AS Tags,

            (
                SELECT json_build_object(
                    'MonOpen', MonOpen,
                    'MonClose', MonClose,
                    'TueOpen', TueOpen,
                    'TueClose', TueClose,
                    'WedOpen', WedOpen,
                    'WedClose', WedClose,
                    'ThurOpen', ThurOpen,
                    'ThurClose', ThurClose,
                    'FriOpen', FriOpen,
                    'FriClose', FriClose,
                    'SatOpen', SatOpen,
                    'SatClose', SatClose,
                    'SunOpen', SunOpen,
                    'SunClose', SunClose
                )
                FROM VenueOpeningHours
                WHERE VenueOpeningHours.VenueID = Venue.VenueID
                LIMIT 1
            ) AS OpeningHours

        FROM Venue
        WHERE Venue.VenueID = %s;
    """

def value(venue_id: UUID):
    return (str(venue_id),)