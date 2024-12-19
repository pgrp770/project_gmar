from data_management_app.db.sql_db.database import session_maker
from data_management_app.db.sql_db.models import TerrorAttack


def insert_many_generic(model_list):
    with session_maker() as session:

        session.add_all(model_list)
        session.commit()

def get_all_generic(type):
    with session_maker() as session:
        return session.query(type).all()

