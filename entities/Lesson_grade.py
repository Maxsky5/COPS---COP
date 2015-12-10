# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from dao.ConnectDb import ConnectDb


class Lesson_grade(ConnectDb.Base):
    __tablename__ = "lessons_grades"

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    lesson = relationship('Lesson', backref="lessons")
    grade_id = Column(Integer, ForeignKey('grades.id'))
    grade = relationship('Grade', backref="grades")