from Apis.RestApiUtils import RestApiUtils
from Apis.Zomato import Config
from Apis import GoogleMapsAddressLookup
from Apis import APIConsts
import datetime
import requests
import json


class ZomatoClient(object):
    @classmethod
    def get_point_of_interest(cls, lat, long, end_time=None, radius=1, start_time=None):
        if start_time is None:
            start_time = datetime.datetime.utcnow()
        if end_time is None:
            end_time = start_time + datetime.timedelta(hours=3)
        params = {}
        params[Config.PARAM_LAT] = lat
        params[Config.PARAM_LONG] = long
        params[Config.PARAM_RADIUS] = radius
        url = RestApiUtils.build_request_url(Config.POINT_OF_INTRESET_API_URL, params)
        restaurants = requests.get(url, headers={"user-key": 'eb437426154058ef4547a6f81778539e'}).json()
        return cls.parse_zomato_response(restaurants)

    @classmethod
    def parse_zomato_response(cls, resp):
        resturaunts_raw = resp[Config.REQUEST_MAIN]
        activities_parsed = [RestApiUtils.parse_response(rest, Config.POINT_OF_INTEREST_RETURN_FORMAT) for rest
                             in resturaunts_raw]

        # Add address if works
        # activities_parsed = cls.enrich_and_filter_activities(activities_parsed)
        # TODO: Add ziv's enrich
        # activities_parsed = cls.enrich_and_filter_activities(activities_parsed)
        parsed_amadeos_response = {APIConsts.RETURN_LOCATION: activities_parsed}
        return parsed_amadeos_response
