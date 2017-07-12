# -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, redirect

from robin import mongo
from robin.models import article
from robin.extensions import mistune_highlight

ARTICLE_PAGE = Blueprint("article_page", __name__, template_folder="templates")

@ARTICLE_PAGE.route('/')
def index():
    """ 首页
    """
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
    return render_template("article_list.html", articles=art_list, github="https://github.com/imkgo")


@ARTICLE_PAGE.route("/<title>", methods=["get"])
def get_one(title):
    """ 根据标题获取博客
    """
    item = mongo.db.article.find_one({"title": title})
    art = article.Article()
    art.title = item["title"]
    art.date = item["date"]
    art.tags = item["tags"]
    art.digest = item["digest"]
    art.body = item["body"]
    return render_template("article.html", article=art)


# 上传页面
@ARTICLE_PAGE.route("/upload")
def upload():
    return render_template("upload_blog.html")


# 博客上传
@ARTICLE_PAGE.route("/upload_article", methods=["post"])
def upload_article():
    article_file = request.files['file']
    if article_file:
        article_str = article_file.read()
        article_obj = mistune_highlight.artilce(article_str)
        temp_obj = mongo.db.article.find_one({"title":article_obj.title})
        if temp_obj:
            mongo.db.article.update_one({"title":article_obj.title}, {"$set":article_obj.to_dic})
        else:
            mongo.db.article.insert_one(article_obj.to_dic)
    return redirect("/")
