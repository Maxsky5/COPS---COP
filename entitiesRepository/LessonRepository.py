# -*-coding: utf-8-*-
from entities import entities
from dao import ConnectDb


class LessonRepository:
    connectDb = None

    def __init__(self):
        self.connectDb = ConnectDb.ConnectDb('localhost', 'dbcops', 'root', '', '3306')
        print("Repo Lesson initialized")

    def getById(self, id):
        session = self.connectDb.session()
        s = session()

        lesson = s.query(entities.Lesson).filter(entities.Lesson.id == id).one()
        return lesson

    def getByStudy(self, idStudy):
        session = self.connectDb.session()
        s = session()

        lesson = s.query(entities.Lesson)\
            .join(entities.Offender.grade)\
            .join(entities.Lesson_grade)\
            .join(entities.Lesson)\
            .filter(entities.Offender.id == idStudy)\
            .one()

        return lesson

    def getLessonByStudy(self, idStudy):
        session = self.connectDb.session()
        s = session()

        lesson = s.query(entities.Lesson)\
            .join(entities.Offender.grade)\
            .join(entities.Lesson_grade)\
            .join(entities.Lesson)\
            .filter(entities.Offender.id == idStudy)\
            .all()

        return lesson





