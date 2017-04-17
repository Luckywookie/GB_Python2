from db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class TerminalModel(Base):
    __tablename__ = 'terminal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    configuration = Column(String)
    title = Column(String)
    pub_key = Column(String)
    comment = Column(String)

    terminal_payment = relationship("PaymentModel", lazy='dynamic')

    def __init__(self, configuration, title, pub_key=None, comment=None):
        self.configuration = configuration
        self.title = title
        self.pub_key = pub_key
        self.comment = comment

    def __repr__(self):
        return "<Terminal {}>".format(self.title)


