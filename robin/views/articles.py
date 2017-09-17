# -*- coding: utf-8 -*-
""" 文章页面逻辑处理
"""

from flask import render_template, Blueprint

from robin import MONGO
from robin.models.article import Article
import logging
import datetime

ARTICLE_PAGE = Blueprint("article_page", __name__, template_folder="templates")


@ARTICLE_PAGE.route('/')
def index():
    """ 首页
    """
    arts = MONGO.db.article.find().sort("date", -1)
    art_list = []
    for item in arts:
        blog = Article.article_from_dic(item)

        art_list.append(blog)


    return render_template("article_list.html",
                           articles=art_list, github="https://github.com/imkgo")


@ARTICLE_PAGE.route("/<year>/<month>/<day>/<title>", methods=["get"])
def get_one(year, month, day, title):
    """ 根据标题获取博客
    """
    item = MONGO.db.article.find_one({"year": int(year),
                                     "month": int(month), "day": int(day), "title": title})
    date = item["date"]
    art = Article.article_from_dic(item)
    next_blogs = MONGO.db.article.find({"date": {"$lt": date}}).sort("date", -1).limit(1)
    for blog in next_blogs:
        art.next_article = Article.article_from_dic(blog)

    pre_blogs = MONGO.db.article.find({"date": {"$gt": date}}).sort("date", 1).limit(1)
    for pre_blog in pre_blogs:
        art.pre_article = Article.article_from_dic(pre_blog)
    return render_template("article.html", article=art)
