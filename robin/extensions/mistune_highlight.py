# -*- coding: utf-8 -*-
# py -2 -m pip install pygments
""" markdown文本转为html文本以及代码高亮
"""
import codecs
import re
from datetime import datetime
import mistune
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name

from robin.models import article


class HighlightRenderer(mistune.Renderer):
    """ 代码高亮
    """
    def block_code(self, code, lang=None):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter(linenos=True)
        return highlight(code, lexer, formatter)


RENDERER = HighlightRenderer()
MARKDOWN = mistune.Markdown(renderer=RENDERER)


def get_article(path):
    """ 根据文章路径获取文章对象
    """
    art = article.Article()
    with codecs.open(path, "r", "utf-8") as mf:
        mark_txt = mf.read()
        art.title = get_title(mark_txt)
        art.date = get_date(mark_txt)
        art.body = get_body(mark_txt)
        art.tags = get_tags(mark_txt)
        art.digest = get_digest(mark_txt)
        art.year, art.month, art.day = get_year_month_day(art.date)
    return art


def artilce(article_str):
    art = article.Article()
    art.title = get_title(article_str)
    art.date = get_date(article_str)
    art.body = get_body(article_str)
    art.tags = get_tags(article_str)
    art.digest = get_digest(article_str)
    art.year, art.month, art.day = get_year_month_day(art.date)
    return art


def get_title(text):
    """ 获取标题
    """
    pattern = re.compile("title:\s(.+)[\r\n]")
    match = pattern.match(text)
    if match:
        return match.group(1)
    else:
        return ""


def get_date(text):
    """ 获取日期
    """
    pattern = re.compile(r"date:\s(.+)[\r\n]")
    t = re.search(pattern, text)
    if t:
        return t.groups()[0]
    else:
        return ""


def get_body(text):
    """ 获取body
    """
    pattern = re.compile(r"---")
    return MARKDOWN(re.split(pattern, text)[1])


def get_digest(text):
    """ 获取摘要
    """
    pattern = re.compile(r"---|\<\!-- more --\>")
    return MARKDOWN(re.split(pattern, text)[1])


def get_tags(text):
    """ 获取标签
    """
    pattern = re.compile(r"tags:\s\[(.+)\]")
    rs = re.search(pattern, text)
    if rs:
        tags = rs.groups()[0]
        return re.split(",", tags)

    return []

def get_year_month_day(date):
    """ 获取年份和月份
    日期格式为：2016-12-31 14:47:07
    """
    article_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return article_date.year, article_date.month, article_date.day
