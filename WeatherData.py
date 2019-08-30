import datetime
import os

import requests
import json


class WeatherData():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(ROOT_DIR, 'Authentication.json')

    def __init__(self, city=None, day=None, threshold=None):
        self.city = city
        self.day = day
        self.threshold = threshold
        with open(self.CONFIG_PATH) as json_file:
            self.config = json.load(json_file)

    def set_city(self, city):
        self.city = city

    def set_day(self, day):
        self.day = day

    def set_threshold(self, threshold):
        self.threshold = threshold

    def check_day(self, day):
        if day == self.day : return True
        return False

    def check_temperature(self, temp):
        if temp>self.threshold:
            return False
        return True

    def get_current_weather_data(self):
        payload = {
                        'q': self.city,
                        'units': "metric",
                        'appid': self.config["Test"]["Api_Key"]
                  }
        response = requests.get(self.config["Test"]["Url"], params=payload)
        if response.status_code ==200:
            return json.loads(response.content)
        else:
            raise Exception("Api call failed with : ", response.content)





