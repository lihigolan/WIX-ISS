import json
from constants import *
import requests

cities_config = open(CONFIG_CITIES_PATH)
cities = json.load(cities_config)
web_config = open(CONFIG_WEB_PATH)
web = json.load(web_config)

URL = web[URL]
num = web[PASSES]

def getData():
    ans = {}
    for city in cities:
        city_lat = cities[city][LATITUDE]
        city_lon = cities[city][LONGITUDE]
        PARAMS = {LATITUDE__PARAM: city_lat, LONGITUDE_PARAM: city_lon, NUMBER_PARAM: num}

        try:
            req = requests.get(url=URL, params=PARAMS)
            if req.status_code == OK:
                data = req.json()
                city_data = data[RESPONSE]
                ans[city] = city_data

        except Exception as exc:
            print(exc)

    return ans

