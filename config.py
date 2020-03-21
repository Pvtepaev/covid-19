import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    HOST = '0.0.0.0'
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'you-ill-ever-guess'