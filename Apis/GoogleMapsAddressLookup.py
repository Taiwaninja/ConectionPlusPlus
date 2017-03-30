#!/usr/bin/python
import urllib2
from urllib import urlencode
import json

GOOGLE_API_KEY = 'AIzaSyDgQu2CSBVjgoICVHQTdDptAI9fh9yDX0g'

GOOGLE_ADDRESS_LOOKUP = 'https://maps.googleapis.com/maps/api/geocode/json?'


RESULTS_STRING = 'results'
ADDRESS_STRING = 'formatted_address'
def get_address_from_geodata(js):
    if RESULTS_STRING not in js or len(js[RESULTS_STRING]) == 0 or ADDRESS_STRING not in js[RESULTS_STRING][0]:
        return None
    else:
        return js[RESULTS_STRING][0][ADDRESS_STRING]

def get_address_by_lon_lat(lat, lon):
    request = GOOGLE_ADDRESS_LOOKUP + 'latlng='+str(lat)+','+str(lon)+'&key='+GOOGLE_API_KEY
    conn = urllib2.urlopen(request)
    st = conn.read()

    js = json.loads(st)
    #TODO Choose correct address
    return get_address_from_geodata(js)


def get_address_by_name(name):
    request = GOOGLE_ADDRESS_LOOKUP + 'address='+str(name.replace(' ', '+'))+'&key='+GOOGLE_API_KEY
    conn = urllib2.urlopen(request)
    st = conn.read()

    js = json.loads(st)
    #TODO Choose correct address
    return get_address_from_geodata(js)


if __name__ == '__main__':
    print get_address_by_lon_lat(40.714232, -73.9612889)
    print get_address_by_name('Assuta Medical Center')


