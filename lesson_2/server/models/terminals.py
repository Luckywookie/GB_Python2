from db import Base, session
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

    @classmethod
    def find_by_id(cls, _id):
        return session.query(TerminalModel.id, TerminalModel.title).filter(TerminalModel.id == _id).first()

    @classmethod
    def find_all(cls):
        return session.query(TerminalModel.id, TerminalModel.title).all()

    @classmethod
    def find_by_title(cls, search_title):
        return session.query(TerminalModel.id, TerminalModel.title).filter(TerminalModel.title == search_title).first()

    @classmethod
    def find_by_pub_key(cls, search_pub_key):
        return session.query(TerminalModel.id, TerminalModel.title).filter(TerminalModel.pub_key == search_pub_key).first()

    def save_to_db(self):
        session.add(self)
        session.commit()

    @classmethod
    def delete_terminal(cls, _id):
        find_terminal = session.query(TerminalModel).filter(TerminalModel.id == _id)
        exist_terminal = find_terminal.first()
        if exist_terminal:
            find_terminal.delete()
            session.commit()
            print("Terminal deleted")
        else:
            print("Bad request")

    @classmethod
    def update_terminal(cls, _id, new_title):
        find_terminal = session.query(TerminalModel).filter(TerminalModel.id == _id)
        exist_terminal = find_terminal.first()
        if exist_terminal:
            find_terminal.update({'title': new_title})
            session.commit()
            print("<Terminal: {}>".format(new_title))
        else:
            print("Bad request")
