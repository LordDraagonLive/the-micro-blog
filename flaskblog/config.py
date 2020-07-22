import os

class Config():
    
    SECRET_KEY = 'c467bb47a41bbbd46ed1fd11c0842a09445eade8a51c5213095b7e5756b035f6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('LIVE_MAIL_USER')
    MAIL_PASSWORD = os.environ.get('LIVE_MAIL_PASS')

    