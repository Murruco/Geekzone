import os


class Config(object):
    SECRET_KEY = 'super_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/geekzone'
    SQLALCHEMY_TRACK_MODIFICATIONS = False