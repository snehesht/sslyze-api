from sqlalchemy import Column, Integer, String, DateTime
from sslyze_api.database import Base
import bcrypt
import datetime
import os
import binascii


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(32), index=True, unique=True)
    password = Column(String(256))
    email = Column(String(128), unique=True)
    created = Column(DateTime)
    updated = Column(DateTime)

    token = Column(String(32), unique=True)
    token_created = Column(DateTime)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = self.hash_password(password)
        self.created = datetime.datetime.now()


    def __repr__(self):
        return '<User {0}>'.format(self.username)

    # Convert plaintext password to oneway hash
    def hash_password(self, password):
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(8))
        return password_hash

    # Check if the hash of plaintext password matches with hashed password
    def verify_password(self, password):
        if bcrypt.hashpw(password.encode(), self.password.encode()) == self.password:
            return True
        else:
            return False

    # Create New Token
    def create_token(self):
        # 32 Char token
        self.token = binascii.hexlify(os.urandom(16))
        self.token_created = datetime.datetime.now()
        return self.token

    # Get token
    def get_token(self):
        return self.token



