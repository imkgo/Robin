# -*- coding: utf-8 -*-
from pymongo import MongoClient
import mistune_highlight
import article
from flask import current_app

client = MongoClient(current_app.config.get("db_host"), current_app.config.get("db_port"))

db = client[current_app.config.get("db_name")]
db.authenticate(current_app.config.get("db_user"), current_app.config.get("db_pwd"))

article_col = db.article


def insert(art):
    article_col.insert_one(art.to_dic)


def find_article_by_title(title):
    item = article_col.find_one({"title": title})
    art = article.Article()
    art.title = item["title"]
    art.date = item["date"]
    art.tags = item["tags"]
    art.digest = item["digest"]
    art.body = item["body"]
    return art


def find_all():
    arts = article_col.find().sort("date", -1)
    art_list = []
    for item in arts:
        art = article.Article()
        art.title = item["title"]
        art.date = item["date"]
        art.tags = item["tags"]
        art.digest = item["digest"]
        art.body = item["body"]
        art_list.append(art)
    return art_list


if __name__ == '__main__':
    art = mistune_highlight.get_article("/Users/imkgo/git/github/hexo-repo/source/_posts/使用Python爬取妹子图片.md")
    insert(art)