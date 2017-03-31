from GetActivties import get_google_places_hours_bl
import json

with open('DataSamples/Activity2.json', 'r') as js_file:
    js = json.load(js_file)
    new_locations = []
    for location in js['Locations']:
        loc = location['location']
        lat = loc['lat']
        lon = loc['long']
        keyword = location['name']
        opening_hours = get_google_places_hours_bl(lon, lat, 100, '', keyword)
        if opening_hours:
            new_location = location
            new_location['opening_hours'] = opening_hours
            new_locations.append(new_location)

    with open(r'DataSamples/Activity2H.json', 'wb') as js_out:
        json.dump(new_locations, js_out, indent=4)
