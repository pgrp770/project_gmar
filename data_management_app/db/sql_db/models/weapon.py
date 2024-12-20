from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class Weapon(Base):
    __tablename__ = 'weapons'
    id = Column(Integer, primary_key=True)

    name = Column(String)

    terror_attacks = relationship('TerrorAttackWeapon', back_populates='weapon', lazy='joined')

    def __repr__(self):
        return f'<Weapon(id-{self.id}, name-{self.name})>'
