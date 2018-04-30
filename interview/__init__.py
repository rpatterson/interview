"""
A minimal Flask application.
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')
db = SQLAlchemy(app)

ROOT_RESPONSE = 'Hello, World!'


@app.route('/')
def hello_world():
    return ROOT_RESPONSE
