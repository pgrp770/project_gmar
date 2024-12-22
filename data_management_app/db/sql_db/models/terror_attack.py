from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttack(Base):

    __tablename__ = 'terror_attacks'

    id = Column(Integer, primary_key=True)

    date = Column(DateTime)
    kills = Column(Integer)
    wounds = Column(Integer)
    summary = Column(String)
    terrorist_amount = Column(Integer)

    terror_location_id = Column(Integer, ForeignKey("terror_locations.id"))
    terror_location = relationship('TerrorLocation', back_populates='terror_attacks')

    nationalities = relationship('TerrorAttackNationality', back_populates='terror_attacks')
    groups = relationship('TerrorAttackGroup', back_populates='terror_attacks')
    target_types = relationship('TerrorAttackTargetType', back_populates='terror_attacks')
    attack_types = relationship('TerrorAttackAttackType', back_populates='terror_attacks')
    weapons = relationship('TerrorAttackWeapon', back_populates='terror_attacks')

    def __repr__(self):
        return f"<TerrorAttack=(id-{self.id}, date-{self.date}, kills-{self.kills}, wounds-{self.wounds}, terrorist-{self.terrorist_amount}, location-{self.terror_location_id})>"
