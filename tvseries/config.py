import os
from decouple import config


class BaseConfig(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SITE_NAME = 'NPS Platform'
    SECRET_KEY = config('SECRET_KEY')
    SERVER_NAME = config('SERVER_NAME')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    COLLECT_STATIC_ROOT = os.path.join(BASE_DIR, "static")
    COLLECT_STORAGE = 'flask_collect.storage.file'
    WTF_CSRF_ENABLED = True
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tvseries.sqlite3'
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    pass
