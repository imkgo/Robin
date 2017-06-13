from json import JSONEncoder


class Article(object):

    def __init__(self):
        pass

    @property
    def to_dic(self):
        return {"title":self.title, "body":self.body, "date":self.date, "tags":self.tags, "digest":self.digest}