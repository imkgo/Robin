# -*- coding: utf-8 -*-
import mistune_highlight
import article


def insert(art, mongo):
    mongo.db.article.insert_one(art.to_dic)


def find_article_by_title(title, mongo):
    item = mongo.db.article.find_one({"title": title})
    art = article.Article()
    art.title = item["title"]
    art.date = item["date"]
    art.tags = item["tags"]
    art.digest = item["digest"]
    art.body = item["body"]
    return art


def find_all(mongo):
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
    return art_list


if __name__ == '__main__':
    art = mistune_highlight.get_article("/Users/imkgo/git/github/hexo-repo/source/_posts/使用Python爬取妹子图片.md")
    insert(art)