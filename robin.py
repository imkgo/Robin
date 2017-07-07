# -*- coding: utf-8 -*-

from robin import app
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    app.run(debug="enable")
