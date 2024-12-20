from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country', back_populates='cities', lazy='joined')

    terror_locations = relationship('TerrorLocation', back_populates='city', lazy='dynamic')

    def __repr__(self):
        return f'<City(id={self.id}, name={self.name}, country_id={self.country_id})>'
