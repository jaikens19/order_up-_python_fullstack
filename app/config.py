import os

class Configuration:
    SQLALCHEMY_DATABASE_URI = 'postgresql://order_up:9uCxydbt@localhost/order_up_dev'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SECRET_KEY = os.environ.get('SECRET_KEY')
