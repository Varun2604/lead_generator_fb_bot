import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root@localhost:3306/lead_generator'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SUBSCRIPTION_VERIFICATION_TOKEN = 'verification_token'
    FACEBOOK_ACCESS_TOKEN = os.environ.get('FACEBOOK_ACCESS_TOKEN') or 'your_fb_access_token'