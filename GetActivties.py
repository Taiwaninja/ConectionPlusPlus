#!/usr/bin/python

from bottle import route, run, debug, template, request, static_file, error
from Apis.Amadeus.AmadeusClient import AmadeusClient
import json


def jsonify(dic):
    print 'dic:', dic
    return json.dumps(dic, indent=4)


@route('/api/helloBlat', methods=["GET"])
def helloBlat():
    return jsonify({"Blat": "6"})


@route("/api/get_mock", methods=["GET"])
def get_mock():
    with open(r".\DataSamples\MosesSample.json", "r") as mosesFile:
        json
        moses = json.load(mosesFile)
    return jsonify(moses)


@route("/api/get_mock_amadeus", methods=["GET"])
def get_mock_amadeus():
    around_moses = AmadeusClient.get_point_of_interest(32.107898, 34.838002, 1)
    # TODO: If you make changes load and jasonify again
    return around_moses


def main():
    # remember to remove reloader=True and debug(True) when you move your
    # application from development to a productive environment
    debug(True)
    run(reloader=True)


if __name__ == '__main__':
    main()
