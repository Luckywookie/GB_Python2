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

    @classmethod
    def find_by_terminal(cls, terminal_id):
        return cls.query.filter_by(terminal_id=terminal_id).first()

    @classmethod
    def find_by_partner(cls, partner_id):
        return cls.query.filter_by(partner_id=partner_id).first()

    def save_to_db(self):
        Base.add(self)
        Base.commit()

    def delete_from_db(self):
        Base.delete(self)
        Base.commit()
