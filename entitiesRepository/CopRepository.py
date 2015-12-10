# -*-coding: utf-8-*-
from entities import entities
from dao import ConnectDb


class CopRepository:
    connectDb = None

    def __init__(self):
        self.connectDb = ConnectDb.ConnectDb('localhost', 'dbcops', 'root', '', '3306')

        print("Repo Offender initialized")

    def getById(self, id):
        session = self.connectDb.session()
        s = session()

        cop = s.query(entities.Cop).filter(entities.Cop.id == id).one()
        return cop

    def getByMacWithLesson(self, id):

        session = self.connectDb.session()
        s = session()

        offender = s\
            .query(entities.Offender).select_from(entities.Grade)\
            .filter(entities.Offender.id == id)\
            .join(entities.Offender.grade)\
            .one()

        return offender

    def getByMac(self, mac):

        session = self.connectDb.session()
        s = session()

        cop = s\
            .query(entities.Cop)\
            .filter(entities.Cop.mac_address == mac)\
            .all()
        return cop

    def getByMacAndByLesson(self, mac, idLesson):

        session = self.connectDb.session()
        s = session()

        cop = s\
            .query(entities.Cop)\
            .join(entities.Classroom)\
            .join(entities.Lesson)\
            .filter(entities.Cop.mac_address == mac)\
            .filter(entities.Lesson.id == idLesson)\
            .all()

        return cop






