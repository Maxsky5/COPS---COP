# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from dao import ConnectDb

connectDb = ConnectDb.ConnectDb('root', 'dbcops', 'root', '', '3306')


class Cop(connectDb.Base):
    __tablename__ = 'cops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    date_update = Column(DateTime)
    date_last_sync = Column(DateTime)
    check = relationship("Check", backref='cops')
    mac_address = Column(String)


class Classroom(connectDb.Base):
    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nb_place = Column(Integer)
    cops = relationship("Cop", backref='classrooms')
    lesson = relationship("Lesson", uselist=False, backref='classrooms')


class Lesson(connectDb.Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('offenders.id'))
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    date = Column(DateTime)
    is_morning = Column(Boolean)
    date_update = Column(DateTime)


class Lesson_grade(connectDb.Base):
    __tablename__ = "lessons_grades"

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    lesson = relationship('Lesson', backref="lessons")
    grade_id = Column(Integer, ForeignKey('grades.id'))
    grade = relationship('Grade', backref="grades")


class Grade(connectDb.Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    date_update = Column(DateTime)
    offenders = relationship('Offender')


class Offender(connectDb.Base):
    __tablename__ = 'offenders'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    grade_id = Column(Integer, ForeignKey('grades.id'))
    grade = relationship('Grade')
    check = relationship("Check", backref='offenders')
    lesson = relationship('Lesson', uselist=False, backref='offenders')
    email = Column(String)
    date_update = Column(DateTime)
    type = Column(Enum, default=1)

    def is_teacher(self):
        if self.type == 'teacher':
            return True
        return False


class Check(connectDb.Base):
    __tablename__ = 'checks'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    offender_id = Column(Integer, ForeignKey('offenders.id'))
    offender = relationship('Offender')
    cop_id = Column(Integer, ForeignKey('cops.id'))
    cop = relationship("Cop")

