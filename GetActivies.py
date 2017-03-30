#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/api/helloBlat', methods=["GET"])
def helloBlat():
    return jsonify({"Blat": "6"})


@app.route("/api/get_mock", methods=["GET"])
def get_mock():
    with open(r".\DataSamples\MosesSample.json", "r") as mosesFile:
        json
        moses = json.load(mosesFile)
    return jsonify(moses)


if __name__ == '__main__':
    app.run(debug=True)
