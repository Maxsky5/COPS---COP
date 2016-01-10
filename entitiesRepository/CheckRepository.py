# -*-coding: utf-8-*-
from entities.Check import Check
from dao.ConnectDb import ConnectDb

class CheckRepository:

    def __init__(self):
        print("Repo Check initialized")

    def add(self, check):

        s = ConnectDb.session()
        s.add(check)
        s.commit()
        print "checked !"

    def getAll(self):
        s = ConnectDb.session()

        checks = s.query(Check).all()
        return checks
