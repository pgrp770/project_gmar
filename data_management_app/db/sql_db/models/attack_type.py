from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class AttackType(Base):
    __tablename__ = 'attack_types'
    id = Column(Integer, primary_key=True)
    target_type_name = Column(String)

    terror_attacks = relationship('TerrorAttackTargetType', back_populates='target_type')
