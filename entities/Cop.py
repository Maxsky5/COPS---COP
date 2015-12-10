# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from dao.ConnectDb import ConnectDb


class Cop(ConnectDb.Base):
    __tablename__ = 'cops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    classroom_id = Column(Integer, ForeignKey('classrooms.id'))
    date_update = Column(DateTime)
    date_last_sync = Column(DateTime)
    check = relationship("Check", backref='cops')
    mac_address = Column(String)