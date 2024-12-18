from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttack(Base):
    __tablename__ = 'terror_attacks'
    id = Column(Integer, primary_key=True)

    nationalities = relationship('TerrorAttackNationality', back_populates='terror_attacks')

    groups = relationship('TerrorAttackGroup', back_populates='terror_attacks')

    target_types = relationship('TerrorAttackTargetType', back_populates='terror_attacks')

    attack_types = relationship('TerrorAttackAttackType', back_populates='terror_attacks')

    weapons = relationship('TerrorAttackWeapon', back_populates='terror_attacks')

    terror_locations = relationship('TerrorAttackTerrorLocation', back_populates='terror_attacks')