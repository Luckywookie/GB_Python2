from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.partners import PartnerModel
from models.payments import PaymentModel
from models.terminals import TerminalModel
from models.balans import CreditModel, DebitModel

from db import Base

# metadata = MetaData()
# Session = sessionmaker()

engine = create_engine('sqlite:///data.db', echo=True)

# conn = engine.connect()
# trans = conn.begin()

Base.metadata.create_all(engine)

# print(Base.metadata.tables.items())

Session = sessionmaker(bind=engine)
session = Session()

now = datetime.now()

t1 = TerminalModel(configuration=123, title='Black terminal')
p1 = PartnerModel(title='Firma OOO')
tr1 = PaymentModel(datetime=now, terminal_id=1, transaction_id=1, partner_id=1, summ=123456)

session.add(t1)
session.add(p1)
session.add(tr1)
session.commit()
