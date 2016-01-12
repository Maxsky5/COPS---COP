# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String
from sqlalchemy.orm import relationship
from dao.ConnectDb import ConnectDb


class Lesson(ConnectDb.Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('offenders.id'))
    offender = relationship("Offender", backref='offenders')
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    classroom = relationship("Classroom", back_populates="lessons")
    date = Column(DateTime)
    is_morning = Column(Boolean)
    date_update = Column(DateTime)