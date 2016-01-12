# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from dao.ConnectDb import ConnectDb


class Grade(ConnectDb.Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    date_update = Column(DateTime)
    offenders = relationship('Offender', passive_updates=False)