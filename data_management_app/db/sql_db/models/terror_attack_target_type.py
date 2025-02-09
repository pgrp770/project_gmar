from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttackTargetType(Base):

    __tablename__ = 'terror_attack_target_type_relations'

    id = Column(Integer, primary_key=True)

    target_type_id = Column(Integer, ForeignKey('target_types.id'))
    target_type = relationship('TargetType', back_populates='terror_attacks')
    terror_attack_id = Column(Integer, ForeignKey('terror_attacks.id'))
    terror_attacks = relationship('TerrorAttack', back_populates='target_types')

    def __repr__(self):
        return f"<TerrorAttackTargetType(target_type_id-{self.target_type_id}, terror_attack_id-{self.terror_attack_id})>"
