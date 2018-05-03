"""
A minimal Flask application.
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_restful

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')
db = SQLAlchemy(app)
api = flask_restful.Api(app)

ROOT_RESPONSE = {'hello': 'world'}


class HelloWorld(flask_restful.Resource):
    def get(self):
        return ROOT_RESPONSE


api.add_resource(HelloWorld, '/')
