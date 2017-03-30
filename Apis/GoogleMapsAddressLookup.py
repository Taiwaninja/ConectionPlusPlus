#!/usr/bin/python
import urllib2
import json

GOOGLE_API_KEY = 'AIzaSyDgQu2CSBVjgoICVHQTdDptAI9fh9yDX0g'

GOOGLE_ADDRESS_LOOKUP = 'https://maps.googleapis.com/maps/api/geocode/json?'


def get_address_by_lon_lat(lat, lon):
    request = GOOGLE_ADDRESS_LOOKUP + 'latlng='+str(lat)+','+str(lon)+'&key='+GOOGLE_API_KEY
    conn = urllib2.urlopen(request)
    st = conn.read()

    js = json.loads(st)
    #TODO Choose correct address
    return js['results'][0]['formatted_address']


def get_address_by_name(name):
    request = GOOGLE_ADDRESS_LOOKUP + 'address='+str(name.replace(' ', '+'))+'&key='+GOOGLE_API_KEY
    conn = urllib2.urlopen(request)
    st = conn.read()

    js = json.loads(st)
    #TODO Choose correct address
    return js['results'][0]['formatted_address']


if __name__ == '__main__':
    print get_address_by_lon_lat(40.714232, -73.9612889)
    print get_address_by_name('Assuta Medical Center')


