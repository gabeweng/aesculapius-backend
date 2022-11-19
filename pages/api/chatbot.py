
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib import parse
import json

import cohere 
from cohere.classify import Example
import os
from dotenv import load_dotenv
load_dotenv()
cohere_api_key = os.environ['cohere_api_key']
print(cohere_api_key)
co = cohere.Client(cohere_api_key)
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
    if "msg" in dic:
      message = dic["msg"]
    else:
      message = "Wrong request, I need a msg parameter"

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
      chat_conv = "Patient: " + data["message"] + "\n"
      inputs=[data["message"] ]
      sentiment = co.classify(  
      model='medium',  
      inputs=inputs,  
      examples=examples)
      print(sentiment)
      response = co.generate(
      prompt=''.join(chat_conv)+"Doctor:",
        model='xlarge', max_tokens=20,   temperature=1.2,   k=0,   p=0.75,
        frequency_penalty=0,   presence_penalty=0, return_likelihoods='NONE',
        stop_sequences=["Patient:", "\n"]
    ).generations[0].text.strip().split("Patient:")[0]
    
      ret_obj = [{"text":response}]
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
