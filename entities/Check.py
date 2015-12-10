# -*-coding: utf-8-*-
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from dao.ConnectDb import ConnectDb

class Check(ConnectDb.Base):
    __tablename__ = 'checks'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    offender_id = Column(Integer, ForeignKey('offenders.id'))
    offender = relationship('Offender')
    cop_id = Column(Integer, ForeignKey('cops.id'))
    cop = relationship("Cop")