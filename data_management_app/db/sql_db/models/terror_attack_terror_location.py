from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttackTerrorLocation(Base):
    __tablename__ = 'terror_attack_terror_location'
    id = Column(Integer, primary_key=True)

    terror_location_id = Column(Integer, ForeignKey('terror_locations.id'))
    terror_location = relationship('TerrorLocation', back_populates='terror_attacks', lazy='joined')

    terror_attack_id = Column(Integer, ForeignKey('terror_attacks.id'))
    terror_attacks = relationship('TerrorAttack', back_populates='terror_locations', lazy='joined')

    def __repr__(self):
        return f"'{self.terror_attack_id}, {self.terror_location_id}'"