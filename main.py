import pywebio
import tabulate
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from datetime import date, timedelta, datetime
from tinydb import TinyDB, Query
from functools import partial
import time
import re
import argparse
import json

from  pywebio.pin import *
import pywebio.output as out

app = Flask(__name__)

# Initialize Flask object

# Initialize TinyDB




import urllib.request, json

#db = TinyDB('/Users/mac/Desktop/db.json')

import requests
import requests

import json




def welcome():



    clear()

  
    put_text("")




    # Choose from either login or signup
    choose_onboarding = actions('', ['دخول', 'تسجيل'],
                                help_text='Choose one of the options to proceed.')
# if __name__ == '__main__':
#     pywebio.start_server(welcome, port=7171)


# app.add_url_rule('/booking', 'webio_view', webio_view(welcome), methods=['GET', 'POST', 'OPTIONS'])


# app.run(host='localhost', port=80)




