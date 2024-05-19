import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://<username>:<password>@localhost/uav_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
