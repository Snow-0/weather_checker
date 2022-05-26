import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    API_KEY = os.environ.get("API_KEY") or "no key found"
