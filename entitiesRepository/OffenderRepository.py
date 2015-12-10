# -*-coding: utf-8-*-
from entities import entities
from dao import ConnectDb
import LessonRepository


class OffenderRepository:
    connectDb = None

    def __init__(self):
        self.connectDb = ConnectDb.ConnectDb('localhost', 'dbcops', 'root', '', '3306')

        print("Repo Offender initialized")

    def getById(self, id):
        session = self.connectDb.session()
        s = session()

        offender = s.query(entities.Offender).filter(entities.Offender.id == id).all()

        return offender

    def getByIdWithGrade(self, id):

        session = self.connectDb.session()
        s = session()

        offender = s\
            .query(entities.Offender).select_from(entities.Grade)\
            .filter(entities.Offender.id == id)\
            .join(entities.Offender.grade)\
            .one()

        return offender

    def getByLesson(self, idLesson):
        session = self.connectDb.session()
        s = session()

        offender = s\
            .query(entities.Offender).select_from(entities.Grade)\
            .filter(entities.Offender.id == id)\
            .join(entities.Offender.grade)\
            .one()






