from sqlalchemy import Column, Integer, String
from db import Base


class PartnerModel(Base):
    __tablename__ = 'partner'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    comment = Column(String)

    def __init__(self, title, comment=None):
        self.title = title
        self.comment = comment

    def __repr__(self):
        return "<Partner {}>".format(self.title)

