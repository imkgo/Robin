# -*- coding: utf-8 -*-

""" 文章
"""

class Article(object):
    """ 文章类
    """
    def __init__(self):
        self.title = None
        self.body = None
        self.date = None
        self.tags = None
        self.digest = None
        self.year = None
        self.month = None
        self.day = None

    @property
    def to_dic(self):
        """ 转为字典
        """
        return {
            "title":self.title,
            "body":self.body,
            "date":self.date,
            "tags":self.tags,
            "digest":self.digest,
            "year":self.year,
            "month":self.month,
            "day":self.day
            }
