#!/usr/bin/python
import urllib2
from urllib import urlencode
import json
import time
import datetime
from GoogleMapsAddressLookup import get_address_by_lon_lat

GOOGLE_API_KEY = 'AIzaSyDgQu2CSBVjgoICVHQTdDptAI9fh9yDX0g'


#'&arrival_time=1391374800'
GOOGLE_DIRECTIONS_LOOKUP = 'https://maps.googleapis.com/maps/api/directions/json?'


RESULTS_STRING = 'routes'
ADDRESS_STRING = 'legs'
def get_direction_data(js):
    if RESULTS_STRING not in js or len(js[RESULTS_STRING]) == 0 or\
                    ADDRESS_STRING not in js[RESULTS_STRING][0] or len(js[RESULTS_STRING][0][ADDRESS_STRING]) == 0:
        return None
    else:
        #TODO Choose correct destination and route
        res = js[RESULTS_STRING][0][ADDRESS_STRING][0]
        return datetime.datetime.fromtimestamp(res['departure_time']['value']), \
            datetime.datetime.fromtimestamp(res['arrival_time']['value'])


def get_directions_travel_duration(src_lat, src_lon,
                                   dst_lat, dst_lon,
                                   user_time, is_arrival_time = False,
                                   use_car = False):
    src = get_address_by_lon_lat(src_lat, src_lon)
    dst = get_address_by_lon_lat(dst_lat, dst_lon)
    if src is None or dst is None:
        return None
    travel_mode = 'driving' if use_car else 'transit'
    arrival_departure = 'arrival' if is_arrival_time else 'departure'
    utc_time = str(int(time.mktime(user_time.timetuple())))
    request = GOOGLE_DIRECTIONS_LOOKUP + \
              'origin=' + src.replace(' ', '+') + \
              '&destination=' + dst.replace(' ', '+') + \
              '&mode=' + travel_mode + \
              '&' + arrival_departure + '_time=' + utc_time + \
              '&key='+GOOGLE_API_KEY

    conn = urllib2.urlopen(request)
    st = conn.read()

    js = json.loads(st)
    #TODO Choose correct address
    return get_direction_data(js)

if __name__ == '__main__':
    print get_directions_travel_duration(40.7428759, -74.00584719999999,
                                         40.814505, -74.07272910000002,
                                         datetime.datetime.fromtimestamp(time.time())
                                         )


