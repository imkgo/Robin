""" robin
"""
from flask import Flask

import config

from flask_pymongo import PyMongo

APP = Flask(__name__)
APP.config.from_object(config)
MONGO = PyMongo(APP)
