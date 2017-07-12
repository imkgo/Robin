# -*- coding: utf-8 -*-

import sys
from robin import app

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    app.run(debug="enable")
