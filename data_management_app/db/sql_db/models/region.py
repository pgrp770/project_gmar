from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_management_app.db.sql_db.models import Base


class Region(Base):

    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    countries = relationship('Country', back_populates='region')