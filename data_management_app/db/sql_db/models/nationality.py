from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class Nationality(Base):
    __tablename__ = 'nationalities'
    id = Column(Integer, primary_key=True)
    nationality = Column(String)

    terror_attacks = relationship('TerrorAttackNationality', backref='nationality')
    # countries = relationship('Country', back_populates='region')