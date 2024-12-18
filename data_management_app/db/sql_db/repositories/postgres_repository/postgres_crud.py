from data_management_app.db.sql_db.database import session_maker


def insert_many_generic(model_list):
    with session_maker() as session:
        session.add_all(model_list)
        session.commit()
