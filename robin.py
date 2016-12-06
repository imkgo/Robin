# -*- coding: utf-8 -*-

from flask import Flask, render_template
import mistune_highlight
app = Flask(__name__)


@app.route('/')
def hello_world():
    arts = []
    art1 = mistune_highlight.get_article(u"E:/git/github/hexo-repo/source/_posts/Hexo搭建Github静态博客.md")
    art2 = mistune_highlight.get_article(u"E:/git/github/hexo-repo/source/_posts/Python每日同步Bing桌面.md")
    arts.append(art1)
    arts.append(art2)
    return render_template("index.html", articles=arts)


@app.route("/ethan")
def hello():
    return "<h1>Hello, eth11an!</h1>"


@app.route("/<user_name>")
def hello1(user_name):
    return "<h1>Hello, %s!</h1>" % user_name


if __name__ == '__main__':
    app.run(debug="enable")
