from data_management_app.db.sql_db.database import session_maker


def insert_many_generic(model_list):
    with session_maker() as session:
        session.add_all(model_list)
        session.commit()
        print(f"many {type(model_list[0])} was inserted")


def get_all_generic(sql_model):
    with session_maker() as session:
        return session.query(sql_model).all()
