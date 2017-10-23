# coding=utf-8
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


'''
you can define other config class in here
'''


config = {'default': Config}
