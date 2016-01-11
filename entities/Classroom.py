# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from dao.ConnectDb import ConnectDb


class Classroom(ConnectDb.Base):
    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nb_place = Column(Integer)
    cops = relationship("Cop", backref='classrooms')
    lesson = relationship("Lesson", uselist=False, backref='classrooms')
    date_update = Column(DateTime)