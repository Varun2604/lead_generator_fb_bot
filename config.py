import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root@localhost:3306/lead_generator'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SUBSCRIPTION_VERIFICATION_TOKEN = os.environ.get('SUBSCRIPTION_VERIFICATION_TOKEN')
    FACEBOOK_ACCESS_TOKEN = os.environ.get('FACEBOOK_ACCESS_TOKEN')
    FACEBOOK_MESSAGE_API='https://graph.facebook.com/v2.6/me/messages'
    DIALOG_FLOW_PROJECT_ID = os.environ.get('DIALOG_FLOW_PROJECT_ID')