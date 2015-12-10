# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from dao.ConnectDb import ConnectDb


class Lesson(ConnectDb.Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('offenders.id'))
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    date = Column(DateTime)
    is_morning = Column(Boolean)
    date_update = Column(DateTime)