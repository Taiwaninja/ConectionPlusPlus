#!/usr/bin/python

from bottle import route, run, debug, response, template, request, static_file, error, hook
from Apis.Amadeus.AmadeusClient import AmadeusClient
from Apis.Zomato.ZomatoClient import ZomatoClient
from Apis.ActivityRetriever import ActivityRetriever
import json
import datetime
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


@route("/api/get_flights", methods=["GET"])
def get_flights():
    """
    http://127.0.0.1:8080/api/get_flights?longitude=-73.98513&latitude=40.75889&radius=300&type=caffee
    :return: 
    """
    with open(os.path.join(*['.', 'DataSamples', 'flights.json']), 'rb') as flight_file:
        flight = json.load(flight_file)
    return jsonify(flight)


@route("/api/get_flights_back", methods=["GET"])
def get_flights_back():
    """
    http://127.0.0.1:8080/api/get_flights_back?longitude=-73.98513&latitude=40.75889&radius=300&type=caffee
    :return: 
    """
    with open(os.path.join(*['.', 'DataSamples', 'flightsBack.json']), 'rb') as flight_file:
        flight = json.load(flight_file)
    return jsonify(flight)


@route("/api/get_flights_back_forth", methods=["GET"])
def get_flights_back_forth():
    """
    http://127.0.0.1:8080/api/get_flights_back_forth?longitude=-73.98513&latitude=40.75889&radius=300&type=caffee
    :return: 
    """
    with open(os.path.join(*['.', 'DataSamples', 'flightsBack.json']), 'rb') as flight_file:
        flight = json.load(flight_file)
    with open(os.path.join(*['.', 'DataSamples', 'flightsBack.json']), 'rb') as flight_file:
        flightBack = json.load(flight_file)
    flights = {"OUTBOUND": flight, "INBOUND": flightBack}
    return jsonify(flights)


def get_google_places_bl(latitude, longitude, radius, obj_type, obj_keyword):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=%s&type=%s&keyword=%s&key=AIzaSyDgQu2CSBVjgoICVHQTdDptAI9fh9yDX0g' % (
        latitude, longitude, radius, obj_type, obj_keyword)
    r = requests.get(url)
    js = r.json()
    if 'results' in js:
        for result in js['results']:
            pid = result['place_id']
            ##PATCH:: Opening hours##
            try:
                open_hours = json.loads(get_google_places_details_bl(pid))['result']['opening_hours']
                result['opening_hours'] = open_hours
            except KeyError:
                pass
            except:
                print 'PlaceID:', pid, '====ERROR_AT_OPEN_HOURS====='
                import traceback
                print traceback.format_exc()
                pass
                #########################
    return js


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
    return jsonify(get_google_places_bl(latitude, longitude, radius, obj_type, obj_keyword))


def get_google_places_hours_bl(longitude, latitude, radius, obj_type, obj_keyword):
    try:
        x = get_google_places_bl(latitude, longitude, radius, obj_type, obj_keyword)
        return x['results'][0]['opening_hours']['weekday_text']
    except Exception:
        return None


@route("/api/get_google_places_hours", methods=["GET"])
def get_google_places_hours():
    """
    view-source:http://127.0.0.1:8080/api/get_google_places_hours?longitude=-73.98513&latitude=40.75889&radius=300&type=caffee&keyword=starbucks
    """
    longitude = request.params.get('longitude', default=-73.98513)
    latitude = request.params.get('latitude', default=40.75889)
    radius = request.params.get('radius', default=5000)
    obj_type = request.params.get('type', default='')
    obj_keyword = request.params.get('keyword', default='')
    return jsonify(get_google_places_hours_bl(longitude, latitude, radius, obj_type, obj_keyword))


def get_google_places_details_bl(placeid):
    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=AIzaSyDgQu2CSBVjgoICVHQTdDptAI9fh9yDX0g' % (
        placeid,)
    r = requests.get(url)
    js = r.json()
    return jsonify(js)


@route("/api/get_google_places_details", methods=["GET"])
def get_google_places_details():
    """
    http://127.0.0.1:8080/api/get_google_places_details?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4
    """
    placeid = request.params.get('placeid', default='')
    return get_google_places_details_bl(placeid)


@route("/api/get_restaurants", methods=["GET"])
def get_restaurants():
    """
    http://127.0.0.1:8080/api/get_restaurants?longitude=-73.98513&latitude=40.75889&radius=50
    """
    longitude = request.params.get('longitude', default=-73.98513)
    latitude = request.params.get('latitude', default=40.75889)
    radius = request.params.get('radius', default=1000)
    # url = 'https://developers.zomato.com/api/v2.1/search?lat=%s&lon=%s&radius=%s' % (latitude, longitude, radius)
    # r = requests.get(url, headers={"user-key":'eb437426154058ef4547a6f81778539e'})
    # js = r.json()
    js = ZomatoClient.get_point_of_interest(latitude, longitude, radius=radius)
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


@route("/api/get_activities", methods=["GET"])
def get_activities():
    """
    http://127.0.0.1:8080/api/get_activities?longitude=32.007966&latitude=34.53866&radius=30&deal_id=blat
    http://127.0.0.1:8080/api/get_activities?longitude=8.5643405&latitude=50.0379326&radius=30&deal_id=SC_139604220_16_110417_LH
    """
    longitude = float(request.params.get('longitude', default=32.107898))
    latitude = float(request.params.get('latitude', default=34.838002))
    radius = request.params.get('radius', default=1)
    deal_id = request.params.get("deal_id", default=None)
    # TODO : Add shit
    start_time = datetime.datetime.utcnow()
    end_time = start_time + datetime.timedelta(days=5)
    if deal_id is not None:
        if deal_id == "SC_139604220_16_110417_LH":
            # If first flight
            if 50 <= latitude and latitude <= 51:
                with open(os.path.join(*['.', 'DataSamples', 'Activity1.json']), 'r') as activity_file:
                    activity = json.load(activity_file)
                    return jsonify(activity)
            else:
                with open(os.path.join(*['.', 'DataSamples', 'Activity2.json']), 'r') as activity_file:
                    activity = json.load(activity_file)
                    return jsonify(activity)

    activities = ActivityRetriever.get_point_of_interest(longitude, latitude, start_time=start_time, end_time=end_time,
                                                         radius=radius)
    return jsonify(activities)


def main():
    # remember to remove reloader=True and debug(True) when you move your
    # application from development to a productive environment
    debug(True)
    run(host="0.0.0.0", reloader=True)


if __name__ == '__main__':
    main()
