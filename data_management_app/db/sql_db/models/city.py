from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    city_name = Column(String)

    country_id = Column(Integer, ForeignKey('regions.id'))
    country = relationship('Country', back_populates='cities')

    terror_locations = relationship('TerrorLocation', back_populates='city')