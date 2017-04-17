from datetime import datetime, date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.partners import PartnerModel
from models.payments import PaymentModel
from models.terminals import TerminalModel
from models.balans import CreditModel, DebitModel
from select_data import search_date, search_partner_trans

from db import Base

engine = create_engine('sqlite:///data.db', echo=True)
Base.metadata.create_all(engine)

Sess = sessionmaker(bind=engine)
session = Sess()

# поиск транвакций в диапазоне дат
print(search_date(session, PaymentModel, date(2011, 3, 5), date(2019, 3, 5)))

# поиск в диапазоне дат партнеров, которым должны денег
print(search_partner_trans(session, PaymentModel, date(2011, 3, 5), date(2019, 3, 5)))

# join
# print(session.query(PaymentModel, PartnerModel).join(PartnerModel, PaymentModel.partner_id == PartnerModel.id).all())


# t1 = TerminalModel(configuration=1258, title='Grey terminal')
# p1 = PartnerModel(title='Lakomka OOO')
# tr1 = PaymentModel(datetm=date(2015, 12, 15), terminal_id=7, transaction_id=15, partner_id=7, summ=152856)

# session.add(t1)
# session.add(p1)
# session.add(tr1)
# session.commit()
