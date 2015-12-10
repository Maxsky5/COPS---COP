# -*-coding: utf-8-*-
from entities.Offender import Offender
from entities.Grade import Grade
from dao.ConnectDb import ConnectDb


class OffenderRepository:

    def __init__(self):

        print("Repo Offender initialized")

    def getById(self, id):
        s = ConnectDb.session()

        offender = s.query(Offender).filter(Offender.id == id).all()

        return offender

    def getByIdWithGrade(self, id):

        s = ConnectDb.session()

        offender = s\
            .query(Offender).select_from(Grade)\
            .filter(Offender.id == id)\
            .join(Offender.grade)\
            .one()

        return offender

    def getByLesson(self, idLesson):
        s = ConnectDb.session()

        offender = s\
            .query(Offender).select_from(Grade)\
            .filter(Offender.id == id)\
            .join(Offender.grade)\
            .one()






