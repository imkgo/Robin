# -*- coding: utf-8 -*-
from pymongo import MongoClient
import mistune_highlight
import article


client = MongoClient('localhost', 27017)

db = client['robin']

article_col = db.article


def insert(art):
    article_col.insert_one(art.to_dic)


def find_article_by_title(title):
    art = article_col.find_one_and_delete({"title": title})


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
