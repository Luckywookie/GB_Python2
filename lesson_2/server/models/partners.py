from db import Base, session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class PartnerModel(Base):
    __tablename__ = 'partner'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    comment = Column(String)

    partner_payment = relationship("PaymentModel", lazy='dynamic')

    def __init__(self, title, comment=None):
        self.title = title
        self.comment = comment

    def __repr__(self):
        return "<Partner {}>".format(self.title)

    @classmethod
    def find_by_id(cls, _id):
        return session.query(PartnerModel.title).filter(PartnerModel.id == _id).first()

    def save_to_db(self):
        session.add(self)
        session.commit()
