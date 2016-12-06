from json import JSONEncoder


class Article(object):

    def __init__(self):
        pass


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
