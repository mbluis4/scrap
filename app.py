from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import os



app = Flask(__name__)
frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
origins = [frontend, backend]
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  expose_headers="location,link",
  allow_headers="content-type,if-modified-since",
  methods="OPTIONS,GET,HEAD,POST"
)

@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  return
