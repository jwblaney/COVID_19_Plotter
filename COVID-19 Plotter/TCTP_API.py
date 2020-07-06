import requests
import json

_base_URL = "https://covidtracking.com/api/v1/"

def GetUSDailyJSON():
    URL = _base_URL + "us/daily.json"
    response = requests.get(url = URL)
    return response.text

def GetStateDailyJson(state):
    URL = _base_URL + "/states/"+state.lower()+"/daily.json"
    response = requests.get(url= URL)
    return response.text
