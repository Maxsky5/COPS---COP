# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, backref
from dao.ConnectDb import ConnectDb


class Cop(ConnectDb.Base):
    __tablename__ = 'cops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    classroom_id = Column(Integer, ForeignKey('classrooms.id', onupdate="cascade"))
    classroom = relationship("Classroom", passive_updates=False)
    date_update = Column(DateTime)
    date_last_sync = Column(DateTime)
    check = relationship("Check", backref='cops')
    mac_address = Column(String)
