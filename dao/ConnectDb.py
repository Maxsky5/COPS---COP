# -*-coding: utf-8-*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ConfigParser

class ConnectDb(object):
    Base = declarative_base()
    engine = None
    Session = None
    host = None
    db_name = None
    username = None
    password = None
    port = None

    @staticmethod
    def session():
        #if ConnectDb.engine is None:
        config = ConfigParser.ConfigParser()
        config.read("../config.ini")
        ConnectDb.host = config.get('database', 'host')
        ConnectDb.db_name = config.get('database', 'dbname')
        ConnectDb.username = config.get('database', 'username')
        ConnectDb.password = config.get('database', 'password')
        ConnectDb.port = config.get('database', 'port')
        ConnectDb.engine = create_engine(
            'mysql://'+ConnectDb.username +
            ':'+ConnectDb.password +
            '@'+ConnectDb.host +
            ':'+ConnectDb.port +
            '/'+ConnectDb.db_name,
            echo=True
        )
        ConnectDb.Session = sessionmaker(bind=ConnectDb.engine)

        return ConnectDb.Session()
