from sqlalchemy import Column, Integer, DateTime, ForeignKey
from db import Base, session
from datetime import datetime, date


class PaymentModel(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    datetm = Column(DateTime)
    terminal_id = Column(Integer, ForeignKey('terminal.id'))
    transaction_id = Column(Integer)
    partner_id = Column(Integer, ForeignKey('partner.id'))
    summ = Column(Integer)

    def __init__(self, datetm, terminal_id, transaction_id, partner_id=None, summ=None):
        self.datetm = datetm
        self.terminal_id = terminal_id
        self.transaction_id = transaction_id
        self.partner_id = partner_id
        self.summ = summ

    def json(self):
        return {
            'id': self.id,
            'datetime': self.datetm,
            'terminal_id': self.terminal_id
        }

    def __repr__(self):
        return "<Payment {}, Data {}, PartnerID {}, Cash {} руб>".format(self.id, self.datetm, self.partner_id, self.summ)

    @classmethod
    def find_by_id(cls, _id):
        return session.query(PaymentModel.id, PaymentModel.title).filter(PaymentModel.id == _id).first()

    @classmethod
    def find_all(cls):
        return session.query(PaymentModel.id, PaymentModel.datetm, PaymentModel.terminal_id, PaymentModel.transaction_id).all()

    @classmethod
    def find_by_terminal_id(cls, search_terminal):
        return session.query(PaymentModel.transaction_id, PaymentModel.title).\
            filter(PaymentModel.terminal_id == search_terminal).first()

    # поиск транвакций в диапазоне дат
    @classmethod
    def find_by_dates(cls, start_date, end_date):
        return session.query(PaymentModel.id, PaymentModel.datetm).\
            filter(PaymentModel.datetm.between(start_date, end_date)).all()

    # поиск в диапазоне дат партнеров, которым должны денег
    @classmethod
    def find_partner_money(cls, start_date, end_date):
        return session.query(PaymentModel.partner_id, PaymentModel.summ).\
            filter(PaymentModel.datetm.between(start_date, end_date)).\
            filter(PaymentModel.summ > 0).all()

    def save_to_db(self):
        session.add(self)
        session.commit()


