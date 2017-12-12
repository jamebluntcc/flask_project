# coding=utf-8
import os


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(os.path.join(__file__, 'app')))
    PROJECT_DIR = os.path.join(APP_DIR, os.pardir)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_DIR, DB_NAME)
    DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    DATABASE = os.environ.get('DATABASE', 'r')
    HOST = os.environ.get('HOST', 'localhost')
    PASSWD = os.environ.get('PASSWD', '050400')
    USER = os.environ.get('USER', 'jamebluntcc')
    DATABASE_URI = 'mysql://{user}:{passwd}@{host}/{database}'.format(
        user=USER,
        passwd=PASSWD,
        host=HOST,
        database=DATABASE
    )


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE_URI = 'sqlite://'


'''
you can define other config class in here
'''


config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
    }
