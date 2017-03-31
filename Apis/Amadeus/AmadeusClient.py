#!/usr/bin/python
from Apis.RestApiUtils import RestApiUtils
from Apis.Amadeus import Config
from Apis.GoogleMapsDirectionsLookup import get_directions_travel_duration
import datetime
import Apis.APIConsts
import json
from threading import Thread


class AmadeusClient(object):
    @classmethod
    def get_point_of_interest(cls, lat, long, end_time=None, radius=1, start_time=None):
        if start_time is None:
            start_time = datetime.datetime.utcnow() + datetime.timedelta(hours=+48)
        if end_time is None:
            end_time = start_time + datetime.timedelta(hours=13)

        params = {}
        params[Config.PARAM_API_KEY] = Config.API_KEY
        params[Config.PARAM_LAT] = lat
        params[Config.PARAM_LONG] = long
        params[Config.PARAM_RADIUS] = radius
        # return json.loads(RestApiUtils.rest_api_request(Config.POINT_OF_INTRESET_API_URL, params))
        places = json.loads(RestApiUtils.rest_api_request(Config.POINT_OF_INTRESET_API_URL, params))
        return cls.parse_amadeos_responses((lat, long), (start_time, end_time), places)

    @classmethod
    def parse_amadeos_responses(cls, curr_location, times, resp):
        locations_raw = resp[Config.REQUEST_MAIN]
        activities_parsed = [RestApiUtils.parse_response(location, Config.POINT_OF_INTEREST_RETURN_FORMAT) for location
                             in locations_raw]

        # Add address if works
        # activities_parsed = cls.enrich_and_filter_activities(activities_parsed)
        # TODO: removed filter
        #activities_parsed = cls.enrich_and_filter_activities(curr_location, times, activities_parsed)
        parsed_amadeos_response = {Apis.APIConsts.RETURN_LOCATION: activities_parsed}
        return parsed_amadeos_response

    @classmethod
    def enrich_and_filter_activities(cls, curr_location, times, activities):
        """
        Enriched activities after filter
        """

        def add_activity(curr_activity):
            enriched_or_filtered = cls.enrich_and_filter_activity(curr_location, times, curr_activity)
            if enriched_or_filtered is not None:
                after_filter_activties.append(enriched_or_filtered)

        after_filter_activties = []
        request_threads = []
        for activity in activities:
            new_thread = Thread(target=add_activity, args=(activity,))
            new_thread.start()
            request_threads.append(new_thread)

        [thd.join() for thd in request_threads]
        return after_filter_activties

    @classmethod
    def enrich_and_filter_activity(cls, (curr_lat, curr_long), (start_time, end_time), activity):
        # Check if in timelimits etc.
        calculated_times = get_directions_travel_duration(
                                                          float(curr_lat), float(curr_long),
                                                          activity['location']['lat'], activity['location']['long'],
                                                          start_time, False)
        if calculated_times is None:
            return None
        departure_time = calculated_times[0]
        calculated_times = get_directions_travel_duration(
                                                          activity['location']['lat'], activity['location']['long'],
                                                          float(curr_lat), float(curr_long),
                                                          calculated_times[1] + datetime.timedelta(hours=+2), False)
        if calculated_times is None:
            return None
        arrival_time = calculated_times[1]
        if start_time <= departure_time and end_time >= arrival_time:
            activity['time_data'] = {
                'start': str(departure_time),
                'duration': str(2), #TODO: Make a real duration
                'end': str(arrival_time)
            }
            return activity
        else:
            return None
