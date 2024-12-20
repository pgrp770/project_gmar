from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class TargetType(Base):

    __tablename__ = 'target_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    terror_attacks = relationship('TerrorAttackTargetType', back_populates='target_type')

    def __repr__(self):
        return f'<TargetType(id={self.id}, name={self.name})>'
