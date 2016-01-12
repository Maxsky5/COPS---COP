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

    def getLessonByGradeAndByDate(self, idGrade, date):
        s = ConnectDb.session()

        lesson = s.query(Lesson)\
            .join(Offender.grade)\
            .join(Lesson_grade)\
            .join(Lesson)\
            .filter(Offender.grade_id == idGrade)\
            .filter(Lesson.date == date)\
            .all()

        return lesson

    def getLessonByTeacherAndByDate(self, idTeacher, date):
        s = ConnectDb.session()

        lesson = s.query(Lesson)\
            .join(Offender.lesson)\
            .filter(Offender.id == idTeacher)\
            .filter(Lesson.date == date)\
            .all()

        return lesson





