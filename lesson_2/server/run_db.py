from datetime import datetime, date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.partners import PartnerModel
from models.payments import PaymentModel
from models.terminals import TerminalModel
from models.balans import CreditModel, DebitModel
from select_data import search_date, search_partner_trans

from db import Base, session

# удаление партнеров по id
PartnerModel.delete_partner(10)
PartnerModel.update_partner(4, "My OOO", "Ohoho")
# partner = PartnerModel(title='Ogogo OOO')
# partner.delete_from_db()

# print(PartnerModel.find_by_title('Ogogo OOO'))


# terminal = TerminalModel(configuration=125258, title='Little terminal')
# terminal.save_to_db()

# поиск транвакций в диапазоне дат
# print(search_date(session, PaymentModel, date(2011, 3, 5), date(2019, 3, 5)))
# print(PaymentModel.find_by_dates(date(2011, 3, 5), date(2019, 3, 5)))

# поиск в диапазоне дат партнеров, которым должны денег
# print(search_partner_trans(session, PaymentModel, date(2011, 3, 5), date(2019, 3, 5)))
# print(PaymentModel.find_partner_money(date(2011, 3, 5), date(2019, 3, 5)))

# join
# print(session.query(PaymentModel, PartnerModel).join(PartnerModel, PaymentModel.partner_id == PartnerModel.id).all())


# transaction = PaymentModel(datetm=date(2016, 11, 30), terminal_id=7, transaction_id=15, partner_id=7, summ=152006)
# transaction.save_to_db()

# session.add(t1)
# session.add(p1)
# session.add(tr1)
# session.commit()
