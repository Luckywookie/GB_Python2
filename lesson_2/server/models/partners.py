from models import session, Base
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
        return session.query(PartnerModel.id, PartnerModel.title).filter(PartnerModel.id == _id).first()

    @classmethod
    def find_all(cls):
        return session.query(PartnerModel.id,
                             PartnerModel.title,
                             PartnerModel.comment).all()

    @classmethod
    def find_by_title(cls, search_title):
        return session.query(PartnerModel.id, PartnerModel.title).filter(PartnerModel.title == search_title).first()

    def save_to_db(self):
        session.add(self)
        session.commit()

    @classmethod
    def delete_partner(cls, _id):
        find_partner = session.query(PartnerModel).filter(PartnerModel.id == _id)
        exist_partner = find_partner.first()
        if exist_partner:
            find_partner.delete()
            session.commit()
            print("Element deleted")
        else:
            print("Bad request")

    @classmethod
    def update_partner(cls, _id, new_title, new_comment):
        find_partner = session.query(PartnerModel).filter(PartnerModel.id == _id)
        exist_partner = find_partner.first()
        if exist_partner:
            find_partner.update({'title': new_title, 'comment': new_comment})
            session.commit()
            print("<Partner: {}, comment: {}>".format(new_title, new_comment))
        else:
            print("Bad request")
