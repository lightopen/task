import os


basedir = os.path.abspath(os.path.dirname(__file__))

# parent class
class Config(object):
    SECRET_KEY = 'demo'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


# design model
class DesignConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'task.sqlite')


config = {'default': DesignConfig}