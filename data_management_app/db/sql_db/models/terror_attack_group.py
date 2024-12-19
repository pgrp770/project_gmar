from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttackGroup(Base):
    __tablename__ = 'terror_attack_group_relations'
    id = Column(Integer, primary_key=True)

    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='terror_attacks')

    terror_attack_id = Column(Integer, ForeignKey('terror_attacks.id'))
    terror_attacks = relationship('TerrorAttack', back_populates='groups')

    def __repr__(self):
        return f"'{self.terror_attack_id}, {self.group_id}'"