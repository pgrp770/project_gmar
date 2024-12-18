from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttackAttackType(Base):
    __tablename__ = 'terror_attack_attack_type_relations'
    id = Column(Integer, primary_key=True)

    attack_type_id = Column(Integer, ForeignKey('attack_types.id'))
    attack_type = relationship('AttackType', back_populates='terror_attacks')

    terror_attack_id = Column(Integer, ForeignKey('terror_attacks.id'))
    terror_attacks = relationship('TerrorAttack', back_populates='attack_types')