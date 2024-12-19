import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_management_app.db.sql_db.models import Base

load_dotenv(verbose=True)

engine = create_engine(os.environ["POSTGRES_URL"])
session_maker = sessionmaker(bind=engine)


def init_db():
    Base.metadata.drop_all(engine)
    print("all tables dropped")
    Base.metadata.create_all(engine)
    print("all tables created")


if __name__ == '__main__':
    init_db()
