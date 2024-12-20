from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class Country(Base):

    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    region_id = Column(Integer, ForeignKey('regions.id'))
    region = relationship('Region', back_populates='countries', lazy='joined')

    cities = relationship('City', back_populates='country', lazy='joined')

    def __repr__(self):
        return f'<Country(id={self.id}, name={self.name}, region_id={self.region_id})>'
