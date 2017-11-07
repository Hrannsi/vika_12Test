import os
from bottle import *


@route('/')
def index():
    return "<h1>Well Hello There</h1>"


run(host='0.0.0.0', port=os.environ.get('PORT'))