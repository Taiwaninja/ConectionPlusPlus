API_KEY = "eb437426154058ef4547a6f81778539e"
POINT_OF_INTRESET_API_URL = "https://developers.zomato.com/api/v2.1/search"

PARAM_API_KEY_HEADER = "user-key"
PARAM_LAT = "lat"
PARAM_LONG = "lon"
PARAM_RADIUS = "radius"

POINT_OF_INTEREST_RETURN_FORMAT = {
    # TODO: add:"location_id" (outside format)
    "name": ["restaurant", "name"],
    # TODO: Calculate distance
    # "distance": blat,
    "location": {"lat": ["restaurant", "location", "latitude"], "long": ["restaurant", "location", "longitude"]},
    "desc": None,
    # TODO: Add rating
    # "rating": blat,
    "img": ["restaurant", "featured_image"],
    "types": ["restaurant", "cuisines"]
}

REQUEST_MAIN = "restaurants"
