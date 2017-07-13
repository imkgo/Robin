# -*- coding: utf-8 -*-
""" 文章页面逻辑处理
"""

from flask import render_template, Blueprint, request, redirect

from robin import MONGO
from robin.models import article
from robin.extensions import mistune_highlight

ARTICLE_PAGE = Blueprint("article_page", __name__, template_folder="templates")


@ARTICLE_PAGE.route('/')
def index():
    """ 首页
    """
    arts = MONGO.db.article.find().sort("date", -1)
    art_list = []
    for item in arts:
        art_list.append(article.article_from_dic(item))

    return render_template("article_list.html", articles=art_list, github="https://github.com/imkgo")


@ARTICLE_PAGE.route("/<year>/<month>/<day>/<title>", methods=["get"])
def get_one(year, month, day, title):
    """ 根据标题获取博客
    """
    item = MONGO.db.article.find_one({"year": int(year), "month": int(month), "day": int(day), "title": title})
    art = article.article_from_dic(item)
    return render_template("article.html", article=art)
