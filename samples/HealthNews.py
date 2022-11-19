import requests
import json
import os


KEY = os.environ['NYT Key']

x = requests.get(f"https://api.nytimes.com/svc/topstories/v2/health.json?api-key={KEY}")
y = json.loads(x.text)
print(y)

