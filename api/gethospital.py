
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib import parse
import json
import requests

import os
from dotenv import load_dotenv
load_dotenv()
cohere_api_key = os.environ['cohere_api_key']
def FindHospitals(Lat, Long):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={Lat}%2C{Long}&radius=4000&type=hospital&keyword=Hospital&key={GoogleMapsApi}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    y = json.loads(response.text)
    return [y["results"][0]["geometry"]["location"],y["results"][1]["geometry"]["location"],y["results"][2]["geometry"]["location"]]

class handler(BaseHTTPRequestHandler):
  def setHeader(s, self):
    self.send_response(200)
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Access-Control-Allow-Headers", "*")
    self.send_header("Access-Control-Allow-Methods","*")
  def do_OPTIONS(self):
    self.setHeader(self)
    self.end_headers()

  def do_HEAD(self):
    self.setHeader(self)
    self.end_headers()

  def do_GET(self):
    dic = dict(parse.parse_qsl(parse.urlsplit(self.path).query)) # parse the query string

    self.setHeader(self)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    # if `msg=` is in the query string
    if "lat" in dic and "lon" in dic:
      message = [dic["lat"],dic["lon"]]
    else:
      message = "Wrong request, I need a lat and lon parameter"

    # create a dictionary to be returned as json
    ret_obj = {'reply':str(message)} 
    self.wfile.write(json.dumps(ret_obj).encode())

    return

   



  def do_POST(self):
    try:

      content_len = int(self.headers.get('content-length'))
      post_body = self.rfile.read(content_len)
      data = json.loads(post_body)
      print("Received: ", data)
      self.setHeader(self)
      self.send_header('Content-type', 'application/json') # 'text/plain' for plain text
      self.end_headers()
      
    
      ret_obj = [{"text":FindHospitals(data["lat"],data["lon"])}]
      self.wfile.write(json.dumps(ret_obj).encode())
      #self.wfile.close()
      return
    except Exception as err:
      print(f"Unexpected {err=}, {type(err)=}")
      ret_obj = [{"text": f"Unexpected {err=}"}]
      self.send_response(200)
      self.send_header("Access-Control-Allow-Origin", "*")
      self.send_header("Access-Control-Allow-Headers", "*")
      self.send_header('Content-type', 'application/json') # 'text/plain' for plain text
      self.end_headers()
      self.wfile.write(json.dumps(ret_obj).encode())
      #self.wfile.close()

## Run the server, for local testing
def main():
    port = 80
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
