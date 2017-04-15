from sqlalchemy import Column, Integer, String
from db import Base


class TerminalModel(Base):
    __tablename__ = 'terminal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    configuration = Column(String)
    title = Column(String)
    pub_key = Column(String)
    comment = Column(String)

    # Credit = Base.relationship('CreditModel')

    def __init__(self, configuration, title, pub_key, comment=None):
        self.configuration = configuration
        self.title = title
        self.pub_key = pub_key
        self.comment = comment


