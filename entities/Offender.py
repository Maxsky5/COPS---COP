# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum
from sqlalchemy.orm import relationship
from dao.ConnectDb import ConnectDb


class Offender(ConnectDb.Base):
    __tablename__ = 'offenders'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    grade_id = Column(Integer, ForeignKey('grades.id', onupdate="cascade"))
    grade = relationship('Grade', passive_updates=False)
    check = relationship("Check", backref='offenders')
    lesson = relationship('Lesson', uselist=False, backref='offenders')
    email = Column(String)
    date_update = Column(DateTime)
    type = Column(Enum, default='STUDENT')

    def is_teacher(self):
        if self.type == 'TEACHER':
            return True
        return False
