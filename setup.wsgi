import sys

activate_this = '/home/lucho/site/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0,'/home/lucho/site')

from setup import app as application
