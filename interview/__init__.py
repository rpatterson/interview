"""
A minimal Flask application.
"""

from flask import Flask
app = Flask(__name__)


ROOT_RESPONSE = 'Hello, World!'


@app.route('/')
def hello_world():
    return ROOT_RESPONSE
