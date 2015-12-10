# -*-coding: utf-8-*-
from entities import entities
from dao import ConnectDb

class CheckRepository:
    connectDb = None

    def __init__(self):
        self.connectDb = ConnectDb.ConnectDb('localhost', 'dbcops', 'root', '', '3306')

    def add(self, check):

        session = self.connectDb.session()
        s = session()
        s.add(check)
        s.commit()
        print "checked !"
