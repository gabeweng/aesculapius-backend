import requests
import json
import os

date = "2022-11-18"  #Should be one day before current date

id = "7495e43c0emshb73f62d4a2588dep170bafjsnecdb6397f918"
url = "https://diagnosis.p.rapidapi.com/api/DDxItems/"

querystring = {"AuthenticationID": "DEMO_AuthenticationID"}

payload = {
  "id": "9999",
  "tests": "[]",
  "symptoms": "[{\"ID\":13},{\"ID\":6},{\"ID\":103},{\"ID\":14}]"
}
headers = {
  "content-type": "application/json",
  "X-RapidAPI-Key": id,
  "X-RapidAPI-Host": "diagnosis.p.rapidapi.com"
}

response = requests.request("POST",
                            url,
                            json=payload,
                            headers=headers,
                            params=querystring)
x = requests.get(
  f"https://diagnosisapi.azurewebsites.net/api/DDxItems/9999?AuthenticationID=DEMO_AuthenticationID"
)
y = json.loads(x.text)



thename = ""

for i in range(len(y)): #Unrealable Must Regester for full information 
  print(y[i]['name'])
