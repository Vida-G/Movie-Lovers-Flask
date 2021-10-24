import os 

baseddir = os.path.abspath(os.path.dirname(__file__))

# Gives Flask access to relative filepath regardless of OS.
# Allows outside file/folders to imported as well
# can consider this a 'roadmap' we are giving flask for our operating system 

class Config:

    SECRET_KEY = 'You will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 