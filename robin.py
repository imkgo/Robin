# -*- coding: utf-8 -*-

from flask import Flask, render_template
import article_dao
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return render_template("article_list.html", articles=article_dao.find_all())


# 根据标题获取博客
@app.route("/<title>", methods=["post", "get"])
def article(title):
    art = article_dao.find_article_by_title(title)
    return render_template("article.html", article=art)


#
# @app.route("/<year>/<month>/<day>")
# def article(year, month, day, title):
#     print year
#     print month
#     print day
#     print title
#
#     return title


if __name__ == '__main__':
    app.run(debug="enable")
