import sys

if 'distlib' not in sys.path:
    # import path to libs
    sys.path[0:0] = ['distlib']

import webapp2
import os
from componentae.handler import Traverse
from componentae.util import load_components

# load all components from componentae and app_lib
load_components(['componentae', 'app_lib'])

app = webapp2.WSGIApplication([('(.+)', Traverse)], debug=True)
