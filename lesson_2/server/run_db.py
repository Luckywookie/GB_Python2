from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from models.partners import PartnerModel
from models.payments import PaymentModel
from models.terminals import TerminalModel
from models.balans import CreditModel, DebitModel

from db import Base

# metadata = MetaData()
# Session = sessionmaker()

engine = create_engine('sqlite:///data.db', echo=True)

conn = engine.connect()
trans = conn.begin()

Base.metadata.create_all(engine)
