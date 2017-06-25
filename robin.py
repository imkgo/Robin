# -*- coding: utf-8 -*-

from flask import Flask, render_template
import config
from flask_pymongo import PyMongo
import article_dao
app = Flask(__name__)
app.config.from_object(config)
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    with app.app_context():
        return render_template("article_list.html", articles=article_dao.find_all(mongo))


# 根据标题获取博客
@app.route("/<title>", methods=["post", "get"])
def article(title):
    with app.app_context():
        art = article_dao.find_article_by_title(title, mongo)
        return render_template("article.html", article=art)


if __name__ == '__main__':
    app.run(debug="enable")
