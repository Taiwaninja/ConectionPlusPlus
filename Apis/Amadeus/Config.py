#!/usr/bin/python
API_KEY = "VGtEgyodg5UO3S8nzlkS6FAvIK4bx4vW"
POINT_OF_INTRESET_API_URL = r"https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-circle"

# PARAMS
PARAM_API_KEY = "apikey"
PARAM_LAT = "latitude"
PARAM_LONG = "longitude"
PARAM_RADIUS = "radius"

# AMADEUS KEYS
AM_POINT_OF_INTRESET = "points_of_interest"
AM_DESC = "details"

# RESPONSE JSON
# Sample as MosesSample

#

POINT_OF_INTEREST_RETURN_FORMAT = {
    # TODO: add:"location_id" (outside format)
    "name": "title",
    # TODO: Calculate distance
    # "distance": blat,
    "location": {"lat": ["location", "latitude"], "long": ["location", "longitude"]},
    "desc": ["details", "description"],
    # TODO: Add rating
    # "rating": blat,
    "img": "main_image",
    "types": "categories"
}
REQUEST_MAIN = "points_of_interest"

# ENRICH

PARAM_ADDRESS = "address"
PARAM_LOCATION = "location"
PARAM_LOCATION_LAT = "lat"
PARAM_LOCATION_LONG = "long"

WANTED_CATEGORIES = ["Skyscrapers","architecture"]
