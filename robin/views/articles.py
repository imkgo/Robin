# -*- coding: utf-8 -*-

from flask import render_template, Blueprint

from robin import mongo
from robin.models import article

article_page = Blueprint("article_page", __name__, template_folder="templates")


@article_page.route('/')
def index():
    arts = mongo.db.article.find().sort("date", -1)
    art_list = []
    for item in arts:
        art = article.Article()
        art.title = item["title"]
        art.date = item["date"]
        art.tags = item["tags"]
        art.digest = item["digest"]
        art.body = item["body"]
        art_list.append(art)
    return render_template("article_list.html", articles=art_list)


# 根据标题获取博客
@article_page.route("/<title>", methods=["post", "get"])
def get_one(title):
    item = mongo.db.article.find_one({"title": title})
    art = article.Article()
    art.title = item["title"]
    art.date = item["date"]
    art.tags = item["tags"]
    art.digest = item["digest"]
    art.body = item["body"]
    return render_template("article.html", article=art)