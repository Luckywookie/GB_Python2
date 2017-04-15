
def search_date(session, model, start_date, end_date):
    query = session.query(model.id, model.datetm).filter(model.datetm.between(start_date, end_date)).all()
    return query


def search_partner_trans(session, model, start_date, end_date):
    query = session.query(model.partner_id, model.summ).\
        filter(model.datetm.between(start_date, end_date)).\
        filter(model.summ > 0).all()
    return query

