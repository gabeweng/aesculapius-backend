import requests
import json
import os


date = "2022-11-18" #Should be one day before current date

id = os.environ["CheckerKey"]
url = "https://diagnosis.p.rapidapi.com/api/DDxItems/"

querystring = {"AuthenticationID":"DEMO_AuthenticationID"}

payload = {
	"id": "9999",
	"tests": "[]",
	"symptoms": "[{\"ID\":1},{\"ID\":18},{\"ID\":103}]"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": id,
	"X-RapidAPI-Host": "diagnosis.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
x = requests.get(f"https://diagnosisapi.azurewebsites.net/api/DDxItems/9999?AuthenticationID=DEMO_AuthenticationID")
y = json.loads(x.text)
print(y)

