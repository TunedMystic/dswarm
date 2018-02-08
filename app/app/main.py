import datetime
import socket

from flask import Flask, jsonify, make_response

app = Flask(__name__)
application = app


def response_(data={}, status_code=200):
    return make_response(jsonify(**data), status_code)


@app.route('/')
def index_endpoint():
    return response_({
        'ref': socket.gethostname(),
        'timestamp': str(datetime.datetime.now().timestamp())
    })
