# -*- coding: utf-8 -*-

from flask import Flask, render_template
import article_dao
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", articles=article_dao.find_all())




@app.route("/ethan")
def hello():
    return "<h1>Hello, eth11an!</h1>"


@app.route("/<user_name>")
def hello1(user_name):
    return "<h1>Hello, %s!</h1>" % user_name


@app.route("/<year>/<month>/<day>/<title>")
def article(year, month, day, title):
    print year
    print month
    print day
    print title

    return title


if __name__ == '__main__':
    app.run(debug="enable")
