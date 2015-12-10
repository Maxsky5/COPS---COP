# -*-coding: utf-8-*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class ConnectDb:
    Base = declarative_base()
    session = sessionmaker()
    host = None
    db_name = None
    username = None
    password = None
    port = None

    def __init__(self, host, db_name, username, password, port=""):
        self.host = host
        self.db_name = db_name
        self.username = username
        self.password = password
        self.port = port
        self.engine = create_engine(
            'mysql://'+self.username +
            ':'+self.password +
            '@'+self.host +
            ':'+self.port +
            '/'+self.db_name,
            echo=True
        )
        self.Base = declarative_base(self.engine)

    def session(self):
        return scoped_session(sessionmaker(bind=self.engine))




