import os

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost/nbaproject')
SQLALCHEMY_TRACK_MODIFICATIONS = False