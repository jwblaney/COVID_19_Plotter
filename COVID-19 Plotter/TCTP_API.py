import requests
import json

_base_URL = "https://covidtracking.com/api/v1/"

def GetUSDailyJSON():
    URL = _base_URL + "us/daily.json"
    response = requests.get(url = URL)
    return response.text