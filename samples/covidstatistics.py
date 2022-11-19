import requests
import json
import os

APIKeyCovid = os.environ['APIKeyCovid']

date = "2022-11-18" #Should be one day before current date


import requests

url = f"https://covid-19-data-nyt.p.rapidapi.com/specific/{date}"

headers = {
	"X-RapidAPI-Key": APIKeyCovid,
	"X-RapidAPI-Host": "covid-19-data-nyt.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)