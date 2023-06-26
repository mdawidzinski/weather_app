import requests
import json


class CurrentWeatherModel:
    def __init__(self):
        self.url = "https://danepubliczne.imgw.pl/api/data/synop/station/wroclaw"

    def get_data(self):
        response = requests.get(self.url)
        data = response.json()
        return data


