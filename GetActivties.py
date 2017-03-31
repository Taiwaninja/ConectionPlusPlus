#!/usr/bin/python

from bottle import route, run, debug, response, template, request, static_file, error, hook
from Apis.Amadeus.AmadeusClient import AmadeusClient
import json
import os
import requests


def jsonify(dic):
    """
    Pretty-print a dictionary as a JSON string
    """
    return json.dumps(dic, indent=4)


@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@route('/api/helloBlat', methods=["GET"])
def helloBlat():
    return jsonify({"Blat": "6"})


@route("/api/get_mock", methods=["GET"])
def get_mock():
    with open(os.path.join(*['.', 'DataSamples', 'MosesSample.json']), 'r') as mosesFile:
        moses = json.load(mosesFile)
    return jsonify(moses)
    
    
@route("/api/get_google_places_details", methods=["GET"])
def get_google_places_details():
    """
    http://127.0.0.1:8080/api/get_google_places_details?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4
    """
    placeid = request.params.get('placeid', default='')
    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=AIzaSyDgQu2CSBVjgoICVHQTdDptAI9fh9yDX0g' % (placeid,)
    r = requests.get(url)
    js = r.json()
    return jsonify(js)
    
    
@route("/api/get_google_places", methods=["GET"])
def get_google_places():
    """
    view-source:http://127.0.0.1:8080/api/get_google_places?longitude=-73.98513&latitude=40.75889&radius=300&type=caffee&keyword=starbucks
    """
    longitude = request.params.get('longitude', default=-73.98513)
    latitude = request.params.get('latitude', default=40.75889)
    radius = request.params.get('radius', default=5000)
    obj_type = request.params.get('type', default='')
    obj_keyword = request.params.get('keyword', default='')
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=%s&type=%s&keyword=%s&key=AIzaSyDgQu2CSBVjgoICVHQTdDptAI9fh9yDX0g' % (latitude, longitude, radius, obj_type, obj_keyword)
    r = requests.get(url)
    js = r.json()
    return jsonify(js)
    
    
@route("/api/get_restaurants", methods=["GET"])
def get_restaurants():
    """
    http://127.0.0.1:8080/api/get_restaurants?longitude=-73.98513&latitude=40.75889&radius=50
    """
    longitude = request.params.get('longitude', default=-73.98513)
    latitude = request.params.get('latitude', default=40.75889)
    radius = request.params.get('radius', default=1000)
    url = 'https://developers.zomato.com/api/v2.1/search?lat=%s&lon=%s&radius=%s' % (latitude, longitude, radius)
    r = requests.get(url, headers={"user-key":'eb437426154058ef4547a6f81778539e', 'Accept': 'application/json'})
    js = r.json()
    return jsonify(js)
    
    
@route("/api/get_amadeus", methods=["GET"])
def get_amadeus():
    """
    http://127.0.0.1:8080/api/get_amadeus?longitude=32.007966&latitude=34.53866&radius=30
    """
    longitude = request.params.get('longitude', default=32.107898)
    latitude = request.params.get('latitude', default=34.838002)
    radius = request.params.get('radius', default=1)
    around_moses = AmadeusClient.get_point_of_interest(longitude, latitude, radius=radius)
    # TODO: If you make changes load and jasonify again
    return jsonify(around_moses)


@route("/api/get_mock_amadeus", methods=["GET"])
def get_mock_amadeus():
    around_moses = AmadeusClient.get_point_of_interest(32.107898, 34.838002, 1)
    # TODO: If you make changes load and jasonify again
    return jsonify(around_moses)


def main():
    # remember to remove reloader=True and debug(True) when you move your
    # application from development to a productive environment
    debug(True)
    run(host="0.0.0.0", reloader=True)


if __name__ == '__main__':
    main()
