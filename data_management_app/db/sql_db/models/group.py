from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class Group(Base):

    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    terror_attacks = relationship('TerrorAttackGroup', back_populates='group')

    def __repr__(self):
        return f'<Group(id={self.id}, name={self.name})>'
