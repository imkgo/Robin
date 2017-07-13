# -*- coding: utf-8 -*-

""" 程序入口
"""
import sys
from robin import APP
from robin.views.articles import ARTICLE_PAGE

reload(sys)
sys.setdefaultencoding('utf-8')
APP.register_blueprint(ARTICLE_PAGE)

if __name__ == '__main__':
    APP.run(debug="enable")
