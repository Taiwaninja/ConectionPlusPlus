#!/usr/bin/python
from Apis.RestApiUtils import RestApiUtils
from Apis.Amadeus import Config
from Apis import GoogleMapsAddressLookup
import datetime
import json


class AmadeusClient(object):
    @classmethod
    def get_point_of_interest(cls, lat, long, end_time=None, radius=1, start_time=None):
        if start_time is None:
            start_time = datetime.datetime.utcnow()
        if end_time is None:
            end_time = start_time + datetime.timedelta(hours=3)

        params = {}
        params[Config.PARAM_API_KEY] = Config.API_KEY
        params[Config.PARAM_LAT] = lat
        params[Config.PARAM_LONG] = long
        params[Config.PARAM_RADIUS] = radius
        # return json.loads(RestApiUtils.rest_api_request(Config.POINT_OF_INTRESET_API_URL, params))
        places = json.loads(RestApiUtils.rest_api_request(Config.POINT_OF_INTRESET_API_URL, params))
        return cls.parse_amadeos_responses(places)

    @classmethod
    def parse_amadeos_responses(cls, resp):
        locations_raw = resp[Config.REQUEST_MAIN]
        activities_parsed = [RestApiUtils.parse_response(location, Config.POINT_OF_INTEREST_RETURN_FORMAT) for location
                             in locations_raw]

        # Add address if works
        # activities_parsed = cls.enrich_and_filter_activities(activities_parsed)
        activities_parsed = cls.enrich_and_filter_activities(activities_parsed)
        parsed_amadeos_response = {Config.RETURN_LOCATION: activities_parsed}
        return parsed_amadeos_response

    @classmethod
    def enrich_and_filter_activities(cls, activities):
        """
        Enriched activities after filter
        """
        after_filter_activties = []
        for activity in activities:
            enriched_or_filtered = cls.enrich_and_filter_activity(activity)
            if enriched_or_filtered is not None:
                after_filter_activties.append(enriched_or_filtered)
        return activities

    @classmethod
    def enrich_and_filter_activity(cls, activity):
        # Check if in timelimits etc.
        return activity
