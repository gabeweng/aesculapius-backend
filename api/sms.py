
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib import parse
import json
import requests
try:
  from api.util.bot import bot
except:
  from util.bot import bot
from twilio.twiml.messaging_response import MessagingResponse

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
    print(dic)
    self.setHeader(self)
    self.send_header('Content-type', 'text/html') # 'text/plain' for plain text
    self.end_headers()


    resp = MessagingResponse()
    resp.message("The Robots are coming! Head for the hills!")
    print(str(resp))
    # return str(resp)

    self.wfile.write(str(resp).encode())
    return
    # return "The Robots are coming! Head for the hills!"



  def do_POST(self):
    try:

      content_len = int(self.headers.get('content-length'))
      post_body = self.rfile.read(content_len)
      print(parse.parse_qs(post_body))
      msg = (parse.parse_qs(post_body)[b'Body'][0].decode("utf-8") )
      print(msg)
    #   data = json.loads(post_body)
    #   print("Received: ", data)
      self.setHeader(self)
      self.send_header('Content-type', 'text/html') # 'text/plain' for plain text
      self.end_headers()

      retintent,response= bot(msg)

      resp = MessagingResponse()
      resp.message(response)
      print(str(resp))
      # return str(resp)

      self.wfile.write(str(resp).encode())

    #   ret_obj = [{"text":FindHospitals(data["lat"],data["lon"])}]
    #   self.wfile.write(json.dumps(ret_obj).encode())
    #   #self.wfile.close()
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
    port = 5000
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
