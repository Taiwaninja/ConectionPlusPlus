#!/usr/bin/python
import json
import urllib2

conn = urllib2.urlopen('http://127.0.0.1:8080/api/get_mock')
st = conn.read()

js = json.loads(st)
print json.dumps(js, indent=4)