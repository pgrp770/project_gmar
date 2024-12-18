from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    country_name = Column(String)

    region_id = Column(Integer, ForeignKey('regions.id'))
    region = relationship('Region', back_populates='countries')

    cities = relationship('City', back_populates='country')