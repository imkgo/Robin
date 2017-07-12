from flask import Flask
import config

from flask_pymongo import PyMongo
app = Flask(__name__)
app.config.from_object(config)
mongo = PyMongo(app)
from views.articles import ARTICLE_PAGE
app.register_blueprint(ARTICLE_PAGE)

