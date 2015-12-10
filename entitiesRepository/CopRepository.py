# -*-coding: utf-8-*-
from entities.Cop import Cop
from entities.Offender import Offender
from entities.Classroom import Classroom
from entities.Grade import Grade
from entities.Lesson import Lesson
from dao.ConnectDb import ConnectDb


class CopRepository:

    def __init__(self):
        print("Repo Offender initialized")

    def getById(self, id):
        s = ConnectDb.session()

        cop = s.query(Cop).filter(Cop.id == id).one()
        return cop

    def getByMacWithLesson(self, id):

        s = ConnectDb.session()

        offender = s\
            .query(Offender).select_from(Grade)\
            .filter(Offender.id == id)\
            .join(Offender.grade)\
            .one()

        return offender

    def getByMac(self, mac):

        s = ConnectDb.session()

        cop = s\
            .query(Cop)\
            .filter(Cop.mac_address == mac)\
            .all()
        return cop

    def getByMacAndByLesson(self, mac, idLesson):

        s = ConnectDb.session()

        cop = s\
            .query(Cop)\
            .join(Classroom)\
            .join(Lesson)\
            .filter(Cop.mac_address == mac)\
            .filter(Lesson.id == idLesson)\
            .all()

        return cop
