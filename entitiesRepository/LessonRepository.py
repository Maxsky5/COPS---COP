# -*-coding: utf-8-*-
from entities.Offender import Offender
from entities.Lesson_grade import Lesson_grade
from entities.Lesson import Lesson
from dao.ConnectDb import ConnectDb


class LessonRepository:

    def __init__(self):
        print("Repo Lesson initialized")

    def getById(self, id):
        s = ConnectDb.session()

        lesson = s.query(Lesson).filter(Lesson.id == id).one()
        return lesson

    def getByStudy(self, idStudy):
        s = ConnectDb.session()

        lesson = s.query(Lesson)\
            .join(Offender.grade)\
            .join(Lesson_grade)\
            .join(Lesson)\
            .filter(Offender.id == idStudy)\
            .one()

        return lesson

    def getLessonByStudy(self, idStudy):
        s = ConnectDb.session()

        lesson = s.query(Lesson)\
            .join(Offender.grade)\
            .join(Lesson_grade)\
            .join(Lesson)\
            .filter(Offender.id == idStudy)\
            .all()

        return lesson





