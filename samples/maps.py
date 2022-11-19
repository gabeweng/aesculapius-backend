import requests
import json
import os
GoogleMapsApi = os.environ['GoogleMapsApi']
def FindHospitals(Lat, Long):
  url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={Lat}%2C{Long}&radius=4000&type=hospital&keyword=Hospital&key={GoogleMapsApi}"

  payload = {}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)

  y = json.loads(response.text)
  return [y["results"][0]["geometry"]["location"],y["results"][1]["geometry"]["location"],y["results"][2]["geometry"]["location"]]


print(FindHospitals(40.730610,-73.935242))
