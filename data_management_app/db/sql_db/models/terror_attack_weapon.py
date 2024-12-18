from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttackWeapon(Base):
    __tablename__ = 'terror_attack_weapons'
    id = Column(Integer, primary_key=True)

    weapon_id = Column(Integer, ForeignKey('weapons.id'))
    weapon_type = relationship('Weapon', back_populates='terror_attacks')

    terror_attack_id = Column(Integer, ForeignKey('terror_attacks.id'))
    terror_attacks = relationship('TerrorAttack', back_populates='weapons')

    # countries = relationship('Country', back_populates='region')