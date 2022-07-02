import os

class Config(object):
    SECRET_KEY = 'super_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True