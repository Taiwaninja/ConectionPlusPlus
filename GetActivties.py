#!/usr/bin/python

from bottle import route, run, debug, response, template, request, static_file, error, hook
from Apis.Amadeus.AmadeusClient import AmadeusClient
import json
import os


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


@route("/api/get_amadeus", methods=["GET"])
def get_amadeus():
    """
    http://127.0.0.1:8080/api/get_amadeus?lon=32.007966&lat=34.53866&d=30
    """
    lon = request.params.get('lon', default=32.107898)
    lat = request.params.get('lat', default=34.838002)
    d = request.params.get('d', default=1)
    around_moses = AmadeusClient.get_point_of_interest(lon, lat, d)
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
    run(reloader=True)


if __name__ == '__main__':
    main()
