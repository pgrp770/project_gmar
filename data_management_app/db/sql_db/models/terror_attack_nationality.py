from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TerrorAttackNationality(Base):

    __tablename__ = 'terror_attack_nationality_relations'

    id = Column(Integer, primary_key=True)

    nationality_id = Column(Integer, ForeignKey('nationalities.id'))
    nationality = relationship('Nationality', back_populates='terror_attacks', lazy='joined')

    terror_attack_id = Column(Integer, ForeignKey('terror_attacks.id'))
    terror_attacks = relationship('TerrorAttack', back_populates='nationalities', lazy='joined')

    def __repr__(self):
        return f"<TerrorAttackNationality<(nationality_id-{self.nationality_id}, terror_attack_id-{self.terror_attack_id})>"
