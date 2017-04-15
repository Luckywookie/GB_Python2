from sqlalchemy import Column, Integer, DateTime, ForeignKey
from db import Base


class PaymentModel(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)
    terminal_id = Column(Integer, ForeignKey('terminal.id'))
    transaction_id = Column(Integer)
    partner_id = Column(Integer, ForeignKey('partner.id'))
    summ = Column(Integer)

    def __init__(self, datetime, terminal_id, transaction_id, partner_id=None, summ=None):
        self.datetime = datetime
        self.terminal_id = terminal_id
        self.transaction_id = transaction_id
        self.partner_id = partner_id
        self.summ = summ

    def json(self):
        return {
            'id': self.id,
            'datetime': self.datetime,
            'terminal_id': self.terminal_id
        }


