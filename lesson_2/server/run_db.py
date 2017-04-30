# from db import Base, session
from datetime import datetime, date

from models.partners import PartnerModel
from models.payments import PaymentModel
from models.terminals import TerminalModel
from models.balans import CreditModel, DebitModel

# удаление партнеров по id
# PartnerModel.delete_partner(10)

print(PaymentModel.find_all())
# изменение партнеров по id его title и comments
# PartnerModel.update_partner(4, "My OOO", "Ohoho")

# partner = PartnerModel(title='My Good Firm OOO', comment='Very looong comment')
# partner.save_to_db()

print(PartnerModel.find_all())

# print(PartnerModel.find_by_title('Ogogo OOO'))

# terminal = TerminalModel(configuration=125258, title='Little terminal')
# terminal.save_to_db()

# поиск транвакций в диапазоне дат
# print(PaymentModel.find_by_dates(date(2011, 3, 5), date(2019, 3, 5)))

# поиск в диапазоне дат партнеров, которым должны денег
# print(PaymentModel.find_partner_money(date(2011, 3, 5), date(2019, 3, 5)))

# join
# print(session.query(PaymentModel, PartnerModel).join(PartnerModel, PaymentModel.partner_id == PartnerModel.id).all())


# transaction = PaymentModel(datetm=date(2016, 11, 30), terminal_id=7, transaction_id=15, partner_id=7, summ=152006)
# transaction.save_to_db()
