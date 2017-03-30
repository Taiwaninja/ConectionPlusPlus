#!/usr/bin/python
from Apis.RestApiUtils import RestApiUtils
from Apis.Amadeus import Config
import json


class AmadeusClient(object):
    @classmethod
    def get_point_of_interest(cls, lat, long, radius=1):
        # TODO : Implement
        params = {}
        params[Config.PARAM_API_KEY] = Config.API_KEY
        params[Config.PARAM_LAT] = lat
        params[Config.PARAM_LONG] = long
        params[Config.PARAM_RADIUS] = radius
        return json.loads(RestApiUtils.rest_api_request(Config.POINT_OF_INTRESET_API_URL, params))
        places = json.loads(RestApiUtils.rest_api_request(Config.POINT_OF_INTRESET_API_URL, params))
        return cls.parse_amadeos_responses(places)

    def parse_amadeos_responses(cls, resp):

        pass


