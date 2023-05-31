from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello World!</p>"

port = environ.get("port", 5555)
host = environ.get("host", "0.0.0.0")
app.run(host, port)
