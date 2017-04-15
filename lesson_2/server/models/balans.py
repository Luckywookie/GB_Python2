from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db import Base
# from sqlalchemy.orm import synonym


class CreditModel(Base):
    __tablename__ = 'credit'
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('partner.id'))
    datetime = Column(DateTime)
    summ = Column(String)

    # id = synonym('ID')


class DebitModel(Base):
    __tablename__ = 'debit'
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('partner.id'))
    datetime = Column(DateTime)
    summ = Column(String)