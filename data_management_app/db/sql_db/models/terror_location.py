from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorLocation(Base):
    __tablename__ = 'terror_locations'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)

    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship('City', backref='regions')

    terror_attacks = relationship('TerrorAttackWeapon', back_populates='terror_location')
