# -*- coding: utf-8 -*-
# py -2 -m pip install pygments
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
import article
import codecs
import re


class HighlightRenderer(mistune.Renderer):

    def block_code(self, code, lang=None):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter(linenos=True)
        return highlight(code, lexer, formatter)


renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


def get_article(path):
    art = article.Article()
    with codecs.open(path, "r", "utf-8") as mf:
        mark_txt = mf.read()
        art.title = get_title(mark_txt)
        art.date = get_date(mark_txt)
        art.body = get_body(mark_txt)
        art.tags = get_tags(mark_txt)
        art.digest = get_digest(mark_txt)
    return art


def get_title(text):
    pattern = re.compile("title:\s(.+)[\r\n]")
    match = pattern.match(text)
    if match:
        return match.group(1)
    else:
        return ""


def get_date(text):
    pattern = re.compile(r"date:\s(.+)[\r\n]")
    t = re.search(pattern, text)
    if t:
        return t.groups()[0]
    else:
        return ""


def get_body(text):
    pattern = re.compile(r"---")
    return markdown(re.split(pattern, text)[1])


def get_digest(text):
    pattern = re.compile(r"---|\<\!-- more --\>")
    return markdown(re.split(pattern, text)[1])


def get_tags(text):
    pattern = re.compile(r"tags:\s\[(.+)\]")
    rs = re.search(pattern, text)
    if rs:
        tags = rs.groups()[0]
        return re.split(",", tags)

    return []


